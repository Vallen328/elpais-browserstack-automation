import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.image_downloader import ImageDownloader
from core.translator import TitleTranslator
from core.driver_factory import create_browserstack_driver


class ElPaisScraper:

    def __init__(self, capability=None, headless=False):

        if capability:
            self.driver = create_browserstack_driver(capability)
        else:
            chrome_options = Options()

            if headless:
                chrome_options.add_argument("--headless=new")

            chrome_options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(options=chrome_options)

        self.wait = WebDriverWait(self.driver, 10)
        self.image_downloader = ImageDownloader()
        self.translator = TitleTranslator()

    def close(self):
        self.driver.quit()

    def _accept_cookies(self):
        try:
            accept_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'Aceptar')]")
                )
            )
            accept_button.click()
        except:
            pass

    def _get_opinion_links(self):

        self.driver.get("https://elpais.com")
        self._accept_cookies()

        self.driver.get("https://elpais.com/opinion/")

        self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//article//h2/a | //article//h3/a")
            )
        )

        # Scroll for lazy loading
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(3)

        headline_links = self.driver.find_elements(
            By.XPATH,
            "//article//h2/a | //article//h3/a"
        )

        unique_articles = []
        seen_links = set()

        for link_element in headline_links:
            link = link_element.get_attribute("href")
            title = self.driver.execute_script(
                "return arguments[0].innerText;",
                link_element
            )
            title = title.strip() if title else ""

            if title and link and link not in seen_links:
                seen_links.add(link)
                unique_articles.append((title, link))

            if len(unique_articles) == 5:
                break

        return unique_articles

    def _extract_article_details(self, title, link):

        self.driver.get(link)

        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )

        article_element = self.driver.find_element(By.TAG_NAME, "article")

        paragraphs = self.driver.execute_script("""
            const article = arguments[0];
            return Array.from(article.querySelectorAll("p"))
                .map(p => p.innerText);
        """, article_element)

        content = "\n".join(
            [p.strip() for p in paragraphs if p.strip()]
        )

        # Fallback if no content found
        if not content:
            content = "No structured article body found."

        image_url = None
        try:
            image_element = self.driver.find_element(
                By.XPATH, "//figure//img"
            )
            image_url = image_element.get_attribute("src")
        except:
            pass

        saved_image_path = None

        if image_url:
            saved_image_path = self.image_downloader.download(image_url)

        translated_title = self.translator.translate(title)

        return {
            "title": title,
            "translated_title": translated_title,
            "link": link,
            "content": content,
            "image_url": image_url,
            "image_path": saved_image_path
        }

    def scrape(self):

        articles_data = []

        opinion_links = self._get_opinion_links()

        for title, link in opinion_links:
            article_data = self._extract_article_details(title, link)
            articles_data.append(article_data)

        return articles_data
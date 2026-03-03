from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.browserstack_config import (
    BROWSERSTACK_USERNAME,
    BROWSERSTACK_ACCESS_KEY
)


def create_browserstack_driver(capability):

    url = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub"

    options = webdriver.ChromeOptions()

    for key, value in capability.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    return driver
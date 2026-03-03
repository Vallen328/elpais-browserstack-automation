from concurrent.futures import ThreadPoolExecutor
from core.scraper import ElPaisScraper
from config.browserstack_config import CAPABILITIES


def mark_test_status(driver, status, reason):
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"' + status + '", "reason": "' + reason + '"}}'
    )


def run_test(capability):

    session_name = capability["bstack:options"]["sessionName"]
    print(f"Starting test: {session_name}")

    scraper = ElPaisScraper(capability=capability)

    try:
        scraper.scrape()

        # Mark as passed
        mark_test_status(
            scraper.driver,
            "passed",
            "Scraping completed successfully"
        )

        print(f"Completed test: {session_name}")

    except Exception as e:

        # Mark as failed
        mark_test_status(
            scraper.driver,
            "failed",
            f"Test failed due to: {str(e)}"
        )

        print(f"Failed test: {session_name}")
        print(str(e))

    finally:
        scraper.close()


def main():

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_test, CAPABILITIES)


if __name__ == "__main__":
    main()
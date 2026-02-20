from core.logger import get_logger


class BasePage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.logger.info(f"Filling {locator} with {value}")
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        self.logger.info(f"Getting text from {locator}")
        return self.page.locator(locator).inner_text()

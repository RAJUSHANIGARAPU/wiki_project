from core.base_page import BasePage
from ui.locators.wiki_locators import WikiLocators


class HomePage(BasePage):
    def search(self, text):
        self.fill(WikiLocators.SEARCH_BOX, text)
        self.page.keyboard.press("Enter")

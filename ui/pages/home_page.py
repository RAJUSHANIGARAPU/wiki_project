from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from core.base_page import BasePage


class HomePage(BasePage):
    def navigate(self):
        base_url = self.config.get_base_url()
        self.page.goto(base_url)

    def accept_cookies(self):
        try:
            button = self.resolve("cookie_accept_button")
            button.wait_for(state="visible", timeout=5000)
            button.click()
            self.resolve("cookie_overlay").wait_for(state="hidden")
        except PlaywrightTimeoutError:
            pass

    def close_register_popup_if_present(self):
        try:
            self.resolve("register_popup_close").click(timeout=3000)
        except PlaywrightTimeoutError:
            pass

    def search(self, keyword):
        self.resolve("search_input").first.fill(keyword)
        self.resolve("search_button").click()

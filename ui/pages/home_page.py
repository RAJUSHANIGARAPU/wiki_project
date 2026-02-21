from core.base_page import BasePage


class HomePage(BasePage):

    def navigate(self):
        base_url = self.config.get_base_url()
        self.page.goto(base_url)

    def accept_cookies(self):
        try:
            self.resolve("cookie_accept_button").click(timeout=3000)
        except:
            pass

    def close_register_popup_if_present(self):
        try:
            self.resolve("register_popup_close").click(timeout=3000)
        except:
            pass

    def search(self, keyword):
        self.resolve("search_input").first.fill(keyword)
        self.resolve("search_button").click()
import re

from playwright.sync_api import expect

from core.base_page import BasePage


class SearchResultsPage(BasePage):
    def click_second_lot(self):
        lots = self.resolve("lot_cards")
        lots.nth(1).click()

    def verify_results_page_loaded(self, keyword: str):
        expect(self.page).to_have_url(re.compile(rf"/en/s\?q={keyword}"))
        expect(self.resolve("lot_cards").first).to_be_visible()
        expect(self.page.get_by_role("heading", level=1)).to_contain_text(keyword)

    def verify_no_results_displayed(self):
        message = self.resolve("search_no_results_message")
        expect(message).to_be_visible()

import re

from playwright.sync_api import expect

from core.base_page import BasePage


class LotPage(BasePage):
    def get_title(self):
        return self.resolve("lot_title").inner_text().strip()

    def get_favorites(self):
        return self.resolve("lot_favorites_button").first.get_attribute("count")

    def get_current_bid(self):
        section = self.resolve("current_bid_section")
        # Get the bid title (Current bid / Starting bid)
        bid_type = section.locator("div[class*='status-title']").first.inner_text().strip()
        # Get the € amount
        amount = section.locator("div[class*='bid-amount']").first.inner_text().strip()
        return bid_type, amount

    def verify_lot_page_loaded(self):
        # verify lot id pattern exists
        expect(self.page).to_have_url(re.compile(r"/en/l/\d+-"))
        expect(self.resolve("lot_title")).to_be_visible()

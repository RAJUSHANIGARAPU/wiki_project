import re

from playwright.sync_api import expect

from core.base_page import BasePage


class LotPage(BasePage):
    def get_title(self):
        return self.resolve("lot_title").inner_text().strip()

    def get_current_bid(self):
        section = self.resolve("current_bid_section")
        bid_type = section.get_by_text("bid", exact=False).first.inner_text().strip()
        amount = section.get_by_text("€").first.inner_text().strip()
        return bid_type, amount

    def get_favorites(self):
        return self.resolve("lot_favorites_button").first.get_attribute("count")

    def verify_lot_page_loaded(self):
        # verify lot id pattern exists
        expect(self.page).to_have_url(re.compile(r"/en/l/\d+-"))
        expect(self.resolve("lot_title")).to_be_visible()

import re
from core.base_page import BasePage
from playwright.sync_api import expect

class LotPage(BasePage):

    def get_title(self):
        return self.resolve("lot_title").inner_text().strip()

    def get_favorites(self):
        return self.resolve("lot_favorites_button").first.get_attribute("count")

    def get_current_bid(self):
        section = self.resolve("current_bid_section")
        return section.locator("text=€").first.inner_text().strip()

    def verify_lot_page_loaded(self):
        # verify lot id pattern exists
        expect(self.page).to_have_url(
            re.compile(r"/en/l/\d+-")
        )
        expect(self.resolve("lot_title")).to_be_visible()
        expect(
            self.resolve("current_bid_section")
            .get_by_text("Current bid")
        ).to_be_visible()
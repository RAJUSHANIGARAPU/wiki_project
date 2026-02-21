from ui.pages.home_page import HomePage
from ui.pages.search_results_page import SearchResultsPage
from ui.pages.lot_page import LotPage


class SearchFlow:

    def __init__(self, page, config):
        self.home = HomePage(page, config)
        self.results = SearchResultsPage(page, config)
        self.lot = LotPage(page, config)

    def search_and_open_second_lot(self, keyword):
        self.home.navigate()
        self.home.accept_cookies()
        self.home.search(keyword)
        self.home.close_register_popup_if_present()
        self.results.verify_results_page_loaded(keyword)
        self.results.click_second_lot()
        self.lot.verify_lot_page_loaded()

    def search_and_verify_no_results(self, keyword):
        self.home.navigate()
        self.home.accept_cookies()
        self.home.search(keyword)
        self.results.verify_no_results_displayed()
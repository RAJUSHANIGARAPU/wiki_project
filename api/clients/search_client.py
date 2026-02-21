import requests


class SearchClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, keyword):
        return requests.get(f"{self.base_url}/en/s", params={"q": keyword}, timeout=10)

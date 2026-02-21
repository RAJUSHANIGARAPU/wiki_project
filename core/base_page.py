import json
from pathlib import Path


class BasePage:
    def __init__(self, page, config):
        self.page = page
        self.config = config

        locator_path = Path("ui/locators/wiki_locators.json")
        with open(locator_path) as f:
            self.locators = json.load(f)

    def resolve(self, key):
        locator = self.locators[key]
        locator_type = locator["type"]

        if locator_type == "css":
            return self.page.locator(locator["value"])

        if locator_type == "role":
            return self.page.get_by_role(locator["role"], name=locator["name"])

        if locator_type == "placeholder":
            return self.page.get_by_placeholder(locator["value"])

        if locator_type == "testid":
            return self.page.get_by_test_id(locator["value"])

        raise ValueError(f"Unsupported locator type: {locator_type}")

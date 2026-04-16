import re

from playwright.sync_api import Page
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/") -> None:
        self.page.goto(f"{self.base_url}{path}")

    @staticmethod
    def normalize_path(path: str) -> str:
        return "/" if path == "/" else f"/{path.strip('/')}/"

    def assert_url(self, path: str) -> None:
        normalized = self.normalize_path(path)
        escaped_url = re.escape(f"{self.base_url}{normalized}")
        expect(self.page).to_have_url(re.compile(rf"^{escaped_url}(?:[#?].*)?$"))

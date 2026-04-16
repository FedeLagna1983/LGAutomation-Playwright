from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import expect

from .base_page import BasePage

if TYPE_CHECKING:
    from .home_page import HomePage


class ContactPage(BasePage):
    HOME_LOGO_LINK = "img[alt='LG Ad Solutions'], a[aria-label='LG Ad Solutions'], header a[href='/'], header a[href$='lgads.tv/']"

    def assert_is_contact_page(self, path: str = "/contact/") -> "ContactPage":
        self.assert_url(path)
        expect(self.page.locator(self.HOME_LOGO_LINK).first).to_be_visible()
        return self

    def click_lg_ad_solutions_logo(self, home_path: str = "/") -> "HomePage":
        from .home_page import HomePage

        self.page.locator(self.HOME_LOGO_LINK).first.click()
        home_page = HomePage(self.page, self.base_url)
        return home_page.assert_is_home_page(home_path)

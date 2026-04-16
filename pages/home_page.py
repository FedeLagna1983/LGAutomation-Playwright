from __future__ import annotations

import re
from typing import TYPE_CHECKING

from playwright.sync_api import Page, expect

from .base_page import BasePage

if TYPE_CHECKING:
    from .contact_page import ContactPage


class HomePage(BasePage):
    CONTACT_LINK_NAME = "Contact"
    HOME_LOGO = "img[alt='LG Ad Solutions'], a[aria-label='LG Ad Solutions'], header a[href='/'], header a[href$='lgads.tv/']"

    def open(self, path: str = "/") -> "HomePage":
        self.goto(path)
        return self.assert_is_home_page(path)

    def go_to_contact(self, contact_path: str = "/contact/") -> "ContactPage":
        from .contact_page import ContactPage

        contact_link = self.page.get_by_role("link", name=self.CONTACT_LINK_NAME, exact=True).first
        expect(contact_link).to_be_visible()
        contact_link.click()
        contact_page = ContactPage(self.page, self.base_url)
        return contact_page.assert_is_contact_page(contact_path)

    def click_lg_ad_solutions_logo(self) -> "HomePage":
        self.page.locator(self.HOME_LOGO).first.click()
        return self.assert_is_home_page()

    def assert_is_home_page(self, path: str = "/") -> "HomePage":
        self.assert_url(path)
        contact_link = self.page.get_by_role("link", name=self.CONTACT_LINK_NAME, exact=True).first
        expect(contact_link).to_be_visible()
        return self

    def assert_text_visible_with_scroll(self, expected_text: str, max_scrolls: int = 8) -> "HomePage":
        normalized_regex = re.compile(r"\s+".join(re.escape(word) for word in expected_text.split()), re.IGNORECASE)
        text_locator = self.page.get_by_text(normalized_regex).first

        for _ in range(max_scrolls):
            if text_locator.is_visible():
                return self
            self.page.mouse.wheel(0, 1400)
            self.page.wait_for_timeout(250)

        expect(text_locator).to_be_visible()
        return self

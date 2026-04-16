from __future__ import annotations

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, scenarios, then

from pages.home_page import HomePage


scenarios("features/home_navigation.feature")


@pytest.fixture
def home_content_context() -> dict[str, object]:
    return {}


@given("que el usuario abre la pagina Home para validar contenidos")
def open_home_for_content_validation(
    home_page: HomePage, home_content_context: dict[str, object]
) -> None:
    opened_home = home_page.open("/")
    home_content_context["home_page"] = opened_home


@then(parsers.parse('debe ver el texto "{expected_text}"'))
def assert_expected_text(
    expected_text: str, home_content_context: dict[str, object]
) -> None:
    opened_home = home_content_context["home_page"]
    assert isinstance(opened_home, HomePage)
    opened_home.assert_text_visible_with_scroll(expected_text)


@then("debe cerrar el navegador")
def close_browser(page: Page) -> None:
    if not page.is_closed():
        page.close()

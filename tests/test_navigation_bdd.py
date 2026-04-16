from __future__ import annotations

import pytest
from pytest_bdd import given, scenarios, then, when

from pages.contact_page import ContactPage
from pages.home_page import HomePage


scenarios("features/navigation.feature")


@pytest.fixture
def bdd_context() -> dict[str, object]:
    return {}


@given("que el usuario abre la pagina Home")
def open_home(home_page: HomePage, bdd_context: dict[str, object]) -> None:
    opened_home = home_page.open("/")
    bdd_context["home_page"] = opened_home
    bdd_context["home_path"] = "/"
    bdd_context["contact_path"] = "/contact/"


@when("hace click en el enlace Contact del menu")
def go_to_contact(bdd_context: dict[str, object]) -> None:
    home_page = bdd_context["home_page"]
    assert isinstance(home_page, HomePage)
    contact_path = str(bdd_context["contact_path"])
    contact_page = home_page.go_to_contact(contact_path)
    bdd_context["contact_page"] = contact_page


@then("debe ver la pagina Contact")
def assert_contact(bdd_context: dict[str, object]) -> None:
    contact_page = bdd_context["contact_page"]
    assert isinstance(contact_page, ContactPage)
    contact_path = str(bdd_context["contact_path"])
    contact_page.assert_is_contact_page(contact_path)


@when("hace click en el logo de LG Ad Solutions")
def click_logo_to_return_home(bdd_context: dict[str, object]) -> None:
    contact_page = bdd_context["contact_page"]
    assert isinstance(contact_page, ContactPage)
    home_path = str(bdd_context["home_path"])
    returned_home = contact_page.click_lg_ad_solutions_logo(home_path)
    bdd_context["returned_home"] = returned_home


@then("debe volver a la pagina Home")
def assert_home(bdd_context: dict[str, object]) -> None:
    returned_home = bdd_context["returned_home"]
    assert isinstance(returned_home, HomePage)
    home_path = str(bdd_context["home_path"])
    returned_home.assert_is_home_page(home_path)

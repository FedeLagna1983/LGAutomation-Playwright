from pages.home_page import HomePage


def test_navigation_from_home_to_contact_and_back(
    home_page: HomePage, navigation_case: dict[str, str]
) -> None:
    opened_home = home_page.open(navigation_case["home_path"])
    contact_page = opened_home.go_to_contact(navigation_case["contact_path"])
    contact_page.assert_is_contact_page(navigation_case["contact_path"])
    returned_home = contact_page.click_lg_ad_solutions_logo(navigation_case["home_path"])

    returned_home.assert_is_home_page(navigation_case["home_path"])

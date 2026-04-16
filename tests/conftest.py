import json
import os
import re
from datetime import datetime
from functools import lru_cache
from pathlib import Path

import pytest

from pages.home_page import HomePage
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://lgads.tv")


@pytest.fixture
def home_page(page: Page, base_url: str) -> HomePage:
    return HomePage(page, base_url)


@lru_cache(maxsize=1)
def _load_navigation_cases() -> tuple[dict[str, str], ...]:
    data_path = Path(__file__).parent / "data" / "navigation_cases.json"
    raw_cases = json.loads(data_path.read_text(encoding="utf-8"))
    return tuple(raw_cases)


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "navigation_case" not in metafunc.fixturenames:
        return
    cases = list(_load_navigation_cases())
    ids = [case["name"] for case in cases]
    metafunc.parametrize("navigation_case", cases, ids=ids)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request: pytest.FixtureRequest, page: Page) -> None:
    yield
    rep_call = getattr(request.node, "rep_call", None)
    if not rep_call or rep_call.passed:
        return

    artifacts_dir = Path("artifacts") / "screenshots"
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = re.sub(r"[^\w.-]+", "_", request.node.nodeid)
    screenshot_path = artifacts_dir / f"{safe_name}_{timestamp}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]) -> None:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

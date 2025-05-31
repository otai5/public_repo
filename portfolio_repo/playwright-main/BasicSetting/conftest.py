from web.BasicSetting.import_list import *

# 드라이버 세팅
@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function", autouse=True)
def adjust_browser_resolution(page):
    # 원하는 해상도로 변경
    page.set_viewport_size({"width": 1920, "height": 1200})


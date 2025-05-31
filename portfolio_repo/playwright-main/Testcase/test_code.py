from ObjectSetting.common_object import *

def checkout(page):
    CommonElements.login_func(page)

def test_playwright_001(page):
    PageElements.main_url(page)
    CommonElements.login_func(page)
    # validation
    expect(page.get_by_role("link", name="닉네임"), '회원정보 미노출').to_be_visible()
    page.close()
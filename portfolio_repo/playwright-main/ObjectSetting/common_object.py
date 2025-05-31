from BasicSetting.conftest import *

class PageElements():
    def main_url(page):
        page.goto('https://test.url.com/')

class CommonElements():
    # 로그인
    def login_func(page):
        page.get_by_role("link", name="로그인").click()
        page.get_by_placeholder("이메일").click()
        page.get_by_placeholder("이메일").fill("test@mail.com")
        page.get_by_placeholder("비밀번호").click()
        page.get_by_placeholder("비밀번호").fill("password")
        page.get_by_role("button", name="로그인").click()
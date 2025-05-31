from conftest import *
from pages.object_setting import *

def test_case_001(driver):
    #로그인 수행
    MainElements.xyclick(driver,1000,1000) # 좌표 클릭
    LoginElements.login_func()

    # validation
    assert MainElements.is_visible(), "요소 미노출"




from import_list import *
from appium.webdriver.common.appiumby import AppiumBy

## 로그인 관련 ###############################################################
class LoginElements():
    # 로그인 하기
    def login_func(driver):
        # 요소 정의
        driver.username = (AppiumBy.ID, "com.bucketplace:id/input_username")
        driver.password = (AppiumBy.ID, "com.bucketplace:id/input_password")
        driver.login_button = (AppiumBy.ID, "com.bucketplace:id/button_login")

        # 로그인
        driver.username.send_keys("id")
        driver.password.send_keys("password")
        driver.login_button.click()

        # 웰컴 팝업 분기 제어
        try:
            if driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='닫기']"):
                driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='닫기']").click()
        except Exception:
            print("팝업 미노출")

## 기타 공통 함수 ###############################################################
class MainElements():
    def xyclick(driver, x, y):
        # 좌표 클릭 첫번째
        pointer_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(driver, mouse=pointer_input)
        action_builder.pointer_action.move_to_location(x, y).click()
        action_builder.perform()

    def is_visible(driver):
        # 요소 정의
        main_logo = (AppiumBy.ID, "com.bucketplace:id/logo_main")
        return driver.find_element(*driver.main_logo).is_displayed()

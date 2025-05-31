from pages.import_list import *

# 드라이버 세팅 정보
@pytest.fixture(autouse=False, scope='module')
def driver():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities={
            'appActivity': 'se.ohou.screen.splash.SplashActivity',
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'udid': 'udid-no'
        })
    yield driver

    # 테스트 종료 시 driver 종료
    driver.quit()

from BasicSetting.import_list import *
from BasicSetting.object_setting import *
from BasicSetting.conftest import *
import pyperclip

def test_case_001(driver, worksheet):
    print("\ntest_case_001 : summary", end='')
    result = LobbyGuestElements.lobby_guest_allow_text(driver, worksheet).text
    assert result == 'sample_text'
    time.sleep(1)

def test_case_002(driver0, worksheet):
    print("\ntest_case_002 : summary", end='')
    result = driver0.find_element(By.CSS_SELECTOR, 'button[data-tooltip]').get_attribute('data-tooltip')
    time.sleep(1)
    driver0.quit()

def test_case_003(driver, worksheet):
    print("\ntest_case_003 : summary", end='')
    try:
        if driver.find_element(By.XPATH, "/sample_xpath"): # sample
            LobbyGuestElements.login_func(driver)
    except NoSuchElementException:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    driver.find_element(By.CSS_SELECTOR, '#css_path').click() # sample
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()  # 팝업 종료
    result = LobbyGuestElements.lobby_guest_allow_text(driver, worksheet).text
    assert result == 'sample_text'
    time.sleep(3)

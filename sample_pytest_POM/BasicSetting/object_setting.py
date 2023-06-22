from BasicSetting.import_list import *
from BasicSetting.conftest import *

class SampleElements_1():
    # 로그인 하기 공통 함수 생성 (sample)
    def login_func(driver):
        driver.find_element(By.XPATH, "/xpath").click()
        driver.find_element(By.XPATH, "/xpath").send_keys("sampletext")
        driver.find_element(By.CLASS_NAME, "smaple").click()
        time.sleep(1)

    # Elements 공통 함수 생성 (Google spread 텍스트 연동)
    def elements_sample_01(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

    def elements_sample_02(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

class SampleElements_2():
    # Elements 공통 함수 생성 (Google spread 텍스트 연동)
    def elements_sample_03(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

    def elements_sample_04(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text
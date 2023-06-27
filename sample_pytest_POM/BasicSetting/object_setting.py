from BasicSetting.import_list import *
from BasicSetting.conftest import *

class SampleElements_1():
    # Login Func(sample)
    def login_func(driver):
        # ID & PW Input
        driver.find_element(By.XPATH, "/id_xpath").click()
        driver.find_element(By.XPATH, "/id_xpath").send_keys("id")
        driver.find_element(By.XPATH, "/pw_xpath").click()
        driver.find_element(By.XPATH, "/pw_xpath").send_keys("pw")
        driver.find_element(By.CLASS_NAME, "smaple").click()
        time.sleep(1)

    # common elements (Google spread sheet 연동)
    def elements_sample_01(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

    def elements_sample_02(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

class SampleElements_2():
    # common elements (Google spread sheet 연동)
    def elements_sample_03(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

    def elements_sample_04(driver, worksheet):
        for cell in worksheet.findall('sample_text', in_column=7):
            text = driver.find_element(By.XPATH, worksheet.cell(cell.row, 8).value)
        return text

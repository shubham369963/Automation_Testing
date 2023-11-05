from selenium.webdriver.common.by import By
import time
import pytest

from PageObject.Login1 import Login2


@pytest.mark.usefixtures("setup")
class TestLogin1:

    def test_001(self):
        lg = Login2(self.driver)
        lg.textbox_email("shubhamhalade1712@gmail.com")
        lg.textbox_pwd("123")
        lg.click_btn()


    def test_002(self):
        self.driver.find_element(By.ID, value="formBasicEmail").send_keys("shubhamhalade1712@gmail.com")
        self.driver.find_element(By.ID, value="formBasicPassword").send_keys("12")
        self.driver.find_element(By.CLASS_NAME, value="mt-4.btn.btn-primary").click()
        time.sleep(5)

    def test_003(self):
        self.driver.find_element(By.ID, value="formBasicEmail").send_keys("shubhamhalade1712@gmail.com")
        self.driver.find_element(By.ID, value="formBasicPassword").send_keys("123")
        self.driver.find_element(By.CLASS_NAME, value="mt-4.btn.btn-primary").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="navbarScroll"]/div[1]/form/input').send_keys("Nice")
        time.sleep(5)
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

@pytest.fixture
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    request.cls.driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver.get("https://codify-app.onrender.com/login")
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()
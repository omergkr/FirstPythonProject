import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectName", "Password123", "Your username is invalid!"),
                              ("student", "Password1234", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        time.sleep(3)
        assert login_page.get_error_message() == expected_error_message


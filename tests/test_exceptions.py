import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.exception_page import ExceptionPage


class TestExceptionScenarios:
    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_row()

    @pytest.mark.exception
    def test_element_not_intractable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_row()
        exception_page.type_row2_input("burger")
        exception_page.save_row_row2()
        assert exception_page.get_confirmation_text() == "Row 2 was saved"

    @pytest.mark.exception
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.click_edit_button()
        exception_page.clear_row1_text()

        new_input = "burger"
        exception_page.type_row1_input(new_input)
        assert exception_page.get_row1_attribute("value") == new_input

        exception_page.save_row_row1()
        assert exception_page.get_confirmation_text() == "Row 1 was saved"

    @pytest.mark.exception
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()

        assert exception_page.get_instructions_text() == "Push “Add” button to add another row"

        exception_page.add_row()
        assert exception_page.is_invisibility_instructions()

    @pytest.mark.exception
    def test_time_out_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_row()
        # when timeout is 3 second -> timeout exception, then increase the time to 10
        wait = WebDriverWait(driver, 10)
        row2_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row2_input.is_displayed()
        # assert exception_page.row2_input_is_displayed()

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utils import get_matching_answer, close_application


# Handle form steps and collect unanswered questions
def handle_form_step(driver, answers, unanswered_questions):
    try:
        # Find all input fields
        input_fields = driver.find_elements(By.TAG_NAME, 'input')
        for input_field in input_fields:
            field_name = input_field.get_attribute('name')
            answer = get_matching_answer(field_name, answers)
            if answer:
                input_field.send_keys(answer)
            else:
                unanswered_questions.add(field_name)

        # Find all dropdowns
        dropdowns = driver.find_elements(By.TAG_NAME, 'select')
        for dropdown in dropdowns:
            field_name = dropdown.get_attribute('name')
            answer = get_matching_answer(field_name, answers)
            if answer:
                for option in dropdown.find_elements(By.TAG_NAME, 'option'):
                    if option.text == answer:
                        option.click()
                        break
            else:
                unanswered_questions.add(field_name)

        # Find all checkboxes
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            field_name = checkbox.get_attribute('name')
            answer = get_matching_answer(field_name, answers)
            if answer and answer is True:
                if not checkbox.is_selected():
                    checkbox.click()
            else:
                unanswered_questions.add(field_name)

        # Try to find and click the first button to proceed
        button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
        button.click()
        return True
    except NoSuchElementException:
        try:
            # If the first button is not found, try to find and click the second button
            button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
            button.click()
            return True
        except NoSuchElementException:
            # If neither button is found, return False
            return False

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import os


def load_answers(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)


# Save unanswered questions to a JSON file
def save_unanswered_questions(unanswered_questions, json_file):
    with open(json_file, 'w') as file:
        json.dump(unanswered_questions, file, indent=4)


def next_page(driver):
    try:
        # Try to find and click the first button
        button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
        button.click()
        return 0
    except NoSuchElementException:
        try:
            # If the first button is not found, try to find and click the second button
            button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
            button.click()

            button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            button.click()

            return 1
        except NoSuchElementException:
            # If neither button is found, just return
            return 2


def get_matching_answer(element_name, answers):
    # Find a key in the answers dictionary that matches a part of the element_name
    for key in answers.keys():
        if key in element_name:
            return answers[key]
    return None


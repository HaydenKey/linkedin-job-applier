from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import scripts


def main():
    # Load answers from JSON
    answers = load_answers('answers.json')

    # Initialize a set to collect unanswered questions
    unanswered_questions = set()

    load_dotenv()
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to the desired webpage
    scripts.navigate_to_jobs(driver)

    # Loop through form steps until there are no more steps
    while scripts.handle_form_step(driver, answers, unanswered_questions):
        # Optionally add a short wait to ensure the page loads properly
        time.sleep(1)

    # Save unanswered questions to a JSON file
    if unanswered_questions:
        scripts.save_unanswered_questions(list(unanswered_questions), 'unanswered_questions.json')

    # Close the WebDriver
    driver.quit()


if __name__ == "__main__":
    main()

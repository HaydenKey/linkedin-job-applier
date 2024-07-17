from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# TODO: complete get_matching_answer()
# TODO: populate answers.json
def get_matching_answer(element_name, answers):
    for key in answers.keys():
        if key in element_name:
            return answers[key]
    return None


def navigate_to_jobs(driver):
    driver.get("https://www.linkedin.com/")

    # Locate the <a> element with the text content "Sign In" using XPath
    driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]").click()

    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(os.getenv('LINKEDIN_EMAIL'))

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(os.getenv('LINKEDIN_PASSWORD'))

    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
    login_button.click()

    driver.find_element(By.XPATH, "//a[@href='https://www.linkedin.com/jobs/?']").click()

    time.sleep(2)

    top_job_picks = (driver.find_element(By.XPATH, "//ul[@id='jobs-home-vertical-list__entity-list']"))

    top_job_picks.find_element(By.TAG_NAME, "li").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@class='jobs-apply-button--top-card']").click()


def close_application(driver):
    try:
        close_button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
        close_button.click()

        time.sleep(2)

        close_button = driver.find_element(By.XPATH, "//button[@data-control-name='save_application_btn']")
        close_button.click()

    except NoSuchElementException:
        print("Close button not found, unable to close application gracefully.")

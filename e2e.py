from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="C:/Users/Shaked/Downloads/chromedriver_win32/chromedriver.exe")


def test_scores_service():
    browser.get("http://127.0.0.1:5000/")
    element = int(browser.find_element(by=By.ID, value='score').text)

    if 1 >= element >= 1000:
        return True
    else:
        return False


def main_function():
    test = test_scores_service()
    if test:
        return exit(0)
    else:
        return exit(-1)


main_function()

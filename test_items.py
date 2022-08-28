from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestButton:
    def test_button(self, browser):

        # opening the page
        browser.get(link)

        # 30 sec waiting
        time.sleep(30)

        # checking the button
        assert browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')


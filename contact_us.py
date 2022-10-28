from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import Helpers
from test_data import mycredentials
from selenium.webdriver.support.ui import Select


class ContactUsPage(Helpers):
    select_list = (By.XPATH, "//select[@id='id_contact']")
    email = (By.XPATH, "//input[@id='email']") # Anna - xpath was incorrect I have changed
    send_button = (By.XPATH, "//span[text()='Send']")
    my_message = (By.XPATH, "//div[@class='alert alert-danger']//li")

    def drop_down(self):
        select_list_el = self.browser.find_element(*self.select_list)
        # Anna - select get element as argument, so no need to pass this element with *
        select_list = Select(select_list_el)
        select_list.select_by_visible_text('Customer service') #Anna - no need to click after select

    def input_fields(self):
        self.browser.find_element(*self.email).send_keys(
            mycredentials['myemail'])
        self.browser.find_element(*self.send_button).click()

    def my_result(self):
        self.browser.find_element(*self.my_message).text
        # Anna - should add return
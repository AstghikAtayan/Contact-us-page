from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import Helpers
from test_data import mycredentials
from selenium.webdriver.support.ui import Select


class ContactUsPage(Helpers):
    select_list = (By.XPATH, "//select[@id='id_contact']")
    email = (By.XPATH, "//div[@id='uniform-id_contact']")
    send_button = (By.XPATH, "//span[text()='Send']")
    my_message = (By.XPATH, "//div[@class='alert alert-danger']//li")

    def drop_down(self):
        select_list = self.browser.find_element(*self.select_list)
        select_list = Select(*self.select_list)
        select_list.select_by_visible_text('Customer service').click()

    def input_fields(self): 
        self.browser.find_element(*self.email).send_keys(
            mycredentials['myemail'])
        self.browser.find_element(*self.send_button).click()

    def my_result(self):
        self.browser.find_element(*self.my_message).text
        
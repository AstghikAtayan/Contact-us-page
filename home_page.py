from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import Helpers


class Homepage(Helpers):
    contact_us = (By.XPATH, "//div[@id='contact-link']//a")

    def select_contact(self):
        self.browser.find_element(*self.contact_us).click()

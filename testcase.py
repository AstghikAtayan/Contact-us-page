from selenium import webdriver
from helper import Helpers
from contact_us import ContactUsPage
from home_page import Homepage
from test_data import mycredentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()


my_helper = Helpers(browser)
contactpage = ContactUsPage(browser)
pagehome = Homepage(browser)

my_helper.open_url(mycredentials['URL'])
pagehome.select_contact()

WebDriverWait(browser, 15).until(EC.presence_of_element_located(
    ContactUsPage.select_list))

contactpage.drop_down()
contactpage.input_fields()

expected_res = contactpage.my_result() #Anna - your my_result() function don't return anything, so result is none
assert expected_res == mycredentials["error_message"], "Invalid output"

helper.close_browser()

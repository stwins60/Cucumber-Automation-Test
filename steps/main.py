from selenium import webdriver
from behave import *
from selenium.webdriver.common import keys
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

@given('I go to amazon.com')
def step_impl(context):
#     context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    context.driver.get("https://www.amazon.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    # nav = context.driver.find_element_by_id("nav-logo-sprites").text
    # assert "amazon" in nav
    # time.sleep(5)


@when('I enter "{search_term}" in the search bar')
def step_impl_2(context, search_term):
    search_bar = context.driver.find_element_by_id("twotabsearchtextbox")
    search_bar.send_keys(search_term)
    search_bar.send_keys(keys.Keys.ENTER)
    # time.sleep(5)


@then('I should see "{search_term}" in the search results')
def step_impl_3(context, search_term):
    search_results = context.driver.find_element_by_class_name("a-color-state").text
    assert search_term in search_results
    print(search_results)
    # time.sleep(5)

@when("I click on an item in the search results")
def step_impl_4(context):
    item = context.driver.find_element_by_class_name("s-image").get_attribute("alt")
    if item == 'HP Stream 14 Pink - Celeron N4000 - 4 GB RAM - 64 GB eMMC Storage - 14" LCD - Wireless - Bluetooth - Webcam - Windows 10 S':
        item.click()
    else:
        AssertionError("Item not found")
    # time.sleep(5)

# @then("I should see the item's title")
# def step_impl_5(context):
#     item_title = context.driver.find_element_by_id('title').text
#     assert item_title == 'HP Stream 14 Pink - Celeron N4000 - 4 GB RAM - 64 GB eMMC Storage - 14" LCD - Wireless - Bluetooth - Webcam - Windows 10 S'
    time.sleep(5)








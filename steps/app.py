from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *
import json, requests
import sys, time, random
sys.setrecursionlimit(1500)

RAND = random.randint(100, 1000)

# # @when
@given('I have a valid API key and I go to the API endpoint')
def get_driver(context):
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(f'https://api.themoviedb.org/3/movie/{RAND}?api_key=37b46b26998e792429f57babd3432089&language=en-US')
    time.sleep(15)
    return context.driver

@then("I should get the latest movie")
def api_test(context):
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.get('https://api.themoviedb.org/3/movie/latest?api_key=37b46b26998e792429f57babd3432089&language=en-US')
    response = context.driver.page_source
    time.sleep(15)
    return response


@given(u"I post a movie rating")
def api_test_3(context):
    rating = {
        "value": 7.8
    }
    if RAND < 100 or RAND > 999:
        return {'status': 400, 'message': 'Invalid movie id'}
    else:
        context.url = requests.post(f'https://api.themoviedb.org/3/movie/{RAND}/rating?\
    api_key=37b46b26998e792429f57babd3432089&language=en-US',rating)
        return context.url.json()

@then("I should get the movie rating")
def api_test_4(context):
    movie_id = RAND
    context.driver = webdriver.Chrome(r'C:\chromedriver.exe')
    context.driver.implicitly_wait(10)
    context.response = context.driver.get(f'https://api.themoviedb.org/3/movie/{movie_id}/rating?\
    api_key=37b46b26998e792429f57babd3432089&language=en-US')
    print(context.response)
    time.sleep(15)
    return context.response




def after_all(context):
    context.driver.implicitly_wait(10)
    context.driver.quit()

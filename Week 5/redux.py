from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup as bs


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
LINK = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'
LOGIN = "kristjan.veensalu@gmail.com"
PASS = "ENTER PASSWORD HERE"



def login(LOGIN_URL, login, password):
    driver.get(LOGIN_URL)
    # wait for the login page to load
    sleep(3)
    driver.find_element_by_id('email').send_keys(login)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

login(LINK, LOGIN, PASS)
sleep(3)
driver.find_element_by_class_name('_1vp5').click()
sleep(3)
driver.find_elements_by_class_name('_6-6')[2].click()
sleep(3)
for x in range(30):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.execute_script("return document.documentElement.innerHTML;")
soup = bs(html, "html.parser")

print(soup.prettify()) #The variable with the text in it is soup.
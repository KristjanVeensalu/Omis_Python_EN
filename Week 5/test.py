from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup


class FacebookCrawler:
    LOGIN_URL = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'

    def __init__(self, login, password):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

        self.login(login, password)
        sleep(5)
        self.goToFriends(login, password)
        sleep(5)
        self.goToFriends2(login, password)
        sleep(5)
        self.fetchFriends(login, password)
    def login(self, login, password):
        self.driver.get(self.LOGIN_URL)

        # wait for the login page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()

        # wait for the main page to load

    def goToFriends(self, login, password):
        self.driver.find_element_by_class_name('_1vp5').click()

    def goToFriends2(self, login, password):
        self.driver.find_elements_by_class_name('_6-6')[2].click()

    def fetchFriends(self, login, password):
        for x in range(2000):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = self.driver.execute_script("return document.documentElement.innerHTML;")
        return html

if __name__ == '__main__':
    crawler = FacebookCrawler(login='kristjan.veensalu@gmail.com', password='')
    WebSiteContent = crawler.fetchFriends("kristjan.veensalu@gmail.com", "")
    print(WebSiteContent)



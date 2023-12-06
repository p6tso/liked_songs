from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from keys import login, password
logins = []
collection = {}
class yandex_user:
    def __init__(self, login: str, password: str):
        self.login=login
        self.password=password
        logins.append(login)
    @property
    def get_data(self):
        return self.login
def auth(driver, login, password):
    driver.get('https://passport.yandex.ru/')
    driver.find_element(By.ID, 'passp-field-login').send_keys(login)
    driver.find_element(By.ID, "passp:sign-in").click()
    sleep(2)
    driver.find_element(By.ID, 'passp-field-passwd').send_keys(password)
    driver.find_element(By.ID, "passp:sign-in").click()
    collection[login] = []
    sleep(10)

def parse_music(driver, login):
    driver.get('https://music.yandex.ru/users/'+login+'/playlists/3')
    artists = driver.find_elements(By.CLASS_NAME, 'd-track__artists')
    tracks = driver.find_elements(By.CLASS_NAME, 'd-track__name')
    for a, t in tracks, artists:
        collection[login].append(t.text, a.text)


driver = webdriver.Chrome()
auth(driver, login, password)
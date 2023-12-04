import time
from pages.login_page import Loginpage


class Loginutil:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self, username, psw) -> None:
        login = Loginpage(self.driver)
        login.open_page(self.url)
        login.enter_username(username)
        login.enter_password(psw)
        login.click_login()

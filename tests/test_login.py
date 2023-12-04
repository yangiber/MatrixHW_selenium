from dotenv.main import load_dotenv
import os
import pytest
import time
from selenium import webdriver
from pages.login_page import Loginpage
from utils.login_util import Loginutil


def test_login():
    load_dotenv()
    driver = webdriver.Chrome()
    psw = os.getenv("PASSWORD")
    url = os.getenv("URL")
    user_name = os.getenv("USER_NAME")
    login = Loginpage(driver)
    loginutil = Loginutil(driver, url)
    loginutil.login(user_name, psw)
    time.sleep(1)
    assert login.get_logged_username() == os.getenv("LOGGED_USERNAME")


import os
import time
from pages.transaction_page import Transaction
from selenium import webdriver
from utils.login_util import Loginutil
from dotenv.main import load_dotenv


def test_transaction():
    load_dotenv()
    driver = webdriver.Chrome()
    psw = os.getenv("PASSWORD")
    url = os.getenv("URL")
    user_name = os.getenv("USER_NAME")
    loginutil = Loginutil(driver, url)
    loginutil.login(user_name, psw)
    time.sleep(1)
    transaction = Transaction(driver)
    completed = transaction.find_all_completed()
    assert completed == int(os.getenv("COMPLETED_ROWS"))
    driver.quit()

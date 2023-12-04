from selenium.webdriver.common.by import By


class Loginpage:

    def __init__(self, driver):
        self.driver = driver
        self.user_name_txt = (By.ID, "username")
        self.password_txt = (By.ID, "password")
        self.submit_btn = (By.ID, "log-in")
        self.logged_in_username = (By.CLASS_NAME, "logged-user-name")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_username(self, username):
        self.driver.find_element(*self.user_name_txt).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit_btn).click()

    def get_logged_username(self):
        return self.driver.find_element(*self.logged_in_username).text

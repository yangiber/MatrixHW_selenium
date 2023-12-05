from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Transaction:

    def __init__(self, driver):
        self.driver = driver
        self.status_index = 0
        self.completed_count = 0
        self.table_headers = (By.XPATH, "//table[@class='table table-padded']//th")
        self.table_body_rows = (By.XPATH, "//table[@class='table table-padded']//tbody/tr")

    def find_all_completed(self):

        header_count = self.driver.find_elements(*self.table_headers)
        body_rows_count = self.driver.find_elements(*self.table_body_rows)
        # for loop to find in which column "Status"
        for i in range(0, len(header_count)):
            if header_count[i].text == "STATUS":
                self.status_index = i + 1
                break
        # for loop go through all rows in column "Status" and count "Completed" transaction
        for j in range(1, len(body_rows_count) + 1):
            try:
                status = self.driver.find_element(By.XPATH, "//table[@class='table table-padded']//tbody/tr[" + str(
                    j) + "]/td[" + str(self.status_index) + "]")
                if status.text == "Complete":
                    self.completed_count += 1
            except NoSuchElementException:
                pass
            return self.completed_count

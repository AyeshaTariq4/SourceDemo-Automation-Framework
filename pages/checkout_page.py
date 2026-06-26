from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def customer_details(self, first, last, postal):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

    def continue_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    def finish_order(self):
        self.driver.find_element(By.ID, "finish").click()
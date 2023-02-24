import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
        # Login Menggunakan Standard User
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # klik tombol sign in
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

        def tearDown(self):
            self.browser.close()

        # Login Menggunakan Locked Out User
    def test_b_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("locked_out_user") # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

        def tearDown(self):
            self.browser.close()

        # Login Menggunakan Problem User
    def test_c_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("problem_user") # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

        def tearDown(self):
            self.browser.close()
    
if __name__ == "__main__": 
    unittest.main()
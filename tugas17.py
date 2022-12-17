import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_One_Login(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(5)

        # validasi
        assert "/web/index.php/dashboard/index" in browser.current_url

    def test_b_invalid_username(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("ibnu") # isi username yang tak valid
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]/div[2]/div/div/div/p").text

        self.assertIn('Invalid credentials', response_message)

    def test_c_invalid_password(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("tugasday17") # isi password yang tak valid
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]/div[2]/div/div/div/p").text

        self.assertIn('Invalid credentials', response_message)

    def test_d_blank_username(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("") # tanpa username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]/div[2]/form/div/div/span").text

        self.assertIn('Required', response_message)

    def test_e_blank_password(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("") # tanpa password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]/div[2]/form/div/div/span").text

        self.assertIn('Required', response_message)



class Test_Two_Logout(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_logout(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(6)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click() # klik profile button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/ul/li[4]/a").click() # klik tombol log out
        time.sleep(3)

        # validasi
        assert "/web/index.php/auth/login" in browser.current_url

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
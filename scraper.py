from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
gChromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
gChromeOptions.add_experimental_option('useAutomationExtension', False)
gChromeOptions.add_argument('--disable-blink-features=AutomationControlled')
gChromeOptions.add_argument('--profile-directory=Profile 1')
gChromeOptions.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
   
driver = webdriver.Chrome(
chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)
driver.implicitly_wait(30)


def login(username, password):
    
    driver.get('https://www.instagram.com/accounts/login/')
    try:
        driver.find_element_by_xpath("//button[text()='Accept']").click()
    except:
        pass
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//*[text()='Log In']").click()
    print('Log in successful')

login("clickhustlers","Backsp@c5")
time.sleep(3)
driver.find_element_by_xpath("//*[text()='Not Now']").click()
print ("Now complete")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(8)
email = driver.find_element_by_name('text')
email.send_keys("@Dhoni123") #put your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("dhoni@76") #put your twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.get("https://twitter.com/imVkohli/status/1548216619641368577") #change to url to which post you want to put auto comment
time.sleep(8)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("one century makes good") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("waiting for vintage form") #change to your comment here
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("goat of cricket") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("master blaster records breaker") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("classic batsman") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("chasing master") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.slee(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("king of cricket") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing batsman") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(3)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("best batsman") #change to your comment text
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.close()




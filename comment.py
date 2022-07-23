import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome("chromedriver.exe")

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@Dhoni123") #put your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("dhoni@76") #put your twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/imVkohli/status/1548216619641368577") #change to url to which post you want to put auto comment
time.sleep(15)
edit = driver.find_element_by_class_name('public-DraftStyleDefault-ltr')
edit.send_keys("one century makes good") #change to your comment text
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/span/span').click()
time.sleep(3)
edit = driver.find_element_by_class_name('public-DraftStyleDefault-ltr')
edit.send_keys("waiting for vintage form") #change to your comment here
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/span/span').click()
time.sleep(30)

#if you want more comments means add 23,24,25 line and change the comment text




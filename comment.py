import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome("chromedriver.exe")
#driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@DhoniDboss")
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("yashu1@#$")
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/dasadarshan/status/1493805149898227718")
time.sleep(15)
edit = driver.find_element_by_class_name('public-DraftStyleDefault-ltr')
edit.send_keys(f"ondu century hodi guru")
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/span/span').click()
time.sleep(3)
edit = driver.find_element_by_class_name('public-DraftStyleDefault-ltr')
edit.send_keys(f"waiting for vintage form")
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/span/span').click()
time.sleep(30)
#time.sleep(2)
#input=driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child(1) > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1f1sjgu > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
#input.send_keys(f"amazing")
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
#edit = driver.find_element_by_class_name('public-DraftStyleDefault-block public-DraftStyleDefault-ltr')
#edit.send_keys(f"good one")
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
#time.sleep(3)
#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child(1) > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1f1sjgu > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div
#edit = driver.find_element_by_class_name('public-DraftStyleDefault-block public-DraftStyleDefault-ltr')
#edit.send_keys(f"nyc one")
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()

#input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtReg"]')
#input.send_keys('19B11090') #put your reg no
#input=driver.find_element_by_css_selector('#ContentPlaceHolder1_ddlExam').click()
#input=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child(1) > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1f1sjgu > div:nth-child(2) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div
#edit = driver.find_element_by_class_name('public-DraftStyleDefault-block public-DraftStyleDefault-ltr').click()
#driver.find_element_by_id("tweet-box-reply-to-" + number).click()
#driver.find_element_by_id("tweet-box-reply-to-" + number).send_keys(amazing)
#driver.find_element_by_id("tweet-box-reply-to-" + number).send_keys(Keys.CONTROL + "\n")
#time.sleep(3)


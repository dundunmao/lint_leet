import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import codecs

# def setUp():
#     '''for Firefox'''
#     driver = webdriver.Firefox()
#     driver.get("https://www.netflix.com/browse/genre/83")
#     return driver
# def openNewtab(driver):
#     body = driver.find_element_by_tag_name("body")
#     '''for MAC'''
#     body.send_keys(Keys.COMMAND + 't')
#     # '''for other OS'''
#     # body.send_keys(Keys.CONTROL + 't')
#
#
# def gmailSignin(driver):

driver = webdriver.Firefox()
driver.get("https://www.netflix.com/browse/genre/83")

Username ="dundunmao@gmail.com"
Password = "200131083"

emailFieldEle = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_name("email"))
emailFieldEle.clear()
emailFieldEle.send_keys(Username)

passFieldEle = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_name('password'))
passFieldEle.clear()
passFieldEle.send_keys(Password)

passFieldEle.submit()

main = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_class_name('profile-icon'))
main.click()




########


NEXT_BUTTON_XPATH = '//input[@type="submit" and @title="next"]'
signinButtonEle = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_text('Sign In'))
signinButtonEle.click()

emailFieldID = "Email"
passFieldID = "Passwd"
passFieldXpath = ".//*[@id='Passwd']"
nextBtnID = "next"
signinButtonId = "signIn"


emailFieldEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(emailFieldID))
emailFieldEle.clear()
emailFieldEle.send_keys(Username)

''' Gmail has two types sign in UI'''
try:
    passFieldEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(passFieldID))

except:
    nextBtnEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(nextBtnID))
    nextBtnEle.click()
    time.sleep(10)
    # passFieldEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldID))
    passFieldEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(passFieldXpath))

passFieldEle.clear()
passFieldEle.send_keys(Password)

signinButtonEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(signinButtonId))
signinButtonEle.click()
accountXpath = ".//*[@id='gb']/div[1]/div[1]/div/div[3]/div[1]/a"
accountEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(accountXpath))

# if __name__ == "__main__":
#     driver = setUp()
#     driver = openNewtab(driver)
#     gmailSignin(driver)
#     url = 'https://www.netflix.com/browse/genre/83'
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import codecs

#my own files
# from writer import writeFile
# from appender import appendFile
# from visited import visited

# from selenium.webdriver.common.keys import Keys

class BreakIt(Exception):
    pass

def setUp():
    '''for Firefox'''
    driver = webdriver.Firefox()

    '''for chrome with chromedriver'''
    # driver = webdriver.Chrome('/Users/Julia/Downloads/chromedriver')  # Optional argument, if not specified will search path.

    driver.get("https://www.gmail.com/intl/en/mail/help/about.html")

    return driver

def openNewtab(driver):
    body = driver.find_element_by_tag_name("body")
    '''for MAC'''
    body.send_keys(Keys.COMMAND + 't')
    # '''for other OS'''
    # body.send_keys(Keys.CONTROL + 't')


def gmailSignin(driver):

    Username ="mygift930@gmail.com"
    Password = "200131083g"

    signinId = "gmail-sign-in"
    signinEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(signinId))
    signinEle.click()

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

def fillForm(driver,item,divNum,company,page):

    company = company.encode('utf-8')

    phone = "(408)499-4251"
    # comment = "Do you help Asian clients marketing in USA ? \n"
    # comment += "\n"
    comment = "Dear %s Account Manager:\n" %company.encode('utf-8')
    comment += "\n"
    comment += "Our company, Glogou Inc., a digital marketing company in Silicon Valley. We focus exclusively to help \n"
    comment += "a business to run marketing campaigns in Asian countries.  \n"
    comment += "\n"
    comment1 = "Recently, we received a few inquires from Asian and China companies, they want to market their products and services in USA.\n"
    comment1 += "Since we do not provide such services, just wonder if you provide this type of service ?\n"
    comment2 = "\n"
    comment2 += "Beside SEM, do you provide social media marketing and mobile marketing ?  What will be the minimal budget requirements of those ? "
    comment2 += "Do you provide off line marketing ?"
    comment2 += "\n"
    comment3 = "Thank you in 3:heap&deque&windows,\n"
    comment3 += "\n"
    comment3 += "Ben Lee\n"
    comment3 += "Director of Customer Services\n"
    comment4 = "Glogou Inc.\n"
    comment4 += "www.glogou.com\n"
    comment4 += "2068 Walsh Ave, #C, Santa Clara, CA, 95050\n"
    comment4 += "Email: blee@glogou.com\n"
    comment4 += "Phone: (408)499-4251\n"

    comment = comment.encode('utf-8')
    comment1 = comment1.encode('utf-8')
    comment2 = comment2.encode('utf-8')
    comment3 = comment3.encode('utf-8')
    comment4 = comment4.encode('utf-8')

    '''define locator'''

    phoneFieldXpath = "html/body/div[%d]/form/div[2]/div[2]/input[2]" %divNum
    textFieldXpath = "html/body/div[%d]/form/div[2]/textarea" %divNum
    sendEmailBtnXpath = "html/body/div[%d]/form/div[3]/a" %divNum
    closeBtnXpath = "html/body/div[%d]/form/div[1]/div[1]" %divNum


    '''open contact popup window'''
    item.click()

    #phoneFieldEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(phoneFieldXpath))
    #textFieldEle = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(textFieldXpath))

    phoneFieldEle = driver.find_element_by_xpath(phoneFieldXpath)
    textFieldEle = driver.find_element_by_xpath("//textarea[@class='gps-contact-form-comments gps-contact-field ng-pristine ng-valid ng-touched']")

    time.sleep(1)

    '''enter phone number and text'''
    phoneFieldEle.clear()
    phoneFieldEle.send_keys(phone)
    time.sleep(1)
    textFieldEle.clear()
    textFieldEle.send_keys(comment.encode('utf-8'))
    time.sleep(1)
    textFieldEle.send_keys(comment1.encode('utf-8'))
    time.sleep(1)
    textFieldEle.send_keys(comment2.encode('utf-8'))
    time.sleep(1)
    textFieldEle.send_keys(comment3.encode('utf-8'))
    time.sleep(1)
    textFieldEle.send_keys(comment4.encode('utf-8'))
    time.sleep(2)

    failedClassname = "gps-contact-success ng-hide"
    successClassname = "gps-contact-success"
    continueXpath = "html/body/div[%d]/div/div[2]/a"%divNum

    '''submit email'''
    sendEmailBtnEle = WebDriverWait(driver,2).until(lambda driver: driver.find_element_by_xpath(sendEmailBtnXpath))
    sendEmailBtnEle.click()

    '''confirm submit or not'''
    submittedXpath = "html/body/div[%d]/div" %divNum

    try:
        submittedEle = WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath(
            submittedXpath).is_displayed())
        print "********"
        print "company: ",company

        """ write company info into file """
        log = 'Success to submit Email to %s at page %s!'%(company,page)
        print log
        file_name = 'company_info'
        file_path = 'company_info'
        appendFile(file_name, file_path, log)

        '''continue searching'''
        continueEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(continueXpath))
        btn = continueEle.get_attribute("text")
        continueEle.click()


    except:
        print "********"
        print "company: ",company
        log_str = 'Failed to submit Email to %s at page %s!'%(company,page)
        print log_str
        file_name = 'form_log'
        file_path = 'form_log'
        appendFile(file_name, file_path, log_str)

        '''close contact popup window'''
        closeBtnEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(closeBtnXpath))
        closeBtnEle.click()




def searchCompany(driver,url,page,skiplist):

    driver.get(url)
    """This waits up to 10 seconds before throwing a TimeoutException or
        if it finds the element will return it in 0 - 10 seconds. """
    contentListClassname = "gps-result-list"
    contentEle = WebDriverWait(driver,10).until(lambda driver: driver.find_elements_by_class_name)(contentListClassname)

    '''define locator'''

    contentListClassname = "gps-search-wrapper"
    contactClassname = "gps-contact-button"
    companyClassname = "gps-agency-name"
    '''the number of companies shown on the web page'''
    companyNum = 10*(page-1)
    '''the number of companies of each scrolling down'''
    loadNum = 10
    divNum = 6
    '''company list'''
    company = []
    n = 0


    '''protect'''
    time.sleep(5)


    '''if starting page is not page 1, we should scroll down to that page directly'''
    if page > 1 :
        for p in range(1,page):

            listEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_class_name)(
                contentListClassname)
            listS = listEle.size
            listH = listS.values()[1]
            driver.execute_script("window.scrollTo(0, %d)" %listH)

            num = 10*p+1


            try:
                pageXpath = "html/body/div[5]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[%d]" %num
                pageEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(pageXpath))
            except:
                pageXpath = "html/body/div[5]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[%d]" %num
                pageEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(pageXpath))

            n += 1
            print "page: ", p

            # except Exception as e:
            #     print 'error: ', e
            #     print 'stuck at loading page %d or path may be changed by Google!'%p

            # '''protect'''
            time.sleep(5)
            # driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);


    ''' if no more company, crawling ends'''
    while loadNum != 0:

        try:
            '''find contact btns'''
            ContactEle = WebDriverWait(driver,20).until(lambda driver: driver.find_elements_by_class_name)(
                contactClassname)

            companyEle = WebDriverWait(driver,10).until(lambda driver: driver.find_elements_by_class_name)(
                companyClassname)

            loadNum = len(ContactEle)-companyNum
            # print 'Contact: ', len(ContactEle)
            # print 'companyNum: ', companyNum


            '''number of companies which have been connected'''
            i = companyNum

            divNum = 7 + companyNum*2


            for item in ContactEle[companyNum:]:
                company = companyEle[i].text

                '''if company in the skiplist, pass it'''
                try:
                    for c in skiplist:
                        if company == c:
                            raise BreakIt

                    fillForm(driver,item,divNum,company,page)
                    time.sleep(120)
                    divNum += 2
                    i += 1
                except BreakIt:
                    skip_log = "Company: %s is skipped at page: %d"%(company,page)
                    print skip_log
                    file_name = 'form_log'
                    file_path = 'form_log'
                    appendFile(file_name, file_path, skip_log)
                    i += 1
                    divNum += 2
                    pass

            companyNum = len(ContactEle)

            print "=============================="
            print "Company Number: ", companyNum
            print "page: ", page


            '''if page does not be loaded automatically'''
            if i == companyNum:
                listEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_class_name)(
                contentListClassname)
                listS = listEle.size
                listH = listS.values()[1]
                driver.execute_script("window.scrollTo(0, %d)" %listH)

                '''confirm new page has been loaded'''
                try:
                    '''pageXpath may be changed'''
                    pageXpath = "html/body/div[5]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[" \
                                "%d]/div/section"%(companyNum+1)
                    pageEle = WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath(pageXpath))

                except:
                     pageXpath = "html/body/div[5]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[%d]/div/section" %(
                        companyNum+1)
                     pageEle = WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath(pageXpath))

                page += 1

                print "==========================="
                print "Loading page ", page
                '''protect'''
                time.sleep(5)


                # except Exception as e:
                #     print 'error: ', e
                #     print 'stuck at loading page %d or locator may be wrong!'%page


                '''new page would be dynamically loaded when the last company on that page is read.'''
            else:
                newContentXpath = "html/body/div[5]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[" \
                                "%d]/div/section"%(companyNum+1)
                page += 1
                try:
                    newContentEle = WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath)(
                        newContentXpath)

                    '''protect'''
                    time.sleep(5)

                except:

                    file_name = 'page_log'
                    file_path = 'log_file'
                    file_content = 'The program was interrupted at page %s' %page
                    print file_content, i,companyNum,loadNum
                    writeFile(file_name, file_path, file_content)

            #'''protect'''
            # time.sleep(20)

        except Exception as e:
	        print 'error: ', e

    driver.quit()



if __name__ == "__main__":
    driver = setUp()
    gmailSignin(driver)
    url = "https://www.google.com/partners/#a_search;bdgt=10000;inds=auto,bsmk,cspg,edgv,fnce,hlcr,ment,rtal,tech,trvl;lang=en;locn=United%20States;srvc=aaws,adog,aews,aomp,mava"
    openNewtab(driver)

    '''starting page'''
    page = 1

    '''companies have already been our customers'''
    customerList = ["PMG Worldwide"]

    '''read lists of company from 'Company info.txt' '''
    # visitedList = visited()

    '''list of companies wanted to be skipped'''
    # skipList = customerList + visitedList
    #
    # searchCompany(driver,url,page,skipList)




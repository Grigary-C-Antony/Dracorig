#This code is fully created by Grigary C Antony
#ask any doubt if. here 
#you need to install 2 things first using command prompt
#type "pip install selenium"
#then download chrome driver from the link provided in read.md
#then put both code and the chrome driver in same folder then run this code
#finally u can contact me her itself


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
username = input("Enter Username")
password = input("Enter Password")
driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("http://www.facebook.com")


def time_for_run():
    time_needed = input("Enter time in 24hr pattern ( work for today only ) : ")
    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(), datetime.time(time_needed, 0, 0))
    time.sleep((alarm_time - now).total_seconds())


def popup():
    try:
        time.sleep(15)
        driver.find_element_by_xpath('//*[@id="facebook"]/body').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
            time.sleep(5)
        except:
            try:
                driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                time.sleep(5)
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                    time.sleep(5)
                except:
                    try:
                        driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                        time.sleep(5)
                    except:
                        try:
                            driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                            time.sleep(5)
                        except:
                            try:
                                driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                                time.sleep(5)
                            except:
                                try:
                                    driver.find_element_by_xpath('//*[@id="facebook"]/body').click()  # popup
                                    time.sleep(5)
                                except:
                                    print("vittukala")


def credentials():
    k = driver.find_element_by_xpath("//*[@id='email']")
    k.click()
    k.send_keys(username)

    l = driver.find_element_by_xpath("//*[@id='pass']")
    l.click()
    l.send_keys(password)

    try:
        m = driver.find_element_by_xpath("//*[@id='u_0_4']")
        m.click()
    except:
        m = driver.find_element_by_xpath("//*[@id='u_0_b']")
        m.click()


def messenger():
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="u_0_a"]/div[2]/div[2]').click()  # messenger icon
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="MercuryJewelFooter"]/div/a[1]').click()  # meSSENGER
    time.sleep(10)
    popup()


def main():
    # time_for_run() # in devolopement stage try only for fun
    credentials()
    popup()
    messenger()


def message(your_message):
    try:
        j = driver.find_element_by_xpath('//*[@id="js_f"]/div/div/div')
        j.click()
        j.send_keys(your_message)
        j.send_keys(Keys.ENTER)
        time.sleep(10)
    except:
        j = driver.find_element_by_xpath('//*[@id="js_h"]/div/div/div')
        j.click()
        j.send_keys(your_message)
        j.send_keys(Keys.ENTER)
        time.sleep(10)


main()
message("hi")
message("how are you")
message("10")
message("done")
#type your message as given above
#uncommend below code to quit browser automatically


#time.sleep(10)
# driver.quit()

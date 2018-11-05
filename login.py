from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, subprocess

def main():

    # You most certainly want to change this
    url = "https://forecasterchallenge.accuweather.com/"
    usr = "email@email.com"
    pwd = "pa$$w0rd"

    # profile = webdriver.FirefoxProfile()
    # # Set a user agent string to help parse webserver logs easily
    # profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")
    browser = webdriver.Firefox()
    browser.get(url)
    time.sleep(1)

    # The element names will likely be different for your application,
    # therefore change accordingly
    browser.find_element_by_id("btn-login").click()
    user = browser.find_element_by_name("email")
    password = browser.find_element_by_name("password")
    # Clear the input fields
    user.clear()
    password.clear()
    user.send_keys(usr)
    password.send_keys(pwd)
    time.sleep(1)
    browser.find_element_by_id("cwLoginSubmit").click()
    time.sleep(5)
    # browser.find_element_by_id("claim-now").click()
    # browser.find_element_by_partial_link_text("Claim").click()

    # Keep the page loaded for 8 seconds
    time.sleep(8)

    # # Log out
    # # The element IDs will likely be different for your application,
    # # therefore change accordingly
    # browser.find_element_by_id("logout_link").click()
    # time.sleep(2)
    # browser.find_element_by_id("dialog_button_ok").click()
    # time.sleep(1)
    #
    # browser.delete_all_cookies()
    # browser.close()

if __name__ == '__main__':
    main()

import webbrowser
import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
import datetime

def config_serv():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("username", "password")
    return server

def browser_connect():
    options = Options()
    options.headless = False
    browser_profile = webdriver.FirefoxProfile()
    browser_profile.set_preference("browser.download.panel.shown", False)
    browser_profile.set_preference("browser.helperApps.neverAsk.openFile", "application/x-ica")
    browser_profile.set_preference("dom.webnotifications.enabled", False)
    browser = webdriver.Firefox(options=options, executable_path = '/usr/local/bin/geckodriver', firefox_profile=browser_profile)
    browser.get('http://username:password@192.168.0.1/RST_status.htm')
    return browser

def reboot():
    wait = ui.WebDriverWait(browser, 20)
    reboot = wait.until(lambda browser: browser.find_element_by_class_name('reboot'))
    reboot.click()
    alert_obj = browser.switch_to.alert
    if alert_obj:
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        msg = "\nAccess point was rebooted at",st
        return msg
    else:
        msg = ("\nFailure to reboot access point")
        return msg

def finalize():
    server.sendmail("from-address", "to-address", " ".join(msg))
    alert_obj = browser.switch_to.alert
    alert_obj.accept()
    browser.quit()

server = config_serv()
browser = browser_connect()
msg = reboot()
finalize()

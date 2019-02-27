import time
from selenium import webdriver
from win10toast import ToastNotifier

winnotifier = ToastNotifier()
#datetime.datetime.strptime(date_string, format1).strftime(format2)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")


browser = webdriver.Chrome(options=chrome_options)

#try:
browser.get("http://192.168.1.1/login.htm")

try:
    username = browser.find_element_by_name("username")
    password = browser.find_element_by_name("userpass")

    username.send_keys("admin")
    password.send_keys("admin")

    #browser.find_element_by_xpath('//input[contains(@onclick,"return saveChanges()")]').click()
    browser.find_element_by_css_selector("input[onclick*='return saveChanges()']").click()

    browser.get("http://192.168.1.1/reboot.htm")
    time.sleep(1)
    browser.find_element_by_css_selector("input[onclick*='return rebootClick()']").click()
    #browser.find_element_by_id("restartNow").click()
    time.sleep(1)
    alert_obj = browser.switch_to.alert
    alert_obj.accept()
    winnotifier.show_toast("sharmaji: Wifi rebooted",\
     "TOTOLINK succesfully has been rebooted wait for 10-15 secs", duration=5)
    time.sleep(3)
    browser.close()

except:
    browser.get("http://192.168.1.1/reboot.htm")
    time.sleep(1)
    browser.find_element_by_css_selector("input[onclick*='return rebootClick()']").click()
    alert_obj = browser.switch_to.alert
    time.sleep(1)
    alert_obj.accept()
    winnotifier.show_toast("sharmaji: Wifi rebooted",\
     "TOTOLINK succesfully has been rebooted wait for 10-15 secs", duration=5)
    time.sleep(3)
    browser.close()

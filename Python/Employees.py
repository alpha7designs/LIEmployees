from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import clicksend_client
from clicksend_client.rest import ApiException
from clicksend_client import SmsMessage

from server import *
import time
import sys
import os


# -------------------------------------------------------------
phones   = ['+13057938514', '+14255189233']
srcPhone = '+114707770111'
smsUser  = 'dave@1hop.xyz'
smsPass  = 'BE6FEFA3-76C3-C27E-4565-718F07149A70'
# -------------------------------------------------------------


# Global Variables

driver = None
conn   = None
cursor = None

conn   = getConn()
cursor = getCursor(conn)

# -------------------------------------------------------------
# -------------------------------------------------------------
def safeXPATH(source, xpath):
    try:
        return source.find_element_by_xpath(xpath)
    except:
        return None
# -------------------------------------------------------------
# -------------------------------------------------------------
def safeXPATHs(source, xpath):
    try:
        return source.find_elements_by_xpath(xpath)
    except:
        return None
# -------------------------------------------------------------
# -------------------------------------------------------------
def waitWeb(b):
    while True:
        if b.execute_script("return (document.readyState)") == 'complete':
            break
        print ('Waiting...')
        time.sleep(0.5)
# -------------------------------------------------------------
# -------------------------------------------------------------

def login(email, password):

    try:
        global driver

        options = Options()

        options=webdriver.ChromeOptions()
        audio_path = 'c:\\temp\\audio01.wav'

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--force-wave-audio")
        options.add_argument("--reduce-security-for-testing")
        options.add_argument('--allow-file-access-from-files')
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--use-file-for-fake-audio-capture=‪{}".format(audio_path))
        # options.add_argument('--blink-settings=imagesEnabled=false')  
        # options.add_argument("headless")
        # options.add_argument("user-data-dir=selenium")

        try:
            driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        except Exception:
            print("Kindly replace the Chrome Web Driver with the latest one from "
                  "http://chromedriver.chromium.org/downloads "
                  "and also make sure you have the latest Chrome Browser version."
                  "\nYour OS: {}".format(platform_)
                  )
            exit()

        driver.get("https://www.linkedin.comhttps://www.linkedin.com")
        driver.delete_all_cookies()

        liPath = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
        driver.get(liPath)
        driver.maximize_window()

        logins = driver.find_elements_by_name('session_key')
        if len(logins) > 0:
            logins[0].send_keys(email)
            time.sleep(1)
            driver.find_element_by_name('session_password').send_keys(password)
            time.sleep(1)
            for butt in safeXPATHs(driver, "//button"):
                if butt.text == 'Sign in':
                    butt.click()
                    time.sleep(1)
                    break
        return
    except:
        print('some error')

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

login('dave@1hop.xyz', 'blahblah99')

while True:

    s   =  "select DATEDIFF(MINUTE, LastChecked, getdate()) Diff, LastChecked from JodyConfig(nolock)"
    chk = SQLGet(s, cursor)
    if chk[0]['Diff'] < 60:
        mins = 60 - chk[0]['Diff']
        tim  = mins * 60
        print(f"Sleeping for {mins} mins.  Last checked at {chk[0]['LastChecked']}")
        time.sleep(tim)

    msg  = ""
    s    = "select * from JodyEmployees(nolock) order by URL"
    urls = SQLGet(s, cursor)
    for url in urls:
        driver.get(url['URL'])
        time.sleep(2)

        num = safeXPATH(driver, "//a[@data-control-name='topcard_see_all_employees']")
        num = num.text.lower()
        x = num.find('see all')
        if x > -1:
            num = num[x+8:]
        x = num.find('employees')
        if x > -1:
            num = num[:x].strip().replace(",", "")

        if num.isdigit():
            if int(num) != url['LastNum']:
                if url['LastNum'] > 0:
                    msg += f"{url['Company']}: Old:{url['LastNum']}, Current:{num}\n"
                s = f"update JodyEmployees set LastNum = {num} where intID = {url['intID']}"
                SQLExec(s, cursor, conn)


    if msg != "":
        configuration = clicksend_client.Configuration()
        configuration.username = smsUser
        configuration.password = smsPass

        api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
        toSend       = []
        for phone in phones:

            toSend.append (SmsMessage(source = "python",
                                    _from  = srcPhone,
                                    body   = msg,
                                    to     = phone))
        sms_messages = clicksend_client.SmsMessageCollection(messages=toSend)

        try:
            api_response = api_instance.sms_send_post(sms_messages)
            print(api_response)
        except ApiException as e:
            print("Exception when calling SMSApi->sms_send_post: %s\n" % e)

    s = "update JodyConfig set LastChecked = getdate()"
    SQLExec(s, cursor, conn)

driver.close()
conn.close()
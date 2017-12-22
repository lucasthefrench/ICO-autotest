# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re, urllib, sys
import HtmlTestRunner
import argparse

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
# Argument Parser for command line option generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
parser = argparse.ArgumentParser()

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
# Here you can create parameter option as much as you want
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
parser.add_argument('-myBrowser','--myBrowser',help='Browser name for test',action='store',)
parser.add_argument('-myFQDN','--myFQDN',help='Test target ICO portal URL',action='store',)
parser.add_argument('-myEMAIL_ADDRESS','--myEMAIL_ADDRESS',help='Test PassAXA - Email address',action='store',)
parser.add_argument('-myEMAIL_PASSWORD','--myEMAIL_PASSWORD',help='Test PassAXA - Password',action='store',)
parser.add_argument('-myDomain','--myDomain',help='Test ICO portal specific domain',action='store',)

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
# Now set variable to take all command line option value
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
args = parser.parse_args()


class FirstTest(unittest.TestCase):
    @classmethod    
    def setUp(self):

        #global driver
        #global myBrowser
        #global myFQDN
        #global myEMAIL_ADDRESS
        #global myEMAIL_PASSWORD
        #global myDomain
        myBrowser = args.myBrowser
        myFQDN = args.myFQDN
        myEMAIL_ADDRESS = args.myEMAIL_ADDRESS
        myEMAIL_PASSWORD = args.myEMAIL_PASSWORD
        myDomain = args.myDomain

        if myBrowser == "firefox": 
            self.driver = webdriver.Firefox("C:\\Users\\Administrator\\Documents\\webdrivers\\geckodriver.exe")
        elif myBrowser == "chrome":	
            chrome_options = Options()
            chrome_options.add_argument("--user-data-dir --disable-web-security --allow-running-insecure-content")
            self.driver = webdriver.Chrome("C:\\Users\\Administrator\\Documents\\webdrivers\\chromedriver.exe", chrome_options=chrome_options)
        elif myBrowser == "ie":
            self.driver = webdriver.Ie("C:\\Users\\Administrator\\Documents\\webdrivers\\IEDriverServer.exe")
        else:
            print ("ERROR, choosen browser is "+args.myBrowser+". This browser is unknown or not supported. Please try with 'firefox', 'chrome' or 'ie'")
	
        self.base_url = myFQDN
        self.verificationErrors = []
        self.accept_next_alert = True
        return self.driver
    @classmethod

    def tearDown(self):
        # close the browser window
        self.driver.quit()
		
    def test_001_login_p_r_o_d(self):
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # |||||||||||||||---VARIABLES TO BE DEFINED BY USER---||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        screenshot_path = "c:\\Users\\Administrator\\Documents\\python_scripts\\Demo_automation_tests"
        date = "22122017"
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # |||||||||||||||---LOG IN TO THE PORTAL---|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        self.driver.get(args.myFQDN)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(args.myEMAIL_ADDRESS)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(args.myEMAIL_PASSWORD)
        self.driver.find_element_by_id("domain").clear()
        self.driver.find_element_by_id("domain").send_keys(args.myDomain)
        self.driver.find_element_by_css_selector("button.login-button").click()
        time.sleep(30)
        self.driver.find_element_by_id("self-service_")
        FILE_PATH = screenshot_path + '\\dashboard_evidence_'+args.myDomain+'.png'
        self.driver.save_screenshot(FILE_PATH)
if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]],testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\Users\\Administrator\\Documents\\python_scripts\\Demo_automation_tests'))

# Example call
# python login_PROD.py -myBrowser chrome -myFQDN https://cloudportal.corp.intraxa/ -myEMAIL_ADDRESS nobuaki.ogawa@axa-tech.com -myEMAIL_PASSWORD XXXXXXXX -myDomain AXA
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
import unittest, time, re, urllib, sys, datetime
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
parser.add_argument('-mySubDescription','--mySubDescription',help='Test ICO portal subscripiton description',action='store',)
parser.add_argument('-myAtsDataCenter','--myAtsDataCenter',help='Test ICO portal select ATS data center',action='store',)
parser.add_argument('-myOpcoName','--myOpcoName',help='Test ICO portal Opco to select',action='store',)
parser.add_argument('-myCurrency','--myCurrency',help='Test ICO portal currency for sub creation',action='store',)
parser.add_argument('-myBudgetEnvelope','--myBudgetEnvelope',help='Test ICO portal budget envelope',action='store',)
parser.add_argument('-myBudgetCode','--myBudgetCode',help='Test ICO portal budget code',action='store',)
parser.add_argument('-myBudgetName','--myBudgetName',help='Test ICO portal budget name',action='store',)
parser.add_argument('-myTargetEnv','--myTargetEnv',help='Test ICO portal target environment',action='store',)
parser.add_argument('-mySubOwner','--mySubOwner',help='Test ICO portal subscripiton owner',action='store',)
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
# Now set variable to take all command line option value
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
args = parser.parse_args()


class CreateSubscription(unittest.TestCase):
    @classmethod    
    def setUp(self):

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
            print ("ERROR, chosen browser is "+args.myBrowser+". This browser is unknown or not supported. Please try with 'firefox', 'chrome' or 'ie'")
	
        self.base_url = myFQDN
        self.verificationErrors = []
        self.accept_next_alert = True
        return self.driver
    @classmethod

    def tearDown(self):
        # close the browser window
        screenshot_path = "c:\\Users\\Administrator\\Documents\\python_scripts\\Demo_automation_tests\\test_results"
        now = datetime.datetime.now()
        today = now.strftime("%B-%d-%Y_%I-%M%p")
        if not self.driver.find_element_by_css_selector("span.text").text:
            self.driver.save_screenshot(screenshot_path+'\\FAILURE_EVIDENCE_CREATESUBSCRIPTION_'+today+'.png')
        self.driver.quit()

    def test_CREATE_SUBSCRIPTION(self):
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        now = datetime.datetime.now()
        today = now.strftime("%B-%d-%Y_%I-%M%p")
        wait = WebDriverWait(self.driver, 70)
		# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # |||||||||||||||---LOG IN TO THE PORTAL---|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        self.driver.get(args.myFQDN)
        self.driver.maximize_window()
        time.sleep(0.5)
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(args.myEMAIL_ADDRESS)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(args.myEMAIL_PASSWORD)
        self.driver.find_element_by_id("domain").clear()
        self.driver.find_element_by_id("domain").send_keys(args.myDomain)
        self.driver.find_element_by_css_selector("button.login-button").click()
        element = wait.until(EC.element_to_be_clickable((By.ID, 'self-service')))

        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # |||||||||||||||---SELECT THE RIGHT PROJECT---|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        self.driver.find_element_by_id('projectSelect').click()
        select = Select(self.driver.find_element_by_id('projectSelect'))
        select.select_by_value("SubscriptionAdministration")
        time.sleep(20)

        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # |||||||||||||||---CREATE NEW SUBSCRIPTION---|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        screenshot_path = "c:\\Users\\Administrator\\Documents\\python_scripts\\Demo_automation_tests\\test_results"
        # ---------verifying if right project is selected----------------------------------------------------------------------------------------------------------------------------------------------
        try: self.assertEqual("SubscriptionAdministration", self.driver.find_element_by_xpath("//span[@id='projectSelectDefault']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ---------go to the right offering-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("self-service").click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.content')))
        #time.sleep(5)
        self.driver.find_element_by_css_selector("div.content").click()
        self.driver.find_element_by_xpath("//a[2]/div/div").click()
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'coach-iframe')))
        #time.sleep(30)
        # ---------Subscription Description--------------------------------------------------------------------------------------------------------------------------
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("coach-iframe")) 
        self.driver.find_element_by_id("dijit_form_Textarea_0").send_keys(args.mySubDescription)
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | css=div.breadcrumbcontents | ]]
        # ---------ats data center-------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("dijit_form_FilteringSelect_0").send_keys(args.myAtsDataCenter)
        time.sleep(3)
        self.driver.find_element_by_id("dijit_form_FilteringSelect_0_popup0").click()
        time.sleep(5)
        # ---------opco legal entity name----------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("dijit_form_FilteringSelect_1").send_keys(args.myOpcoName)
        time.sleep(3)
        self.driver.find_element_by_id('dijit_form_FilteringSelect_1_popup0').click()
        time.sleep(3)
        # ---------currency-------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("dijit_form_FilteringSelect_2").send_keys(args.myCurrency)
        time.sleep(3)
        self.driver.find_element_by_id('dijit_form_FilteringSelect_2_popup0').click()
        time.sleep(3)
        # ---------budget envelope------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=uniqName_1_0 | ]]
        self.driver.find_element_by_id("uniqName_1_0").send_keys(args.myBudgetEnvelope)
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | css=div.breadcrumbcontents | ]]
        # ---------budget code-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=dijit_form_ComboBox_0 | ]]
        self.driver.find_element_by_id("dijit_form_ComboBox_0").send_keys(args.myBudgetCode)
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | css=div.breadcrumbcontents | ]]
        # ---------budget name------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=dijit_form_ComboBox_1 | ]]
        self.driver.find_element_by_id("dijit_form_ComboBox_1").send_keys(args.myBudgetName)
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | css=div.breadcrumbcontents | ]]
        # ---------target environment-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("dijit_form_FilteringSelect_3").send_keys(args.myTargetEnv)
        time.sleep(3)
        self.driver.find_element_by_id('dijit_form_FilteringSelect_3_popup0').click()
        time.sleep(3)
        # ---------subscription owner--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_id("dijit_form_FilteringSelect_4").send_keys(args.mySubOwner)
        time.sleep(3)
        self.driver.find_element_by_id('dijit_form_FilteringSelect_4_popup0').click()
        time.sleep(3)
        # ---------go next------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_css_selector("button.BPMButton.BPMButtonBorder").click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.text')))        
		#time.sleep(10)
        # ---------store subscription name------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        subscription_name = self.driver.find_element_by_css_selector("span.text").text
        time.sleep(3)
        FILE_PATH = screenshot_path + '\\summary_evidence_'+project_name+'_'+today+'.png'
        self.driver.save_screenshot(FILE_PATH)
        time.sleep(3)
        # ---------submit----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.driver.find_element_by_css_selector("#div_4_1_2 > button.BPMButton.BPMButtonBorder").click()        
        time.sleep(3)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]],testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\Users\\Administrator\\Documents\\python_scripts\\Demo_automation_tests\\test_results'))
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys
sys.path.append(".")

class BasePage(object):
    
    def __init__(self, drv):
        self.drv = drv
    
    def wd_click_simple(self, locator):
        self.drv.find_element("xpath",locator).click()
    
    def wd_implicitly_wait(self, time):
        self.drv.implicitly_wait(time) 

    def get_element(self, locator):    
        webel = self.drv.find_element("xpath",locator)
        return webel
    
    def wait_until_element_clickable(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))   
        return webel
    
    def wait_until_visibility_of_element_located(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel    
    def wait_until_visibility_of_element_located_name(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.NAME, locator)))   
        return webel 
    def wd_Send_keys (self, locator, text):
        
        self.drv.find_element("xpath", locator).clear()
        self.drv.find_element("xpath", locator).send_keys(text)

    def selector_index(self,webel,num):
        sel = Select(webel)
        sel.select_by_index(num)


    def wd_Send_keys_css (self, locator, text):
        self.drv.find_element(By.CSS_SELECTOR, locator).clear()
        self.drv.find_element(By.CSS_SELECTOR, locator).send_keys(text) 
        
    def wd_Send_keys_siimple (self, locator, text):
        self.drv.find_element("xpath", locator).send_keys(text) 
    
    def wd_Send_keys_Name (self, locator, text):
        self.drv.find_element(By.NAME, locator).clear()
        self.drv.find_element(By.NAME, locator).send_keys(text)    
    
    def wd_Send_keys_Name_simple (self, locator, text):
        self.drv.find_element(By.NAME, locator).send_keys(text)

      
    
    def wait_until_visibility_of_element_located_parameter(self, waitTime, search):
        locator = "//*div[contains(text(),{search})]".format(search)
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel        
    def wait_until_visibility_of_element_located_parameter(self, waitTime, container, search):
        locator = "//*div[contains({container},{search})]".format(container, search)
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel        
    
    def handle_webelement_exception(self, waitTime, locator,message ):   
        wait = WebDriverWait(self.drv, waitTime)
        try: 
            webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except  NoSuchElementException:  
            print(message)
    def wait_untill_visibility_CSS(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))   
        return webel 
    def wait_untill_clickable_CSS(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))   
        return webel    
    
    def wd_click_simple_CSS(self, locator):
        self.drv.find_element_by_css_selector(locator).click()   
    
    def wd_click_simple_id(self, locator):
        self.drv.find_element_by_id(locator).click()
        
    def findElementsimpleX(self, locator):
        webel =  self.drv.find_element(By.XPATH,locator)
        return webel
    
    def findElements(self, locator):
        webel =  self.drv.find_elements(By.XPATH,locator)
        return webel
    
    def Send_keys_inner_element(self, text, locator):
        webel = self.drv.find_element("xpath",locator)
        print(webel.text)
        webel.click()
        inner = webel.find_element_by_tag_name("input")
        time.sleep(2)
        inner.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + text)
        
    def Send_keys_inner_element_span(self, locator, text):
        wait = WebDriverWait(self.drv, 10)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        webel.click()
        inner = webel.find_element_by_tag_name("div")
        time.sleep(2)
        inner.send_keys(text)
    
    def Send_keys_inner_element_clear(self, locator):
        webel = self.drv.find_element("xpath",locator)
        print(webel.text)
        webel.click()
        inner = webel.find_element_by_tag_name("textarea")
        inner.clear()
        
    def actions_click(self,locator):
        wait = WebDriverWait(self.drv, 10)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))  
        action = ActionChains(self.drv)
        action.move_to_element(webel).send_keys(Keys.RETURN).perform()    

    def actions_Sendkeys_click(self,text,save,key):
        wait = WebDriverWait(self.drv, 10)
        text_web = wait.until(EC.visibility_of_element_located((By.XPATH, text)))  
        save_web = wait.until(EC.visibility_of_element_located((By.XPATH, save)))  
        action = ActionChains(self.drv)
        action.move_to_element(text_web).send_keys(key)
        action.move_to_element(save_web).click().perform()    

   
    def javasscript_sendkeys (self, webel):
        self.drv.execute_script("return document.getElementsByClassName('view-lines monaco-mouse-cursor-text').value='test'")

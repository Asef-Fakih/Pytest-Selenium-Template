from textwrap import wrap
import pytest
import sys
from selenium import webdriver
sys.path.append(".")
from PyTest.pages.wrapper import BasePage
from PyTest.resources.Locator import Commonlocators as cl
from PyTest.resources.Constants import Constantinope as cndemo
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os

@pytest.fixture
def setup():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = options)
    driver.get(cndemo.URLnew)
    Wrap = BasePage(driver)
    Wrap.wait_until_visibility_of_element_located(10, cl.Title)
    Wrap.wait_until_element_clickable(10, cl.Username)
    Wrap.wd_Send_keys_siimple(cl.Username, cndemo.username)
    Wrap.wd_Send_keys_siimple(cl.Password, cndemo.password)
    Wrap.wait_until_element_clickable(10, cl.Login)
    Wrap.wd_click_simple(cl.Login)
    Wrap.wait_until_visibility_of_element_located(10, cl.Products)
    driver.fullscreen_window()  
    return driver
@pytest.fixture
def setup_chrome():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get(cndemo.URLnew)
    Wrap = BasePage(driver)
    Wrap.wait_until_visibility_of_element_located(10, cl.Title)
    Wrap.wait_until_element_clickable(10, cl.Username)
    Wrap.wd_Send_keys_siimple(cl.Username, cndemo.username)
    Wrap.wd_Send_keys_siimple(cl.Password, cndemo.password)
    Wrap.wait_until_element_clickable(10, cl.Login)
    Wrap.wd_click_simple(cl.Login)
    Wrap.wait_until_visibility_of_element_located(10, cl.Products)
    driver.fullscreen_window()  
    return driver

@pytest.fixture
def teardown():  
    driver.close()
    driver.quit()  
    return teardown


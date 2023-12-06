from textwrap import wrap
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import string
import random
sys.path.append(".")
from PyTest.pages.wrapper import BasePage
from PyTest.resources.Locator import Commonlocators as cl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException , TimeoutException

class Cart(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)


    def Add_to_Cart(self):
        wrap = self.Wrap
        backpack = cl.Add_Backpack
        cart = cl.Cart
        incart = cl.Backpack_incart
        wrap.wait_until_element_clickable(10, backpack)
        wrap.wd_click_simple(backpack)
        wrap.wait_until_element_clickable(10, cart)
        wrap.wd_click_simple(cart)
        cart_webel = wrap.wait_until_element_clickable(10, incart)
        return cart_webel.text
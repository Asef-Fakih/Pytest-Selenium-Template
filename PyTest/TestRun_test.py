import sys
import time
sys.path.append(".")
from PyTest.pages.wrapper import BasePage
from PyTest.pages.Cart import Cart
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from PyTest.resources.Constants import Constantinope as cn
import random
import string
import pytest
import os



def test_set_driver(setup_chrome):
    global drv
    drv = setup_chrome

def test_cart():
    cart = Cart(drv)
    backpack = cart.Add_to_Cart()

def test_teardown(teardown):
    pass


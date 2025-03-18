import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from selenium.webdriver.common.by import By
from main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import random



class Test_TC2:
    def 
import pytest
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from magazine_main import TestMain
from magazine_post1 import TestPost1
from magazine_post2 import TestPost2
from magazine_search1 import Testsearch1
from magazine_search2 import TestSearch2

class magazine(TestMain):
    super(TestMain)

class magazine(TestPost1):
    super(TestPost1)

class magazine(TestPost2):
    super(TestPost2)

class magazine(Testsearch1):
    super(Testsearch1)

class magazine(TestSearch2):
    super(TestSearch2)
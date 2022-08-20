# Generated by Selenium IDE
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

class TestDanofitinprogress():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_danofitinprogress(self):
    self.driver.get("https://danofit-stand-stage.internal.dano.me/")
    time.sleep(2)
    self.driver.set_window_size(1000, 800)
    #time.sleep(2)
    #self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-gYqUNx-size-xlarge > .c-cHZnbS").click()
    #time.sleep(2)
    #self.driver.find_element(By.CSS_SELECTOR, ".c-XUuOx c-cPQuGY c-bPFrui c-bPFrui-jifBFW-size-medium c-bPFrui-ecHVAM-safeArea-false c-bPFrui-ddLexP-cv").click()
    #self.driver.find_element(By.CSS_SELECTOR, "radix-id-5983299983-1-trigger-/coach").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-gYqUNx-size-xlarge > .c-cHZnbS").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jifBFW-size-medium > .c-bPFrui").click()
    time.sleep(2)
    self.driver.close()
    time.sleep(2)
  

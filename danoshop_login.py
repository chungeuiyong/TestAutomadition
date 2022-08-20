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

class TestDanoshoplogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_danoshoplogin(self):
    self.driver.get("https://qa.danoshop.net/")
    self.driver.set_window_size(1000, 800)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".popup-modal-close").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#header-right > .c-idUfoM > svg").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bdHSrw-eHmeGy-color-coral").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "member_id").send_keys("onlydano_test45")
    time.sleep(2)
    self.driver.find_element(By.ID, "member_passwd").send_keys("qwe321")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".loginok").click()
    time.sleep(8)
  
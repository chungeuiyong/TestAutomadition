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

class TestDanofitdiagnosis():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
     return set(wh_now).difference(set(wh_then)).pop()
  
  def test_danofitdiagnosis(self):
    timeout = 500
    self.driver.get("https://danofit-stand-stage.internal.dano.me/danofit")
    timeout = 500
    time.sleep(2)
    self.driver.set_window_size(1000, 800)
    time.sleep(1)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-bVzJkd-cv > .c-cHZnbS").click()
    time.sleep(1)
    self.vars["win9561"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win9561"])
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-dfWiW-size-large:nth-child(1)").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jifBFW-size-medium").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "age").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "height").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "age").send_keys("12")
    time.sleep(1)
    self.driver.find_element(By.NAME, "height").send_keys("172")
    time.sleep(1)
    self.driver.find_element(By.NAME, "weight").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "weight").send_keys("22")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-fGHEql").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv:nth-child(1)").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-dfWiW-size-large:nth-child(1)").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-XUuOx:nth-child(1) > .c-cHZnbS > .c-XUuOx > .c-XUuOx").click()
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-dfWiW-size-large:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-dfWiW-size-large:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jfvrRO-cv").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".c-cPQuGY > svg").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".c-bPFrui-jifBFW-size-medium:nth-child(2) > .c-cHZnbS").click()
    #time.sleep(1)
    #self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.vars["root"])
    time.sleep(1)
    self.driver.close()
  

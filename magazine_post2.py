# Generated by Selenium IDE
from socket import timeout
import pytest_timeout
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

class TestPost2():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_post2(self):
    time.sleep(1)
    self.driver.get("https://magazine-stage.dev.seoul.kube.dano.me/")
    timeout = 300
    time.sleep(2)
    self.driver.execute_script("window.scrollTo(0,1300)")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".sxqwvxc:nth-child(1) > .sxsxxpi > div:nth-child(2) .sxw2o1q").click()
    time.sleep(2)
    self.driver.execute_script("window.scrollTo(0,6700)")
    time.sleep(2)
    #self.driver.find_element(By.CSS_SELECTOR, ".sxsjo8x:nth-child(1) > .sxw2o1q").click() # sxsjo8x:nth-child(1) .sxw2o1q
    #self.driver.find_element(classname = "sxrzthn").click()
    self.driver.find_element(By.XPATH, "//div[@id='__next']/div/div/div/div[6]/div/div/div/div/div[2]/div").click()
    time.sleep(2)
    self.driver.close()
  

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

class Test2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_2(self):
    self.driver.get("https://qa.danoshop.net/product?product_no=511")
    time.sleep(2)
    self.driver.set_window_size(1000, 800)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".css-1yb80zs").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "member_id").send_keys("onlydano_test45")
    time.sleep(2)
    self.driver.find_element(By.ID, "member_passwd").send_keys("qwe321")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".loginok").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".css-1qd07mv-StyledDropdown:nth-child(1)").click()
    time.sleep(2)
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".css-1qd07mv-StyledDropdown:nth-child(1)")
    time.sleep(2)
    dropdown.find_element(By.XPATH, "//option[. = '야채현미곤약밥&등심간장볶음 4,500원']").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".css-17zrffq-Button").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-17zrffq-Button")
    time.sleep(2)
    actions = ActionChains(self.driver)
    time.sleep(2)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-cancel").click()
    time.sleep(2)
    self.driver.get("https://qa.danoshop.net/mypage/coupon")
    time.sleep(2)
    #self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .css-15jrqqw").click()
    self.driver.find_element(By.ID, "coupon_code").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "coupon_code").send_keys("정의용")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".css-ac20-StyledButton").click()
    time.sleep(2)
    
  

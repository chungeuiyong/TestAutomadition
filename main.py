#-*- encoding: UTF-8 -*-
from distutils.util import execute
from importlib.abc import ExecutionLoader
import sys
from typing import overload
from PyQt5 import QtWidgets
from PyQt5 import QtCore 
#print(sys.executable)

import pytest
import time
import json
import os
import subprocess
#test1 = 'C:/Users/NotePC/OneDrive/바탕화면/자동화/automadition1/selenium/pytest'
#test1 = r'C:\\Users\\NotePC\\OneDrive\\바탕 화면\\자동화\\automadition1\\selenium\\Scripts'
#test1 = r'"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/py.test.exe test_main.py"'
#test1 = r'"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/"'
#os.system(test1)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton , QLabel , QLineEdit
from PyQt5.QtCore import QCoreApplication
from magazine_main import TestMain




class Automadition2(QWidget):
    def __init__(self):
       super().__init__()
       self.initUI()
    def initUI(self):
        btn = QPushButton('다노 매거진' , self)
        btn.resize(btn.sizeHint())
        btn.move(50 , 50)
        btn.click
        btn.clicked.connect(self.magazine_btn)

        btn = QPushButton('다노샵' , self)
        btn.resize(btn.sizeHint())
        btn.move(50 , 100)
        btn.click
        btn.clicked.connect(self.danoshop_btn)

        btn = QPushButton('다노핏' , self)
        btn.resize(btn.sizeHint())
        btn.move(150 , 50)
        btn.click
        btn.clicked.connect(self.danofit_btn)

        
        #testbox = QLineEdit('' , self)
        #testbox.resize(testbox.sizeHint())
        #testbox.move(50 , 250)
        
        self.setGeometry(500,500,500,500)
        self.setWindowTitle('다노 자동화')
        self.show()

    def magazine_btn(self):
       #global execution
       global magazine_execution
       global magazine_route
       #self = test1
       #test1 = '"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/py.test.exe"'
       magazine_execution = 'pytest ' 
       magazine_route = '"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/magazine.py"'
       os.system(magazine_execution + magazine_route)
       
        #subprocess.run([pytest], shell=True)
    

       # test3=r'"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/py.test.exe"'
        # arguments=('./test_main.py')
        # subprocess.call([test3, arguments])
    def danoshop_btn(self):
        #global execution
        global danoshop_execution
        global danoshop_route

        danoshop_execution = 'pytest '
        danoshop_route = '"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/danoshop_login.py"'
        os.system(danoshop_execution + danoshop_route)

    def danofit_btn(self):
        global danofit_execution
        global danofit_route

        danofit_execution = 'pytest '
        danofit_route = '"c:/Users/NotePC/OneDrive/바탕 화면/자동화/automadition1/selenium/danofit/danofit.py"'
        os.system(danofit_execution + danofit_route)

        

app = QApplication(sys.argv)
a = Automadition2()
sys.exit(app.exec_())



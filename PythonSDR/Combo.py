#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os
import time
import struct
import signal
import numpy as np

from PyQt5 import Qt
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QWidget

class Combo():
  def __init__(self,main,config,control,function,config_name,content = None):
    self.main = main
    self.config = config
    self.control = control
    self.function = function
    self.config_name = config_name
    self.index = 0
    self.inhibit = False
    self.set_content(content)
    self.control.currentIndexChanged.connect(self.set_value)
  
  def enable(self,value):
    self.control.setEnabled(value)
  
  def check_valid_range(self):
    if self.content != None:
      n = len(self.content)-1
      self.index = (self.index,n)[self.index > n]
      
  def set_content(self,content):
    self.inhibit = True
    self.control.clear()
    self.content = content
    if content != None:
      self.control.addItems(content)
      self.check_valid_range()
    self.inhibit = False
    self.process_index()
    
  def process_index(self,index = None):
    if index == None:
      self.index = self.config[self.config_name]
    else:
      self.config[self.config_name] = index
      self.index = index
    self.check_valid_range()
    self.inhibit = True
    self.control.setCurrentIndex(self.index)
    self.inhibit = False
  
  def get_index(self):
    return self.index
        
  def get_value(self,index = None):
    self.process_index(index)
    if self.content == None:
      v = 0
    else:
      v = self.content[self.index]
    try:
      v = int(v)
    except:
      None
    return v
    
  def set_value(self,index = None):
    if not self.inhibit:
      self.process_index(index)
      if self.content != None:
        if len(self.content) > 0:
          a = self.index
          b = self.content[self.index]
          self.function(a,b)
  
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys
import os
import time
import struct
import signal
import numpy as np
from threading import Thread

from PyQt5 import Qt
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QEvent
#from PyQt5.QtGui #import ContextMenu

class TextEntry(QWidget):
  def __init__(self,main,obj,function,config_name,minv,maxv,string_entry = False):
    QWidget.__init__(self)
    self.obj = obj
    self.obj.setAlignment(QtCore.Qt.AlignRight)
    self.main = main
    self.function = function
    self.config_name = config_name
    self.minv = int(minv)
    self.maxv = int(maxv)
    self.string_entry = string_entry
    self.new_entry_flag = False
    self.set_value()
    self.obj.installEventFilter(self)
    
  def eventFilter(self, source, evt):
    t = evt.type()
    if t == QEvent.Wheel:
      self.new_entry_flag = True
      self.mouse_scroll_event(evt)
      return True
    elif t == QEvent.KeyPress:
      self.new_entry_flag = True
      if evt.key() == QtCore.Qt.Key_Return:
        self.update_entry(evt)
        return True
    return False
    
  def mouse_scroll_event(self,evt):
    try:
      value = self.value
      if evt.angleDelta().y() > 0:
        value += 1
      else:
        value -= 1     
      self.set_value(value)
    except:
      None
  
  def process(self,value):
    if value == None:
      if self.new_entry_flag:
        value = self.convert_entry(self.obj.text())
      else:
        value = self.main.config[self.config_name]
    #print("value1: %s" % str(value))
    value = self.convert_entry(value)
    #print("value2: %s" % str(value))
    if isinstance(value,int):
      value = (value,self.minv)[value < self.minv]
      value = (value,self.maxv)[value > self.maxv]
    #print("test values: %s %s" % (str(self.minv),str(self.maxv)))
    #print("value3: %s" % str(value))
    self.value = value
    self.main.config[self.config_name] = self.value
    self.obj.setText(str(self.value))
    self.obj.setAlignment(QtCore.Qt.AlignRight)
    self.new_entry_flag = False
  
  def set_range(self,v):
    self.maxv = int(v)
    self.minv = int(-v)
        
  def set_value(self,value = None):
    self.process(value)
    self.function(self.value)
    
  def get_value(self,value = None):
    self.process(value)
    return self.value
      
  def convert_entry(self,value):
    if self.string_entry:
      value = str(value)
    else:
      # numeric only
      try:
        # allow entries such as "1e6"
        value = int(float(value))
      except:
        value = 0
    return value
    
  def update_entry(self,evt = None):
    value = self.convert_entry(self.obj.text())
    self.set_value(value)


   
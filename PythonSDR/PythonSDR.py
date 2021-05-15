#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os
import ast
import time
import struct
import signal
import numpy as np
import glob
from gnuradio import gr

from PyQt5 import Qt
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QMainWindow,QHeaderView, QMessageBox

import osmosdr

from PythonSDR_GUI import Ui_MainWindow
import Radio
import FFTDisp
import TextEntry
import Combo
import Waterfall

class PythonSDR(QMainWindow, Ui_MainWindow):
  def __init__(self,app):
    QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
      
    self.app = app
    self.setupUi(self)
    self.setWindowTitle("PythonSDR - GMC")
    self.imageLabel.setPixmap(QtGui.QPixmap("datos.jpg"))
    app.aboutToQuit.connect(self.app_quit)
    self.graphic_data = None
    self.config = self.get_default_config()
    self.full_rebuild_flag = True
    self.running = False
    self.enabled = False
    self.upconvert_state_control = None
    self.radio = Radio.Radio(self)
    self.meta_style_sheet = """
    QLabel[accessibleName=FreqDigit] {
      color:#00c000;
      font-size:24pt;
      background:black;
      padding:0;
    }
    QLabel[accessibleName=FreqDigitDark] {
      color:#003000;
      font-size:24pt;
      background:black;
      padding:0;
    }
    QLabel[accessibleName=FreqDigit]:hover {
      color:#00ff00;
      background:#404040;
    }
    QLabel[accessibleName=FreqDigitDark]:hover {
      color:#00ff00;
      background:#404040;
    }
    QWidget[objectName=digit_widget] {
      background:black;
    }
    /* this solves the mouse tooltip color problem */
    DisplayPlot {
      qproperty-zoomer_color: #c0e0ff;
    }
    QTextEdit {
      text-align:right;
    }
    """
    self.setStyleSheet(self.meta_style_sheet)
    self.run_stop_button.clicked.connect(self.run_stop_event)
    self.offset_freq_control = None
      
    self.MODE_AM = 0     ####Modo
    self.MODE_FM = 1
    self.MODE_WFM = 2
    self.MODE_USB = 3
    self.MODE_LSB = 4
    self.MODE_CW_USB = 5
    self.MODE_CW_LSB = 6
    
    self.BW_WIDE = 0      ##Ancho de banda de frecuencia intermedia
    self.BW_MEDIUM = 1
    self.BW_NARROW = 2
    
    self.bandwidth_control = Combo.Combo(self,self.config,self.bandwidth_combo,self.set_bandwidth,'bandwidth')
    
    self.sample_rate_control = Combo.Combo(self,self.config,self.sample_rate_combo,self.critical_change,'sample_rate')
    
    self.audio_rate_control = TextEntry.TextEntry(self,self.audio_rate_text,self.critical_change,'audio_rate',1e3,60e3)
    
    # pause number 1 waits for interface to be rendered
    # before modifying it
    QtCore.QTimer.singleShot(100, self.first_read_config)
              
  def first_read_config(self):
    self.assign_freq(self.config['freq'])
    self.update_radio_values()
    self.resize(1020,520)
    self.float_to_splitter(0.65,self.splitter_v)
    self.float_to_splitter(0.80,self.splitter_h)
    # pause number 2 allows interface to
    # be fully laid out before starting
    # radio configuration
    QtCore.QTimer.singleShot(100, self.run_stop)
    self.waterfall_widget = Waterfall.WaterfallWidget(self,self.config,self.waterfall_layout)
    self.fft_widget = FFTDisp.FFTDispWidget(self,self.config,self.fft_disp_layout)
    self.enabled = True
  
  def get_default_config(self):
    defaults = {
      'antenna' : 0,
      'sample_rate' : 2.4e6,
      'audio_rate' : 48000,
      'freq' : 106500000,
      'bandwidth' : 5,
      'dbscale_lo' : -140,
      'dbscale_hi' : 10,
      'hilbert_taps' : 128,
      'fft_zoom' : -1,
      'waterfall_bias' : 150,
      'disp_trace_color' : '#ffff00',
      'disp_text_color' : '#80c0ff',
      'disp_vline_color' : '#c00000',
    }
    return defaults
      
  def update_radio_values(self):
    self.bandwidth_control.set_value()
    #self.offset_state_control.get_value()
    #self.offset_freq_control.set_value()
    self.sample_rate_control.get_value()
    self.audio_rate_control.get_value()
  
  def splitter_to_float(self,splitter):
    # creates normalized splitter position {0 ... 1}
    a,b = splitter.sizes()
    return float(a)/(a+b)
    
  def float_to_splitter(self,v,splitter):
    # requires normalized splitter position {0 ... 1}
    a,b = splitter.sizes()
    t = a+b
    aa = int(t * v)
    bb = t-aa
    splitter.setSizes([aa,bb])
    
  def update_freq_event(self,x = None):
    self.update_freq()
  
  def update_freq(self,f = None):
    if self.enabled:
      self.radio.test_set_cw_offset()
      if f == None:
        f = self.config['freq']
        self.lcdFreq.display(f/1000)
      else:
        self.config['freq'] = f
      mf = self.config['freq']
      if self.radio.osmosdr_source != None:
        #print("assigned freq: %f = %d" % (mf,int(mf)))
        self.radio.osmosdr_source.set_center_freq(int(mf), 0)
      self.radio.update_freq_xlating_fir_filter()

  def assign_freq(self,f = None):
    if f == None:
      f = self.config['freq']
    self.lcdFreq.display(f/1000)
    self.update_freq(f)
        
  def update_default_freq(self):
    self.update_freq(self.config['freq'])
  
  def start_process(self,start = True):
    self.run_stop_button.setChecked(start)
    if start and self.radio.error == False:
      self.update_default_freq()
      self.radio.start()
    else:
      self.radio.stop()
      self.radio.wait()
      self.radio.disconnect_all()
               
  def run_stop_event(self):
      self.running = not self.running
      self.run_stop()
    
  def run_stop(self,x = None):
    self.run_stop_button.setChecked(self.running)
    if self.running:
      self.start_process(False)
      self.radio.cw_offset = 0
      if self.full_rebuild_flag:
        self.radio = Radio.Radio(self)
        self.full_rebuild_flag = False  
      self.update_freq()
      self.update_radio_values()
      self.radio.initialize_radio(self.config)
      self.start_process()
      self.run_stop_button.setText("Detener")
    else:
      self.radio.initialize_radio(self.config)
      self.start_process(False)
      self.run_stop_button.setText("Comenzar")
 
  def critical_change(self,value,name = None):
    if self.enabled:
      self.full_rebuild_flag = True
      self.run_stop()
  
  def message_dialog(self,title,message):
    mb = QMessageBox (QMessageBox.Warning,title,message,QMessageBox.Ok)
    mb.exec_()
       
  def draw_fft_disp(self):
    if self.graphic_data != None:
      #sya = self.config['dbscale_lo']
      #syb = self.config['dbscale_hi']
      # note Y axis reversal
      self.fft_widget.accept_data(self.graphic_data)
      self.graphic_data = None
      
  def set_bandwidth(self,value = None,string = None):
    if self.radio.osmosdr_source != None and string != None:
      bw = float(string)
      print("set bandwidth: %d" % bw)
      self.radio.osmosdr_source.set_bandwidth(bw, 0)
      
  def app_quit(self,x=0):
    self.running = False
    self.enabled = False
    self.start_process(False)
    Qt.QApplication.quit()   

if __name__ == "__main__":
    pd = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(pd)
    app = Qt.QApplication(sys.argv)
    window = PythonSDR(app)
    window.show()
    sys.exit(app.exec_())
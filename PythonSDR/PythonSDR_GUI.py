# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\GNURadio-3.7\bin\PythonSDR\PythonSDR_GUI_design.ui'
#
# Created: Fri Feb  1 11:48:52 2019
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 786)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_h = QtWidgets.QSplitter(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter_h.sizePolicy().hasHeightForWidth())
        self.splitter_h.setSizePolicy(sizePolicy)
        self.splitter_h.setToolTip("")
        self.splitter_h.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_h.setObjectName("splitter_h")
        self.splitter_v = QtWidgets.QSplitter(self.splitter_h)
        self.splitter_v.setToolTip("")
        self.splitter_v.setOrientation(QtCore.Qt.Vertical)
        self.splitter_v.setObjectName("splitter_v")
        self.fft_disp = QtWidgets.QWidget(self.splitter_v)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.fft_disp.sizePolicy().hasHeightForWidth())
        self.fft_disp.setSizePolicy(sizePolicy)
        self.fft_disp.setMinimumSize(QtCore.QSize(0, 64))
        self.fft_disp.setToolTip("")
        self.fft_disp.setObjectName("fft_disp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fft_disp)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.fft_disp_layout = QtWidgets.QHBoxLayout()
        self.fft_disp_layout.setContentsMargins(0, 0, 0, 0)
        self.fft_disp_layout.setObjectName("fft_disp_layout")
        self.gridLayout_6.addLayout(self.fft_disp_layout, 0, 0, 1, 1)
        self.waterfall_widget = QtWidgets.QWidget(self.splitter_v)
        self.waterfall_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.waterfall_widget.setObjectName("waterfall_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.waterfall_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.waterfall_layout = QtWidgets.QHBoxLayout()
        self.waterfall_layout.setObjectName("waterfall_layout")
        self.gridLayout_4.addLayout(self.waterfall_layout, 0, 0, 1, 1)
        self.controls_widget = QtWidgets.QWidget(self.splitter_h)
        self.controls_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.controls_widget.setObjectName("controls_widget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.controls_widget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.bandwidth_label = QtWidgets.QLabel(self.controls_widget)
        self.bandwidth_label.setObjectName("bandwidth_label")
        self.gridLayout_9.addWidget(self.bandwidth_label, 3, 0, 1, 1)
        self.bandwidth_combo = QtWidgets.QComboBox(self.controls_widget)
        self.bandwidth_combo.setObjectName("bandwidth_combo")
        self.gridLayout_9.addWidget(self.bandwidth_combo, 3, 1, 1, 1)
        self.sample_rate_combo = QtWidgets.QComboBox(self.controls_widget)
        self.sample_rate_combo.setObjectName("sample_rate_combo")
        self.gridLayout_9.addWidget(self.sample_rate_combo, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 6, 0, 1, 2)
        self.lcdFreq = QtWidgets.QLCDNumber(self.controls_widget)
        self.lcdFreq.setDigitCount(6)
        self.lcdFreq.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdFreq.setProperty("intValue", 0)
        self.lcdFreq.setObjectName("lcdFreq")
        self.gridLayout_9.addWidget(self.lcdFreq, 7, 0, 1, 2)
        self.audio_rate_text = QtWidgets.QLineEdit(self.controls_widget)
        self.audio_rate_text.setObjectName("audio_rate_text")
        self.gridLayout_9.addWidget(self.audio_rate_text, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.controls_widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 2, 0, 1, 1)
        self.run_stop_button = QtWidgets.QPushButton(self.controls_widget)
        self.run_stop_button.setCheckable(True)
        self.run_stop_button.setObjectName("run_stop_button")
        self.gridLayout_9.addWidget(self.run_stop_button, 8, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.controls_widget)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 1, 0, 1, 1)
        self.imageLabel = QtWidgets.QLabel(self.controls_widget)
        self.imageLabel.setText("")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout_9.addWidget(self.imageLabel, 5, 0, 1, 2)
        self.gridLayout_3.addWidget(self.splitter_h, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bandwidth_label.setText(_translate("MainWindow", "Ancho de Banda Hz"))
        self.sample_rate_combo.setToolTip(_translate("MainWindow", "The rate at which data samples are produced"))
        self.audio_rate_text.setToolTip(_translate("MainWindow", "The rate at which the audio stream is created"))
        self.label_17.setText(_translate("MainWindow", "Muestreo de Audio"))
        self.run_stop_button.setToolTip(_translate("MainWindow", "Comienza o detiene la reproducción"))
        self.run_stop_button.setText(_translate("MainWindow", "Comenzar"))
        self.label_15.setText(_translate("MainWindow", "Tasa de Muestreo"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eyetracker.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from tkinter.messagebox import NO
from turtle import shape
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from cv2 import aruco
import time
import sys
import torch
import numpy as np
import math
from sklearn.linear_model import LinearRegression
import pandas as pd
from datetime import date, datetime
import pytz

# Variables Globales
detect = False  # Iniciar detector de pupila
aruco_detect = False  # Iniciar detector de aruco
nro_aruco = 0  # ID aruco
pos_aruco_x = 0  # Posicion en X centro aruco
pos_aruco_y = 0  # Posicion en Y centro aruco
calibrationOn = False  # Comenzar calibracion
addData = False  # Anadir datos para cada punto de calibracion para el entranamiento
training_data = []  # lista de los datos para la calibracion
numData = 0  # contador para anadir datos
boundingBox_cX = 0  # centro en x de la bounding box
boundingBox_cY = 0  # centro en y de la bounding box
contourCenter_cX = 0  # centro en x del contorno
contourCenter_cY = 0  # centro en y del contorno
glintCenter_cX = 0  # centro en x del glint
glintCenter_cY = 0  # centro en y del glint
model = LinearRegression()  # modelo de regresion
gaze_predict = False  # Comenzar prediccion de mirada
x_, y_ = None, None
name = None
diametro = None
today = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 1016)
        MainWindow.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_1 = QtWidgets.QLabel(self.centralwidget)
        self.img_1.setGeometry(QtCore.QRect(30, 20, 640, 480))
        self.img_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.img_1.setObjectName("img_1")
        self.img_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_2.setGeometry(QtCore.QRect(30, 510, 640, 480))
        self.img_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.img_2.setObjectName("img_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 10, 321, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_2.setGeometry(QtCore.QRect(20, 100, 290, 48))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.camara_2_on = QtWidgets.QPushButton(self.splitter_2)
        self.camara_2_on.setObjectName("camara_2_on")
        self.camara_2_off = QtWidgets.QPushButton(self.splitter_2)
        self.camara_2_off.setObjectName("camara_2_off")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.fps_2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.fps_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.fps_2.setObjectName("fps_2")
        self.verticalLayout_2.addWidget(self.fps_2)
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(20, 40, 290, 48))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.camara_1_on = QtWidgets.QPushButton(self.splitter)
        self.camara_1_on.setObjectName("camara_1_on")
        self.camara_1_off = QtWidgets.QPushButton(self.splitter)
        self.camara_1_off.setObjectName("camara_1_off")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fps_1 = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.fps_1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.fps_1.setObjectName("fps_1")
        self.verticalLayout.addWidget(self.fps_1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(690, 170, 321, 211))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 70, 82, 58))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.detector_on = QtWidgets.QPushButton(self.layoutWidget2)
        self.detector_on.setObjectName("detector_on")
        self.verticalLayout_3.addWidget(self.detector_on)
        self.detector_off = QtWidgets.QPushButton(self.layoutWidget2)
        self.detector_off.setObjectName("detector_off")
        self.verticalLayout_3.addWidget(self.detector_off)
        self.segment = QtWidgets.QLabel(self.groupBox)
        self.segment.setGeometry(QtCore.QRect(100, 30, 211, 141))
        self.segment.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.segment.setObjectName("segment")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(40, 180, 231, 23))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_11 = QtWidgets.QLabel(self.splitter_3)
        self.label_11.setObjectName("label_11")
        self.pupil_diameter = QtWidgets.QLCDNumber(self.splitter_3)
        self.pupil_diameter.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pupil_diameter.setObjectName("pupil_diameter")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(690, 450, 321, 541))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 281, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 261, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aruco_on = QtWidgets.QPushButton(self.layoutWidget3)
        self.aruco_on.setObjectName("aruco_on")
        self.horizontalLayout.addWidget(self.aruco_on)
        self.aruco_off = QtWidgets.QPushButton(self.layoutWidget3)
        self.aruco_off.setObjectName("aruco_off")
        self.horizontalLayout.addWidget(self.aruco_off)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 100, 281, 221))
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(40, 30, 202, 140))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.aruco_next = QtWidgets.QPushButton(self.layoutWidget4)
        self.aruco_next.setObjectName("aruco_next")
        self.horizontalLayout_2.addWidget(self.aruco_next)
        self.aruco_rest = QtWidgets.QPushButton(self.layoutWidget4)
        self.aruco_rest.setObjectName("aruco_rest")
        self.horizontalLayout_2.addWidget(self.aruco_rest)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.aruco_x = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.aruco_x.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.aruco_x.setObjectName("aruco_x")
        self.horizontalLayout_4.addWidget(self.aruco_x)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.aruco_y = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.aruco_y.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.aruco_y.setObjectName("aruco_y")
        self.horizontalLayout_5.addWidget(self.aruco_y)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.aruco_number = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.aruco_number.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.aruco_number.setObjectName("aruco_number")
        self.horizontalLayout_6.addWidget(self.aruco_number)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 180, 231, 27))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.calibration_on = QtWidgets.QPushButton(self.layoutWidget5)
        self.calibration_on.setObjectName("calibration_on")
        self.horizontalLayout_9.addWidget(self.calibration_on)
        self.dataCollection = QtWidgets.QPushButton(self.layoutWidget5)
        self.dataCollection.setObjectName("dataCollection")
        self.horizontalLayout_9.addWidget(self.dataCollection)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 330, 281, 191))
        self.groupBox_6.setObjectName("groupBox_6")
        self.endCalib = QtWidgets.QPushButton(self.groupBox_6)
        self.endCalib.setGeometry(QtCore.QRect(70, 30, 141, 25))
        self.endCalib.setObjectName("endCalib")
        self.resultCalib = QtWidgets.QLabel(self.groupBox_6)
        self.resultCalib.setGeometry(QtCore.QRect(20, 60, 241, 41))
        self.resultCalib.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resultCalib.setText("")
        self.resultCalib.setObjectName("resultCalib")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget6.setGeometry(QtCore.QRect(50, 110, 191, 61))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gazePredict = QtWidgets.QPushButton(self.layoutWidget6)
        self.gazePredict.setObjectName("gazePredict")
        self.horizontalLayout_12.addWidget(self.gazePredict)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.predict_x = QtWidgets.QLCDNumber(self.layoutWidget6)
        self.predict_x.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.predict_x.setObjectName("predict_x")
        self.horizontalLayout_10.addWidget(self.predict_x)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.predict_y = QtWidgets.QLCDNumber(self.layoutWidget6)
        self.predict_y.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.predict_y.setObjectName("predict_y")
        self.horizontalLayout_11.addWidget(self.predict_y)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(690, 380, 321, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.widget = QtWidgets.QWidget(self.groupBox_7)
        self.widget.setGeometry(QtCore.QRect(10, 30, 296, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.user_name.setText("")
        self.user_name.setObjectName("user_name")
        self.horizontalLayout_13.addWidget(self.user_name)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_13.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # acciones de botones
        # Inicar camaras
        self.camara_1_on.clicked.connect(self.start_video)
        self.camara_1_off.clicked.connect(self.cancel)

        self.camara_2_on.clicked.connect(self.start_video2)
        self.camara_2_off.clicked.connect(self.cancel2)

        # Iniciar detector de pupila
        self.detector_on.clicked.connect(self.fdetector_on)
        self.detector_off.clicked.connect(self.fdetector_off)

        # Iniciar detector de marcadores aruco
        self.aruco_on.clicked.connect(self.faruco_on)
        self.aruco_off.clicked.connect(self.faruco_off)
        self.aruco_next.clicked.connect(self.next_aruco)
        self.aruco_rest.clicked.connect(self.restart_aruco)

        # Inicar Calibracion
        self.calibration_on.clicked.connect(self.calib_on)
        self.dataCollection.clicked.connect(self.appendCalibpoints)

        # Realizar la estimacion
        self.endCalib.clicked.connect(self.end_calculate)

        # aplicar el modelo para estimacion
        self.gazePredict.clicked.connect(self.gaze_est)

        # get name
        self.pushButton.clicked.connect(self.get_name)

    # Funciones para hacer funcionar el thread 1

    def start_video(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        global detect
        if detect:
            self.Work.Imageupd_gray.connect(self.Imageupd_slot_gray)

        self.Work.FPS.connect(self.get_FPS)
        self.Work.d_pupil.connect(self.get_dPupil)

    def Imageupd_slot(self, Image):
        self.img_1.setPixmap(QPixmap.fromImage(Image))

    def get_FPS(self, fps):
        self.fps_1.display(int(fps))

    def cancel(self):
        self.img_1.clear()
        self.Work.stop()

    def salir(self):
        sys.exit()

    # funcion para inciar detector
    def fdetector_on(self):
        global detect
        self.cancel()
        time.sleep(2)
        detect = True
        self.start_video()

    def fdetector_off(self):
        global detect
        self.cancel()
        time.sleep(2)
        detect = False
        self.start_video()

    # Funciones para hacer funcionar el thread 2

    def start_video2(self):
        self.Work2 = Work2()
        self.Work2.start()
        self.Work2.Imageupd.connect(self.Imageupd_slot2)
        self.Work2.FPS.connect(self.get_FPS2)
        self.Work2.aruco_number.connect(self.get_arucoNum)
        self.Work2.aruco_cx.connect(self.get_arucocX)
        self.Work2.aruco_cy.connect(self.get_arucocY)
        self.Work2.predict_x.connect(self.get_estimationX)
        self.Work2.predict_y.connect(self.get_estimationY)

    def Imageupd_slot2(self, Image):
        self.img_2.setPixmap(QPixmap.fromImage(Image))

    def get_FPS2(self, fps):
        self.fps_2.display(int(fps))

    def cancel2(self):
        self.img_2.clear()
        self.Work2.stop()

    def salir2(self):
        sys.exit()

# Detectar arucos
    def faruco_on(self):
        global aruco_detect
        self.cancel2()
        time.sleep(2)
        aruco_detect = True
        self.start_video2()

    def faruco_off(self):
        global aruco_detect
        self.cancel2()
        time.sleep(2)
        aruco_detect = False
        self.start_video2()

    def next_aruco(self):
        global nro_aruco
        nro_aruco += 1

    def restart_aruco(self):
        global nro_aruco
        nro_aruco = 0

    def get_arucoNum(self, arucoNum):
        self.aruco_number.display(int(arucoNum))

# Calibracion
    def get_arucocX(self, arucoCx):
        self.aruco_x.display(int(arucoCx))

    def get_arucocY(self, arucoCy):
        self.aruco_y.display(int(arucoCy))

    def calib_on(self):
        global calibrationOn
        calibrationOn = True
        print('Calibracion iniciada')

    def appendCalibpoints(self):
        global addData
        addData = True
        print('Anadiendo datos')

        # label3 segment

    def Imageupd_slot_gray(self, Image):
        self.segment.setPixmap(QPixmap.fromImage(Image))

# Gaze estimation
# Estimar modelo

    def variables(self, lst):
        df = pd.DataFrame(lst)

        df['dx'] = df[0] - df[2]
        df['dy'] = df[1] - df[3]
        df['dx_dy'] = df['dx']*df['dy']
        df['dxdx'] = df['dx']**2
        df['dydy'] = df['dy']**2
        df['dx_dy_2'] = df['dxdx']*df['dydy']
        df['x_aruco'] = df[4]
        df['y_aruco'] = df[5]
        new_df = df[['dx', 'dy', 'dx_dy', 'dxdx',
                     'dydy', 'dx_dy_2', 'x_aruco', 'y_aruco']]
        return new_df

    def end_calculate(self):
        global calibrationOn
        global training_data
        global model
        global nro_aruco

        print(len(training_data))
        df = self.variables(training_data)
        y_ = df[['x_aruco', 'y_aruco']].to_numpy()
        x_ = df[['dx', 'dy', 'dx_dy', 'dxdx', 'dydy', 'dx_dy_2']].to_numpy()

        model.fit(x_, y_)
        print(f"intercept: {model.intercept_}")
        print(f"coefficients: {model.coef_}")

        calibrationOn = False
        print('End Calibration')
        self.resultCalib.setText('Model Estimated')
        nro_aruco = 0

# Estimando el punto de mirada
    def gaze_est(self):
        global gaze_predict
        gaze_predict = True
        print('Estimando la mirada')

    def get_estimationX(self, x_):

        if gaze_predict:
            self.predict_x.display(int(x_))

    def get_estimationY(self, y_):

        if gaze_predict:
            self.predict_y.display(int(y_))

# nombre usuario
    def get_name(self):
        global name
        name = self.user_name.text()
        # self.user_name.setReadOnly(True)
        name = name + '.txt'
        self.user_name.setDisabled(True)
        self.pushButton.setDisabled(True)
        print(name)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_1.setText(_translate("MainWindow", "TextLabel"))
        self.img_2.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Coneccion Camaras"))
        self.label_2.setText(_translate("MainWindow", "Camara 2"))
        self.camara_2_on.setText(_translate("MainWindow", "On"))
        self.camara_2_off.setText(_translate("MainWindow", "Off"))
        self.label_4.setText(_translate("MainWindow", "FPS"))
        self.label.setText(_translate("MainWindow", "Camara 1"))
        self.camara_1_on.setText(_translate("MainWindow", "On"))
        self.camara_1_off.setText(_translate("MainWindow", "Off"))
        self.label_3.setText(_translate("MainWindow", "FPS"))
        self.groupBox.setTitle(_translate("MainWindow", "Detector"))
        self.detector_on.setText(_translate("MainWindow", "On"))
        self.detector_off.setText(_translate("MainWindow", "Off"))
        self.segment.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate(
            "MainWindow", "Diametro de la pupila"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Gaze estimation"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Aruco Markers"))
        self.aruco_on.setText(_translate("MainWindow", "On"))
        self.aruco_off.setText(_translate("MainWindow", "Off"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Calibration"))
        self.label_6.setText(_translate("MainWindow", "Aruco markers"))
        self.aruco_next.setText(_translate("MainWindow", "Next"))
        self.aruco_rest.setText(_translate("MainWindow", "Restart"))
        self.label_7.setText(_translate("MainWindow", "X:"))
        self.label_8.setText(_translate("MainWindow", "Y:"))
        self.label_5.setText(_translate("MainWindow", "Nro:"))
        self.calibration_on.setText(_translate("MainWindow", "Start"))
        self.dataCollection.setText(_translate("MainWindow", "Collect data"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Gaze estimation"))
        self.endCalib.setText(_translate("MainWindow", "End Calibration"))
        self.gazePredict.setText(_translate("MainWindow", "Predict"))
        self.label_9.setText(_translate("MainWindow", "X:"))
        self.label_10.setText(_translate("MainWindow", "Y:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Datos Usuario"))
        self.label_12.setText(_translate("MainWindow", "Nombre:"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

# diamtro pupila en pixeles
    def get_dPupil(self, dPupil):
        self.pupil_diameter.display(int(dPupil))
# threads


class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    Imageupd_gray = pyqtSignal(QImage)
    FPS = pyqtSignal(int)
    d_pupil = pyqtSignal(int)

    def run(self):
        self.hilo_corriendo = True
        global detect
        global glintCenter_cX, glintCenter_cY

        if detect:
            self.detector = PupilDetection(model_name='bestSmall2.pt')
        else:
            pass

        width = 640
        height = 480
        gstreamer = 'udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink'
        #gstreamer = 'udpsrc port=5000 buffer-size=90000 ! application/x-rtp, encoding-name=JPEG,payload=26,clock-rate=90000 ! rtpjpegdepay ! jpegparse ! queue ! jpegdec ! videoconvert ! appsink'
        #cap = cv2.VideoCapture(gstreamer, cv2.CAP_GSTREAMER)
        cap = cv2.VideoCapture(1)
        # codec = 0x47504A4D  # MJPG
        #cap.set(cv2.CAP_PROP_FPS, 30.0)
        #cap.set(cv2.CAP_PROP_FOURCC, codec)
        #cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        prev_frame_time = 0
        new_frame_time = 0
        mask = None
        while self.hilo_corriendo:
            ret, frame = cap.read()
            global today
            today = datetime.strftime(datetime.now(
                pytz.timezone('America/La_Paz')), '%Y-%m-%d,%H:%M:%S')
            # print(today)

            if not ret:
                break
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = self.adjust_gamma(frame, 1.5)
            frame = cv2.flip(frame, -1)
            glint_center = self.glint_detect(frame)

            if glint_center is not None:

                glintCenter_cX, glintCenter_cY = glint_center

            if detect:
                frame = cv2.resize(frame, (640, 640))
                results = self.detector.score_frame(frame)
                frame, mask = self.detector.plot_boxes(results, frame)
                frame = cv2.resize(frame, (640, 480))
                # print(mask.shape)
                #gray = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
                Image_gray = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
                convetir_QT_gray = QImage(
                    Image_gray.data, Image_gray.shape[1], Image_gray.shape[0], QImage.Format_RGB888)
                pic_gray = convetir_QT_gray.scaled(211, 141)
                self.Imageupd_gray.emit(pic_gray)

            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            fps = int(fps)
            prev_frame_time = new_frame_time
            # print(str(fps))
            convetir_QT = QImage(
                Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            pic = convetir_QT.scaled(640, 480, Qt.KeepAspectRatio)
            self.Imageupd.emit(pic)
            self.FPS.emit(fps)
            global diametro
            self.d_pupil.emit(diametro)

    def stop(self):
        self.hilo_corriendo = False
        self.quit()

    def adjust_gamma(self, frame, gamma):
        lut = np.empty((1, 256), np.uint8)
        for i in range(256):
            lut[0, i] = np.clip(pow(i/255.0, gamma) * 255.0, 0, 255)
        return cv2.LUT(frame, lut)

    def preprocess_glint(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 10)
        return blur

    def glint_detect(self, frame):
        blur = self.preprocess_glint(frame)
        kernel = np.ones((5, 5), np.uint8)
        #glint_bgr= cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
        ret4, th4 = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)
        th4 = cv2.morphologyEx(th4, cv2.MORPH_OPEN, kernel)
        contours_g, hierarchy_g = cv2.findContours(
            th4, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        centro = None
        center_g = None

        for cnt_g in contours_g:
            cnt_g = cv2.convexHull(cnt_g)
            area_g = cv2.contourArea(cnt_g)
            # print(area)
            if area_g > 10 and area_g < 3000:
                m_g = cv2.moments(cnt_g)
                if m_g['m00'] != 0:
                    center_g = [int(m_g['m10'] / m_g['m00']),
                                int(m_g['m01'] / m_g['m00'])]
                    #cv2.circle(frame, center_g, 3, (255, 0, 0), -1)
                else:
                    center_g = [0, 0]
            else:
                center_g = [0, 0]
        centro = center_g
        # print(center_g)
        #cv2.circle(frame, center_g, 3, (255, 0, 0), -1)

        # try:
        #     ellipse_g = cv2.fitEllipse(cnt_g)
        #     cv2.ellipse(frame, box=ellipse_g,
        #                 color=(255, 0, 0))
        # except:
        #     pass
        return centro


class Work2(QThread):
    Imageupd = pyqtSignal(QImage)
    FPS = pyqtSignal(int)
    aruco_number = pyqtSignal(int)
    aruco_cx = pyqtSignal(int)
    aruco_cy = pyqtSignal(int)
    predict_x = pyqtSignal(int)
    predict_y = pyqtSignal(int)

    def run(self):
        self.hilo_corriendo = True
        width = 640
        height = 480

        global aruco_detect
        global nro_aruco
        global pos_aruco_x, pos_aruco_y
        global calibrationOn
        global training_data
        global addData
        global numData
        global boundingBox_cX, boundingBox_cY
        global glintCenter_cX, glintCenter_cY
        global gaze_predict
        global model
        global x_, y_

        if aruco_detect:
            self.arucos = ArucoDetection()
            print('aruco detection activate')
        gstreamer = 'udpsrc port=5002 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink'
        #gstreamer = 'udpsrc port=5000 buffer-size=90000 ! application/x-rtp, encoding-name=JPEG,payload=26,clock-rate=90000 ! rtpjpegdepay ! jpegparse ! queue ! jpegdec ! videoconvert ! appsink'
        cap = cv2.VideoCapture(gstreamer, cv2.CAP_GSTREAMER)
        #cap = cv2.VideoCapture(2)
        # codec = 0x47504A4D  # MJPG
        #cap.set(cv2.CAP_PROP_FPS, 30.0)
        #cap.set(cv2.CAP_PROP_FOURCC, codec)
        #cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        prev_frame_time = 0
        new_frame_time = 0
        while self.hilo_corriendo:
            ret, frame = cap.read()
            if not ret:
                break

            if aruco_detect:
                #frame = self.adjust_gamma(frame, 1.5)
                gary = self.arucos.gray_frame(frame)
                corners, ids, rejected = self.arucos.detect_markers(gary)
                frame = self.arucos.drawing_markers(
                    corners, ids, frame, nro_aruco)
                self.aruco_cx.emit(pos_aruco_x)
                self.aruco_cy.emit(pos_aruco_y)
                if calibrationOn:
                    if addData:
                        training_data.append(
                            (boundingBox_cX, boundingBox_cY, glintCenter_cX, glintCenter_cY, pos_aruco_x, pos_aruco_y,
                             abs(boundingBox_cX-glintCenter_cX), abs(boundingBox_cY-glintCenter_cY), nro_aruco))
                        numData += 1
                        if numData == 60:
                            addData = False
                            numData = 0
                    # print(training_data)
            else:
                pass
            # frame = cv2.resize(frame, (640, 480))
            # print(frame.shape)

            if gaze_predict:
                polfeat = self.pol_feat(
                    boundingBox_cX - glintCenter_cX, boundingBox_cY - glintCenter_cY)
                polfeat = polfeat.reshape(1, -1)
                y_new = model.predict(polfeat)
                #print('x: ', int(y_new[0][0]), ' y: ', int(y_new[0][1]))
                x_ = int(y_new[0][0])
                y_ = int(y_new[0][1])
                # print('prediciendo')

                if x_ and y_ is not None:
                    self.predict_x.emit(x_)
                    self.predict_y.emit(y_)
                    cv2.circle(frame, (x_, y_), 12, (255, 0, 0), -1)
                    global name, diametro, today
                    self.write_data(today, x_, y_,
                                    pos_aruco_x, pos_aruco_y, diametro, name)

            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flip = cv2.flip(Image, -1)
            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            fps = int(fps)
            prev_frame_time = new_frame_time
            # print(str(fps))
            convetir_QT = QImage(
                flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
            pic = convetir_QT.scaled(640, 480, Qt.KeepAspectRatio)
            self.Imageupd.emit(pic)
            self.FPS.emit(fps)
            self.aruco_number.emit(nro_aruco)

    def stop(self):
        self.hilo_corriendo = False
        self.quit()

    def adjust_gamma(self, frame, gamma):
        lut = np.empty((1, 256), np.uint8)
        for i in range(256):
            lut[0, i] = np.clip(pow(i/255.0, gamma) * 255.0, 0, 255)
        return cv2.LUT(frame, lut)

    def pol_feat(self, x, y):
        return np.hstack((
            [x],
            [y],
            [x * y],
            [x**2],
            [y**2],
            [(x**2) * (y**2)]))

    def write_data(fecha, x, y, x_a, y_a, diametro, titulo='reporte.txt'):

        outfile = open(titulo, 'a')
        outfile.write(fecha+','+str(x)+','+str(y)+', ' +
                      str(x_a)+','+str(y_a)+','+str(diametro)+'\n')
        outfile.close

    # def write_data(self, x, y, x_a, y_a):

    #     outfile = open('report.txt', 'a')
    #     outfile.write(str(x)+','+str(y)+', '+str(x_a)+','+str(y_a)+'\n')
    #     outfile.close


class PupilDetection:

    # Load de model and verify if we are using the GPU

    def __init__(self, model_name):

        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)
        self.kernel = np.ones((5, 5), np.uint8)

    def load_model(self, model_name):

        if model_name:
            # model = torch.hub.load(
            #    'ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
            model = torch.hub.load(
                '/home/mirko/yolov5', 'custom', source='local', path=model_name, force_reload=True)

        else:
            print('no hay modelo')
            # model = torch.hub.load('ultralytics/yolov5',
            #                       'yolov5s', pretrained=True)
        return model

# Functions for preprocessing the frame

    def adjust_gamma(self, frame, gamma):
        lut = np.empty((1, 256), np.uint8)
        for i in range(256):
            lut[0, i] = np.clip(pow(i/255.0, gamma) * 255.0, 0, 255)
        return cv2.LUT(frame, lut)

# Functions to predict the bounding Box

    def score_frame(self, frame):

        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):

        return self.classes[int(x)]

    def plot_boxes(self, results, frame):

        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        # creating the frame to create the mask
        mask = np.zeros((y_shape, x_shape), dtype=np.uint8)
        extra = 15
        masking = None
        dilation2 = None
        edges = None
        global boundingBox_cX
        global boundingBox_cY
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.5:
                x1, y1, x2, y2 = int(
                    row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)

                mask[y1 - extra:y2 + extra, x1 - extra:x2 + extra] = 255
                masking = cv2.bitwise_and(frame, frame, mask=mask)
                #cv2.imshow("mask", masking)

                # finding the center of the bounding Box
                x_center = int((x2-x1)/2) + x1
                y_center = int((y2-y1)/2) + y1
                boundingBox_cX, boundingBox_cY = x_center, y_center
                # print(frame.shape)

                # Segmentacion

                blur = cv2.GaussianBlur(masking, (5, 5), 0)
                #gray22 = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
                inv_boxframe = cv2.bitwise_not(blur)
                gray_inv = cv2.cvtColor(inv_boxframe, cv2.COLOR_BGR2GRAY)
                _, thresh_gray = cv2.threshold(
                    gray_inv, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                #edges = limites
                #edges = cv2.Canny(gray_inv, 50, 30)
                # _, thresh_gray = cv2.threshold(
                #    gray_inv, 167, 255, cv2.THRESH_BINARY)
                dilation = cv2.dilate(thresh_gray, self.kernel, iterations=4)
                masking2 = cv2.bitwise_and(dilation, dilation, mask=mask)
                erosion = cv2.erode(masking2, self.kernel, iterations=6)
                dilation2 = cv2.dilate(erosion, self.kernel, iterations=5)

                # ElipseFit
                drawing = np.copy(dilation2)
                contours, hierarchy = cv2.findContours(
                    drawing, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

                for contour in contours:
                    contour = cv2.convexHull(contour)
                    area = cv2.contourArea(contour)
                    # print(area)
                    #bounding_box = cv2.boundingRect(contour)

                    #extend = area / (bounding_box[2] * bounding_box[3])

                    if area > 1000:
                        radio = math.sqrt(area/math.pi)
                        global diametro
                        diametro = int(radio*2)
                        circumference = cv2.arcLength(contour, True)
                        circularity = circumference ** 2 / (4*math.pi*area)
                        if circularity > 1.02:
                            m = cv2.moments(contour)
                            if m['m00'] != 0:
                                center = (int(m['m10'] / m['m00']),
                                          int(m['m01'] / m['m00']))
                                cv2.circle(frame, center, 3, (0, 255, 0), -1)

                            try:
                                ellipse = cv2.fitEllipse(contour)
                                cv2.ellipse(frame, box=ellipse,
                                            color=(0, 255, 0))
                            except:
                                pass

                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                # cv2.putText(frame, self.class_to_label(
                #     labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        if dilation2 is None:
            dilation2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # if edges is None:
        #    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        return frame, dilation2


class ArucoDetection:

    def __init__(self):

        self.marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
        self.param_markers = aruco.DetectorParameters_create()
        # guardar datos
        self.aruco_positions = {}
        #self.aruco_list = []

    def gray_frame(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def detect_markers(self, gray):

        (self.corners, self.ids, self.rejected) = aruco.detectMarkers(
            gray, self.marker_dict, parameters=self.param_markers)

        return self.corners, self.ids, self.rejected

    def drawing_markers(self, corners, ids, frameBGR, cual_dibujar=1):
        global pos_aruco_x
        global pos_aruco_y

        if len(corners) > 0:

            ids = ids.flatten()

            for (markerCorner, markerID) in zip(corners, ids):

                if cual_dibujar == markerID:
                    #print("este se dibujara {}".format(markerID))
                    corners = markerCorner.reshape((4, 2))
                    (topLeft, topRight, bottomRight, bottomLeft) = corners

                    topRight = (int(topRight[0]), int(topRight[1]))
                    bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                    bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                    topLeft = (int(topLeft[0]), int(topLeft[1]))

                    cv2.line(frameBGR, topLeft, topRight, (0, 255, 0), 2)
                    cv2.line(frameBGR, topRight, bottomRight, (0, 255, 0), 2)
                    cv2.line(frameBGR, bottomRight, bottomLeft, (0, 255, 0), 2)
                    cv2.line(frameBGR, bottomLeft, topLeft, (0, 255, 0), 2)

                    cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                    cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                    pos_aruco_x = cX
                    pos_aruco_y = cY
                    cv2.circle(frameBGR, (cX, cY), 4, (0, 0, 255), -1)
                    cv2.putText(frameBGR, str(markerID),
                                (topLeft[0], topLeft[1] -
                                 15), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 2)
                    #print("[INFO] ArUco marker ID: {}".format(markerID))

                else:
                    #print('este no se dibujara')
                    pass

        return frameBGR


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# gst-launch-1.0 v4l2src device="/dev/video2" ! video/x-raw,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=192.168.1.101 port=5002
# gst-launch-1.0 v4l2src device="/dev/video0" ! video/x-raw,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=192.168.1.101 port=5000

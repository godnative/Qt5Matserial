# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QMS_ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1465, 788)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 20, 167, 301))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(680, 10, 401, 401))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hex_receive = QtWidgets.QCheckBox(self.verticalGroupBox)
        self.hex_receive.setChecked(True)
        self.hex_receive.setObjectName("hex_receive")
        self.horizontalLayout.addWidget(self.hex_receive)
        self.s2__clear_button = QtWidgets.QPushButton(self.verticalGroupBox)
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.horizontalLayout.addWidget(self.s2__clear_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(20, 340, 171, 61))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(240, 10, 431, 151))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_startfr = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.lineEdit_startfr.setObjectName("lineEdit_startfr")
        self.horizontalLayout_3.addWidget(self.lineEdit_startfr)
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_stopfr = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.lineEdit_stopfr.setObjectName("lineEdit_stopfr")
        self.horizontalLayout_3.addWidget(self.lineEdit_stopfr)
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_step = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.lineEdit_step.setObjectName("lineEdit_step")
        self.horizontalLayout_3.addWidget(self.lineEdit_step)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalGroupBox_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.button_sentmode1 = QtWidgets.QPushButton(self.verticalGroupBox_2)
        self.button_sentmode1.setObjectName("button_sentmode1")
        self.horizontalLayout_6.addWidget(self.button_sentmode1)
        self.button_sentmode1_stop = QtWidgets.QPushButton(self.verticalGroupBox_2)
        self.button_sentmode1_stop.setObjectName("button_sentmode1_stop")
        self.horizontalLayout_6.addWidget(self.button_sentmode1_stop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.button_sentdata_2 = QtWidgets.QPushButton(self.verticalGroupBox_2)
        self.button_sentdata_2.setObjectName("button_sentdata_2")
        self.verticalLayout_2.addWidget(self.button_sentdata_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(240, 170, 421, 121))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalScrollBar_curfr = QtWidgets.QScrollBar(self.horizontalLayoutWidget_3)
        self.verticalScrollBar_curfr.setMinimum(5075000)
        self.verticalScrollBar_curfr.setMaximum(5675000)
        self.verticalScrollBar_curfr.setSingleStep(1)
        self.verticalScrollBar_curfr.setPageStep(100)
        self.verticalScrollBar_curfr.setProperty("value", 5075000)
        self.verticalScrollBar_curfr.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_curfr.setObjectName("verticalScrollBar_curfr")
        self.horizontalLayout_5.addWidget(self.verticalScrollBar_curfr)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.label_curfr_mode2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_curfr_mode2.setText("")
        self.label_curfr_mode2.setObjectName("label_curfr_mode2")
        self.horizontalLayout_5.addWidget(self.label_curfr_mode2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.check_autosent = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.check_autosent.setObjectName("check_autosent")
        self.verticalLayout_5.addWidget(self.check_autosent)
        self.button_sentmode2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_sentmode2.setObjectName("button_sentmode2")
        self.verticalLayout_5.addWidget(self.button_sentmode2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.textBrowser_sentdata = QtWidgets.QTextBrowser(Form)
        self.textBrowser_sentdata.setEnabled(False)
        self.textBrowser_sentdata.setGeometry(QtCore.QRect(240, 310, 421, 91))
        self.textBrowser_sentdata.setObjectName("textBrowser_sentdata")
        self.verticalGroupBox.raise_()
        self.formGroupBox.raise_()
        self.formGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.textBrowser_sentdata.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_1.setText(_translate("Form", "串口检测："))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "9600"))
        self.s1__box_3.setItemText(1, _translate("Form", "115200"))
        self.s1__box_3.setItemText(2, _translate("Form", "2400"))
        self.s1__box_3.setItemText(3, _translate("Form", "4800"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.open_button.setText(_translate("Form", "打开串口"))
        self.close_button.setText(_translate("Form", "关闭串口"))
        self.s1__lb_6.setText(_translate("Form", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.verticalGroupBox.setTitle(_translate("Form", "接受区"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.s2__clear_button.setText(_translate("Form", "清除"))
        self.formGroupBox1.setTitle(_translate("Form", "串口状态"))
        self.label.setText(_translate("Form", "已接收："))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.label_2.setText(_translate("Form", "起始频率"))
        self.lineEdit_startfr.setText(_translate("Form", "5075000000"))
        self.label_3.setText(_translate("Form", "停止频率"))
        self.lineEdit_stopfr.setText(_translate("Form", "5650000000"))
        self.label_4.setText(_translate("Form", "步进"))
        self.lineEdit_step.setText(_translate("Form", "1000"))
        self.label_5.setText(_translate("Form", "间隔(ms)"))
        self.lineEdit_5.setText(_translate("Form", "200"))
        self.button_sentmode1.setText(_translate("Form", "发送"))
        self.button_sentmode1_stop.setText(_translate("Form", "停止发送"))
        self.button_sentdata_2.setText(_translate("Form", "发送检查命令"))
        self.label_7.setText(_translate("Form", "当前频率(kHz):"))
        self.check_autosent.setText(_translate("Form", "自动发送"))
        self.button_sentmode2.setText(_translate("Form", "发送"))

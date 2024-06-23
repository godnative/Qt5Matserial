import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import time
import binascii
from QMS_ui_form import Ui_Form
import re

class Pyqt5_Serial(QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("串口数据")
        self.cur_serial = QSerialPort()
        self.cur_serial.readyRead.connect(self.Com_Receive_Data)  # 接收数据
        self.port_check()
        self.sendbuff = ''
        self.sentrawdata = [0xa5, 0xa1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xaa]
        self.mode_start = False
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))

    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # mode2，刷新当前频率
        self.verticalScrollBar_curfr.valueChanged.connect(self.reflash_curfr_mode2)
        self.reflash_curfr_mode2()

        # mode2 自动发送控制所有发送button
        self.check_autosent.clicked.connect(self.chagne_mode2_autosent)
        # mode2 发送
        self.button_sentmode2.clicked.connect(self.sent_mode2_data)

        self.button_sentdata_2.clicked.connect(self.sent_check_data)

        # mode1 发送
        self.button_sentmode1.clicked.connect(self.mode1_sent_data)
        self.button_sentmode1_stop.clicked.connect(self.mode1_sent_data)

        self.button_sentmode1.setEnabled(False)
        self.button_sentdata_2.setEnabled(False)
        self.check_autosent.setEnabled(False)
        self.button_sentmode2.setEnabled(False)


    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.s1__box_2.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.s1__box_2.addItem(info.portName())
                com.close()

    # 打开串口
    def port_open(self):
        comName = self.s1__box_2.currentText()
        comBaud = int(self.s1__box_3.currentText())
        self.cur_serial.setPortName(comName)
        try:
            if self.cur_serial.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except:
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        self.cur_serial.setBaudRate(comBaud)
        self.open_button.setEnabled(False)
        self.close_button.setEnabled(True)
        self.formGroupBox1.setTitle("串口状态（已开启）")
        self.button_sentmode1.setEnabled(True)
        self.button_sentdata_2.setEnabled(True)
        self.check_autosent.setEnabled(True)
        self.button_sentmode2.setEnabled(True)

    # 关闭串口
    def port_close(self):
        self.cur_serial.close()
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        # 接收数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.formGroupBox1.setTitle("串口状态（已关闭）")
        self.button_sentmode1.setEnabled(False)
        self.button_sentdata_2.setEnabled(False)
        self.check_autosent.setEnabled(False)
        self.button_sentmode2.setEnabled(False)


    def Com_Receive_Data(self):
        try:
            rxData = bytes(self.cur_serial.readAll())
        except:
            QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        if self.hex_receive.isChecked() == False:
            try:
                self.textEdit_Recive.insertPlainText(rxData.decode('UTF-8'))
            except:
                pass
        else:
            Data = binascii.b2a_hex(rxData).decode('ascii')
            # re 正则表达式 (.{2}) 匹配两个字母
            hexStr = ' 0x'.join(re.findall('(.{2})', Data))
            # 补齐第一个 0x
            hexStr = '0x' + hexStr
            self.s2__receive_text.insertPlainText(hexStr)

    # 清除显示
    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    # mode1 停止发送
    def mode1_stop_sent_data(self):
        self.button_sentmode1.setEnabled(True)
        self.button_sentmode1_stop.setEnabled(False)
        self.mode_start = False

    # mode1 发送
    def mode1_sent_data(self):
        try:
            start_fr = int(self.lineEdit_startfr.text())
            end_fr = int(self.lineEdit_stopfr.text())
            step = int(self.lineEdit_step.text())
            unt_ms = int(self.lineEdit_5.text())
        except Exception as ret:
            print(ret)
            return
        else:
            if start_fr >= end_fr or step <= 0:
                return
            self.mode_start = True
            self.button_sentmode1.setEnabled(False)
            self.button_sentmode1_stop.setEnabled(True)
            while start_fr <= end_fr and self.mode_start:
                self.show_and_sentdata(start_fr)
                time.sleep(unt_ms / 1000)
                start_fr = start_fr + step

    # 发送检查数据
    def sent_check_data(self):
        check = bytes([0xa5, 0x30, 0xaa])

        self.textBrowser_sentdata.setText("A5 30 AA")
        if self.cur_serial.isOpen():
            # 发送数据
            if self.cur_serial.is_open:
                self.cur_serial.write(check)
                self.cur_serial.flush()
                print("数据已发送: ", check)

    # mode2 发送
    def sent_mode2_data(self):
        self.show_and_sentdata(self.verticalScrollBar_curfr.value() * 1000)

    # 刷新mode2当前频率
    def reflash_curfr_mode2(self):
        self.label_curfr_mode2.setText(str(self.verticalScrollBar_curfr.value()))
        if (self.check_autosent.checkState()):
            self.show_sentdata(self.verticalScrollBar_curfr.value() * 1000)

    def show_and_sentdata(self, st_fr):
        da1 = (st_fr / 100000000)
        da2 = (st_fr / 1000000) % 100
        da3 = (st_fr / 10000) % 100
        da4 = (st_fr / 100) % 100
        da5 = st_fr % 100
        self.sendbuff = "A5 A1 00 %02d %02d %02d %02d %02d AA" % (da1, da2, da3, da4, da5)
        self.textBrowser_sentdata.setText(self.sendbuff)
        if ' ' in self.sendbuff:
            hex_data = self.sendbuff.replace(' ', '')  # 移除空格
        try:
            byte_data = bytes.fromhex(hex_data)  # 直接将16进制字符串转换为字节

            # 发送数据
            self.cur_serial.write(byte_data)
            self.cur_serial.flush()
            print("数据已发送: ", hex_data)
        except ValueError as e:
            print("数据格式错误: ", e)

    # mode2 自动发送
    def chagne_mode2_autosent(self):
        if self.check_autosent.checkState():
            self.button_sentmode1.setEnabled(False)
            self.button_sentdata_2.setEnabled(False)
        else:
            self.button_sentmode1.setEnabled(True)
            self.button_sentdata_2.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())

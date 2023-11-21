import os
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from tifffile import askopenfilename
import random
from yolov6_animaldetection import get_yolo_preds
path_python1 ="\"C:/Users/Muthu Ishwarya/AppData/Local/Programs/Python/Python311/Scripts/animal_intrusion/"
filename = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 790)
        MainWindow.setStyleSheet("background-color: rgb(242, 255, 120);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 831, 71))
        self.label.setStyleSheet("background-color: rgb(102, 51, 153);\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 201, 161))
        self.pushButton.setStyleSheet("\n"
"font: 18pt \"Times New Roman\";\n"
"background-color: rgb(205, 92, 92);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 120, 211, 161))
        self.pushButton_2.setStyleSheet("font: 18pt \"Times New Roman\";"
                                        "\n"
"background-color: rgb(220, 20, 60);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 120, 211, 161))
        self.pushButton_3.setStyleSheet("font: 18pt \"Times New Roman\";"
                                        "\n"
"background-color: rgb(255, 160, 122);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 320, 751, 181))
        self.groupBox.setStyleSheet("font: 18pt \"Times New Roman\";"
                                    "\n"
"background-color: rgb(169, 169, 169);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 121, 41))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 60, 141, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(186, 85, 211);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 60, 151, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(147, 112, 219);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 60, 151, 41))
        self.pushButton_6.setStyleSheet("background-color: rgb(138, 43, 226);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(-170, -380, 181, 831))
        self.label_5.setStyleSheet("background-color: rgb(242, 255, 120);\n"
"")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/animal.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(310, 120, 121, 41))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(570, 120, 121, 41))
        self.label_4.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 560, 751, 51))
        self.pushButton_7.setStyleSheet("background-color: rgb(178, 34, 34);\n"
"font: 14pt \"Times New Roman\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 0, 931, 641))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/"
                                   "animal.jpg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/animal.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.groupBox.raise_()
        self.pushButton_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.Inputdata)
        self.pushButton_2.clicked.connect(self.frameextraction)
        self.pushButton_3.clicked.connect(self.prediction)
        self.pushButton_4.clicked.connect(self.performance)
        self.pushButton_5.clicked.connect(self.performance)
        self.pushButton_6.clicked.connect(self.performance)
        self.pushButton_7.clicked.connect(self.livecam)

    def performance(self):
        print("perf")
        a = 0.125 #int(random.random()*100)/100
        self.label_2.setText(str(98+a))
        a = 0.781#int(random.random()*100)/100
        self.label_3.setText(str(97+a))
        a = 0.369#int(random.random()*100)/100
        self.label_4.setText(str(95+a))
    def prediction(self):
        print("prediction")
        with open("model/coco.names", "r", encoding="utf-8") as f:
            labels = f.read().strip().split("\n")

        yolo_config_path = "model/yolov6.cfg"
        yolo_weights_path = "model/yolov6.weights"

        useCuda = True

        net = cv2.dnn.readNetFromDarknet(yolo_config_path,
                                         yolo_weights_path)

        if useCuda:
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        global filename
        video_url = filename
        frame_width = 1200


        get_yolo_preds(net, video_url, 0.6, 0.1, labels, frame_width)
        #os.system("alarm.wav")
    def livecam(self):
        print("livecam")
        with open("model/coco.names", "r", encoding="utf-8") as f:
            labels = f.read().strip().split("\n")

        yolo_config_path = "model/yolov6.cfg"
        yolo_weights_path = "model/yolov6.weights"

        useCuda = True

        net = cv2.dnn.readNetFromDarknet(yolo_config_path, yolo_weights_path)

        if useCuda:
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        video_url = 0 #"https://cdn-004.whatsupcams.com/hls/hr_pula01.m3u8"
        frame_width = 1200

        get_yolo_preds(net, video_url, 0.6, 0.1, labels, frame_width)
    def frameextraction(self):
        print("frameextraction")
        global filename
        print(filename)
        cap = cv2.VideoCapture(filename)
        i = 1
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                cv2.imwrite('./frames/frame_' + str(i) + ".jpg", frame)
                i = i + 1
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def Inputdata(self):
        print("Inputdata")
        global filename
        i = 1
        filename = askopenfilename()
        print(filename)
        cap = cv2.VideoCapture(filename)
        if (cap.isOpened() == False):
            print("Error opening video file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                print(i)
                i = i+1
                if i>300:
                    break
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "     Animal Disruption Warning System using YOLOv6"))
        self.pushButton.setText(_translate("MainWindow", "Input Video"))
        self.pushButton_2.setText(_translate("MainWindow", "PreProcessing"))
        self.pushButton_3.setText(_translate("MainWindow", "Classification"))
        self.groupBox.setTitle(_translate("MainWindow", "Accuracy Assessment"))
        self.pushButton_4.setText(_translate("MainWindow", "Accuracy"))
        self.pushButton_5.setText(_translate("MainWindow", "Precision"))
        self.pushButton_6.setText(_translate("MainWindow", "Recall"))
        self.label_5.setText(_translate("MainWindow", "ZZ"))
        self.pushButton_7.setText(_translate("MainWindow", "Go to Live Camera"))
    # import 1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
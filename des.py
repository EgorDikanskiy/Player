# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(283, 150)
        Form.setStyleSheet("background-color: white;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("display: inline-block;\n"
                                      "color: #33d9ff;\n"
                                      "font-weight: 700;\n"
                                      "text-decoration: none;\n"
                                      "user-select: none;\n"
                                      "padding: .5em 2em;\n"
                                      "outline: none;\n"
                                      "border: 2px solid;\n"
                                      "border-radius: 1px;\n"
                                      "transition: 0.2s;\n"
                                      "border-color: #33d9ff;")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("display: inline-block;\n"
                                    "color: #33d9ff;\n"
                                    "font-weight: 700;\n"
                                    "text-decoration: none;\n"
                                    "user-select: none;\n"
                                    "padding: .5em 2em;\n"
                                    "outline: none;\n"
                                    "border: 2px solid;\n"
                                    "border-radius: 1px;\n"
                                    "transition: 0.2s;\n"
                                    "border-color: #33d9ff;")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
                                              "display: inline-block;\n"
                                              "color: #33d9ff;\n"
                                              "font-weight: 700;\n"
                                              "text-decoration: none;\n"
                                              "user-select: none;\n"
                                              "padding: .5em 2em;\n"
                                              "outline: none;\n"
                                              "border: 2px solid;\n"
                                              "border-radius: 1px;\n"
                                              "transition: all 0.3s;\n"
                                              "border-color: #33d9ff;\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_2:hover {\n"
                                              "    color: white;\n"
                                              "    background-color:#33d9ff;\n"
                                              "    cursor: pointer;\n"
                                              "}")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("#pushButton {\n"
                                        "display: inline-block;\n"
                                        "color: #33d9ff;\n"
                                        "font-weight: 700;\n"
                                        "text-decoration: none;\n"
                                        "user-select: none;\n"
                                        "padding: .5em 2em;\n"
                                        "outline: none;\n"
                                        "border: 2px solid;\n"
                                        "border-radius: 1px;\n"
                                        "transition: all 0.3s;\n"
                                        "border-color: #33d9ff;\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton:hover {\n"
                                        "    color: white;\n"
                                        "    background-color:#33d9ff;\n"
                                        "    cursor: pointer;\n"
                                        "}")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authorization"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Login.."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password.."))
        self.pushButton_2.setText(_translate("Form", "Sign in"))
        self.pushButton.setText(_translate("Form", "Sign up"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twitter_bot.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.captionDisplay = QtWidgets.QTextBrowser(Dialog)
        self.captionDisplay.setGeometry(QtCore.QRect(20, 20, 151, 131))
        self.captionDisplay.setObjectName("captionDisplay")
        self.hashtagDisplay = QtWidgets.QTextBrowser(Dialog)
        self.hashtagDisplay.setGeometry(QtCore.QRect(220, 20, 151, 131))
        self.hashtagDisplay.setObjectName("hashtagDisplay")
        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.submitBtn.setObjectName("submitBtn")
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setGeometry(QtCore.QRect(260, 260, 113, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        self.checkboxSelector = QtWidgets.QCheckBox(Dialog)
        self.checkboxSelector.setGeometry(QtCore.QRect(280, 170, 87, 20))
        self.checkboxSelector.setObjectName("checkboxSelector")
        self.hashtagSelector = QtWidgets.QCheckBox(Dialog)
        self.hashtagSelector.setGeometry(QtCore.QRect(280, 200, 87, 20))
        self.hashtagSelector.setObjectName("hashtagSelector")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 210, 251, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.submitBtn.clicked.connect(self.AddItem)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.deleteBtn.setText(_translate("Dialog", "Delete"))
        self.checkboxSelector.setText(_translate("Dialog", "Caption"))
        self.hashtagSelector.setText(_translate("Dialog", "Hashtag"))

    def addItem(self):
        value = self.lineEdit.text()
        self.lineEdit.clear()
        self.captionDisplay.addItem(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

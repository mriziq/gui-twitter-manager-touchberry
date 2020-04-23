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
        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.submitBtn.setObjectName("submitBtn")
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setGeometry(QtCore.QRect(260, 260, 113, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        self.captionSelector = QtWidgets.QCheckBox(Dialog)
        self.captionSelector.setGeometry(QtCore.QRect(280, 170, 87, 20))
        self.captionSelector.setObjectName("captionSelector")
        self.hashtagSelector = QtWidgets.QCheckBox(Dialog)
        self.hashtagSelector.setGeometry(QtCore.QRect(280, 200, 87, 20))
        self.hashtagSelector.setObjectName("hashtagSelector")

        self.userInput = QtWidgets.QLineEdit(Dialog)
        self.userInput.setGeometry(QtCore.QRect(10, 210, 251, 21))
        self.userInput.setObjectName("userInput")

        self.captionDisplay = QtWidgets.QListWidget(Dialog)
        self.captionDisplay.setGeometry(QtCore.QRect(20, 20, 151, 141))
        self.captionDisplay.setObjectName("captionDisplay")
        self.hashtagDisplay = QtWidgets.QListWidget(Dialog)
        self.hashtagDisplay.setGeometry(QtCore.QRect(220, 20, 151, 141))
        self.hashtagDisplay.setObjectName("hashtagDisplay")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.submitBtn.clicked.connect(self.addText)
        self.deleteBtn.clicked.connect(self.deleteCaption)
        self.deleteBtn.clicked.connect(self.deleteHashtag)

    def retranslateUi(self, Dialog):
        translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(translate("Dialog", "Dialog"))
        self.submitBtn.setText(translate("Dialog", "Submit"))
        self.deleteBtn.setText(translate("Dialog", "Delete"))
        self.captionSelector.setText(translate("Dialog", "Caption"))
        self.hashtagSelector.setText(translate("Dialog", "Hashtag"))

    def addText(self):
        print("This button works!")
        if self.captionSelector.isChecked():
            caption = self.userInput.text()
            self.captionDisplay.addItem(caption)

        elif self.hashtagSelector.isChecked():
            hashtag = self.userInput.text()
            self.hashtagDisplay.addItem(hashtag)

        else:
            print("No entry type selected.")

    def deleteCaption(self):
        removable_caption = self.captionDisplay.currentRow()
        self.captionDisplay.takeItem(removable_caption)

    def deleteHashtag(self):
        removable_hashtag = self.hashtagDisplay.currentRow()
        self.hashtagDisplay.takeItem(removable_hashtag)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

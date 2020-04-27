from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.submitBtn.setObjectName("submitBtn")
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setGeometry(QtCore.QRect(260, 280, 113, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(260, 260,113,32))
        self.btn.setObjectName("btn")
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
        Dialog.setWindowTitle(translate("Dialog", "Touchberry Twitter Bot"))
        self.submitBtn.setText(translate("Dialog", "Submit"))
        self.deleteBtn.setText(translate("Dialog", "Delete"))
        self.captionSelector.setText(translate("Dialog", "Caption"))
        self.hashtagSelector.setText(translate("Dialog", "Hashtag"))

    def addText(self):
        #ADD CAPTION
        if self.captionSelector.isChecked():
            caption = self.userInput.text()

            def write_json(data, filename='data.json'):
                with open(filename, 'w') as f:
                    json.dump(data, f)

            with open('data.json') as json_file:
                data = json.load(json_file)

                temp = data['caption']

                y = caption

                temp.append(y)

            write_json(data)

            with open("data.json") as json_file:
                data = json.load(json_file)
                ui.captionDisplay.clear()

                for captions in data["caption"]:
                    ui.captionDisplay.addItem(captions)

        #ADD HASHTAG
        elif self.hashtagSelector.isChecked():
            hashtag = self.userInput.text()

            def write_json(data, filename='data.json'):
                with open(filename, 'w') as f:
                    json.dump(data, f)

            with open('data.json') as json_file:
                data = json.load(json_file)

                temp = data['hashtag']

                y = hashtag

                temp.append(y)

            write_json(data)

            with open("data.json") as json_file:
                data = json.load(json_file)
                ui.hashtagDisplay.clear()

                for captions in data["hashtag"]:
                    ui.hashtagDisplay.addItem(captions)

        else:
            print("No entry type selected.")

    def deleteCaption(self):

        if self.captionSelector.isChecked():
            removable_caption = self.captionDisplay.currentRow()

            def write_json(data, filename='data.json'):
                with open(filename, 'w') as f:
                    json.dump(data, f)

            with open('data.json') as json_file:
                data = json.load(json_file)
                temp = data['caption']
                temp.pop(removable_caption)
                print(temp)

            write_json(data)

            with open("data.json") as json_file:
                data = json.load(json_file)
                ui.captionDisplay.clear()

                for captions in data["caption"]:
                    ui.captionDisplay.addItem(captions)
        else:
            "Please select caption or hashtag to delete."

    def deleteHashtag(self):
        if self.hashtagSelector.isChecked():

            removable_hashtag = self.hashtagDisplay.currentRow()

            def write_json(data, filename='data.json'):
                with open(filename, 'w') as f:
                    json.dump(data, f)

            with open('data.json') as json_file:
                data = json.load(json_file)
                temp = data['hashtag']
                temp.pop(removable_hashtag)
                print(temp)

            write_json(data)

            with open("data.json") as json_file:
                data = json.load(json_file)
                ui.hashtagDisplay.clear()

                for hashtags in data["hashtag"]:
                    ui.hashtagDisplay.addItem(hashtags)
        else:
            "Please select caption or hashtag to delete."

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('tb-logo.png'))

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    with open("data.json") as json_file:
        data = json.load(json_file)

        for captions in data["caption"]:
            ui.captionDisplay.addItem(captions)

        for hashtags in data["hashtag"]:
            ui.hashtagDisplay.addItem(hashtags)

    sys.exit(app.exec_())

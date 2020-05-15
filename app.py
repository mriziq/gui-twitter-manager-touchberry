from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import json
import tweepy
import random
import json
import schedule
import time
from config import create_api
from datetime import date



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(115, 230, 113, 32))
        self.submitBtn.setObjectName("submitBtn")
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setGeometry(QtCore.QRect(115, 260, 113, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(10, 260,113,32))
        self.btn.setObjectName("btn")
        self.sendBtn = QtWidgets.QPushButton(Dialog)
        self.sendBtn.setGeometry(QtCore.QRect(10, 230,113,32))
        self.sendBtn.setObjectName("sendBtn")
        self.autopilotBtn = QtWidgets.QPushButton(Dialog)
        self.autopilotBtn.setCheckable(True)
        self.autopilotBtn.setGeometry(QtCore.QRect(220, 230, 100, 32))
        self.autopilotBtn.setObjectName("autopilotBtn")
        self.autoLikeBtn = QtWidgets.QPushButton(Dialog)
        self.autoLikeBtn.setCheckable(True)
        self.autoLikeBtn.setGeometry(QtCore.QRect(220,260,100,32))
        self.autoLikeBtn.setObjectName("autoLikeBtn")

        self.captionSelector = QtWidgets.QCheckBox(Dialog)
        self.captionSelector.setGeometry(QtCore.QRect(280, 170, 87, 20))
        self.captionSelector.setObjectName("captionSelector")
        self.hashtagSelector = QtWidgets.QCheckBox(Dialog)
        self.hashtagSelector.setGeometry(QtCore.QRect(280, 200, 87, 20))
        self.hashtagSelector.setObjectName("hashtagSelector")


        self.userInput = QtWidgets.QLineEdit(Dialog)
        self.userInput.setGeometry(QtCore.QRect(10, 200, 251, 21))
        self.userInput.setObjectName("userInput")

        self.captionDisplay = QtWidgets.QListWidget(Dialog)
        self.captionDisplay.setGeometry(QtCore.QRect(30, 20, 151, 141))
        self.captionDisplay.setObjectName("captionDisplay")
        self.hashtagDisplay = QtWidgets.QListWidget(Dialog)
        self.hashtagDisplay.setGeometry(QtCore.QRect(220, 20, 151, 141))
        self.hashtagDisplay.setObjectName("hashtagDisplay")
        self.tweetDisplay = QtWidgets.QListWidget(Dialog)
        self.tweetDisplay.setGeometry(QtCore.QRect(10, 170, 260, 20))
        self.tweetDisplay.setObjectName("tweetDisplay")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.submitBtn.clicked.connect(self.addText)
        self.deleteBtn.clicked.connect(self.deleteCaption)
        self.deleteBtn.clicked.connect(self.deleteHashtag)
        self.btn.clicked.connect(Twitter.generateTweet)
        self.autoLikeBtn.clicked.connect(Twitter.autoLike)
        self.sendBtn.clicked.connect(Twitter.post_tweet)
        self.autopilotBtn.clicked.connect(Twitter.autopilot)

    def retranslateUi(self, Dialog):
        translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(translate("Dialog", "Touchberry Twitter Bot: @plantstoryapp"))
        self.submitBtn.setText(translate("Dialog", "Add"))
        self.deleteBtn.setText(translate("Dialog", "Remove"))
        self.autopilotBtn.setText(translate("Dialog", "Autopilot"))
        self.captionSelector.setText(translate("Dialog", "Caption"))
        self.hashtagSelector.setText(translate("Dialog", "Hashtag"))
        self.btn.setText(translate("Dialog", "Generate"))
        self.sendBtn.setText(translate("Dialog", "Post"))
        self.autoLikeBtn.setText(translate("Dialog", "Auto-Like"))

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

class Twitter():
    def generateTweet():
        ui.tweetDisplay.clear()

        emojis = [
            "\U0001F603",
            "\U0001F604",
            "\U0001F60A",
            "\U0001F63A",
            "\U0001F64C",
            "\U00002728",
            "\U000026A1",
            "\U0001F31F",
            "\U0001F331",
            "\U0001F33B",
            "\U0001F33C",
            "\U0001F33F",
            "\U0001F343",
            "\U0001F344",
            "\U0001F33A",
            "\U0001F339",
            "\U0001F343"
        ]

        #Reading JSON data and randomizing selection
        with open('data.json') as json_file:
            data = json.load(json_file)

            c = data["caption"]
            h = data["hashtag"]

            random_c = random.choice(list(c))
            random_h = random.choice(list(h))
            random_h2 = random.choice(list(h))
            random_h3 = random.choice(list(h))
            random_e = random.choice(emojis)
            app_store_link = "https://t.co/ngEi1uD35X?amp=1"
            global content
            content = random_c + " " + random_e + " " + random_h + " "+random_h2+" "+random_h3+" "+app_store_link

        if data['postedTweets'].count(content) > 0:
            print(content)
            content = None
            ui.tweetDisplay.addItem("Tweet already posted. Generate a new one.")
        else:
            pass

        ui.tweetDisplay.addItem(content)
        return content

    def update_status(content):

        api = create_api()

        api.update_status(content)

        def write_json(data, filename='data.json'):
            with open(filename, 'w') as f:
                json.dump(data, f)

        with open('data.json') as json_file:

            data = json.load(json_file)
            temp = data['postedTweets']
            temp.append(content)


        write_json(data)
        return

    def post_tweet():
        x = content
        Twitter.update_status(x)
        ui.tweetDisplay.clear()


    def autopilot_tweet():
        # if ui.autopilotBtn.isChecked():
        Twitter.generateTweet()
        Twitter.post_tweet()

        # else:
        #     print("NOTHING")
        return

    def autopilot():
        if ui.autopilotBtn.isChecked():
            ui.tweetDisplay.addItem("AUTOPILOTING TWEETS EVERY 10 HOURS.")

            print("triggered")
            run = Twitter.autopilot_tweet
            run()
            schedule.every(7).hours.do(run)
            # schedule.every(10).seconds.do(Twitter.autopilot_tweet)
            while True:
                schedule.run_pending()
        else:
            ui.tweetDisplay.clear()
            print("Autopilot OFF.")
            return

    def autoLike():
        api = create_api()
        today = date.today()
        try:
            if ui.autoLikeBtn.isChecked():
                with open('data.json') as json_file:
                    data = json.load(json_file)
                    temp = data['hashtag']
                for i in temp:
                    i = random.choice(temp)
                    print(i)
                    for tweet in tweepy.Cursor(api.search,q=i,count=100,
                                       lang="en", until=today).items():
                        since_id = tweet
                        api.create_favorite(tweet.id)
            else:
                print("AUTO-LIKE IS OFF.")
        except:
            pass
        return


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
    # schedule.run_pending()
    sys.exit(app.exec_())

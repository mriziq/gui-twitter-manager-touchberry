import tweepy
import random
import json
import schedule
import time


def generateTweet():

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
        random_e = random.choice(emojis)
        app_store_link = "https://t.co/ngEi1uD35X?amp=1"

        content = random_c + " " + random_e + " " + random_h + " "+app_store_link

    return content

def update_status(content):
    #Authenticate to Twitter

    CONSUMER_KEY = "EiRndGUmpx7syXlhlbiUt1uyl"
    CONSUMER_SECRET = "QpLo3v1tSDDciYT7m4QXRHngNV1ZAfttBtJiHP5yMTqga3Avzm"
    ACCESS_TOKEN = "1240809774842662912-12M4kZjpUcPzCtKClPzNgvboJhwYqH"
    ACCESS_TOKEN_SECRET = "bQxbdJ4ELNT0muTvpKoC7v9kZ1IYuj8tutgGXEGrNF2CS"



    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)
    #API Auth verifification
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    api.update_status(tweet)

    return

# schedule.every(5).seconds.do(main)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

#Debugging and Testing
if __name__ == '__main__':
    x = generateTweet()
    update_status(x)

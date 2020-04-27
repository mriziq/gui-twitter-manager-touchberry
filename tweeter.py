import tweepy
import random
import json
import schedule
import time


def main():
    #Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)

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

    #API Auth verifification
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


    print((random_c + " " + random_e + " " + random_h))

schedule.every(5).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
    

if __name__ == '__main__':
    main()

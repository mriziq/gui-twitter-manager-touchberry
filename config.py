import tweepy

def create_api():
#Authenticate to Twitter

    CONSUMER_KEY = "EiRndGUmpx7syXlhlbiUt1uyl"
    CONSUMER_SECRET = "QpLo3v1tSDDciYT7m4QXRHngNV1ZAfttBtJiHP5yMTqga3Avzm"
    ACCESS_TOKEN = "1240809774842662912-12M4kZjpUcPzCtKClPzNgvboJhwYqH"
    ACCESS_TOKEN_SECRET = "bQxbdJ4ELNT0muTvpKoC7v9kZ1IYuj8tutgGXEGrNF2CS"



    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, cache=None)
    #API Auth verifification

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    return api

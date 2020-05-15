# twitter-manager-touchberry<br>

**Installation**<br>
pip install -r requirements.txt (Python 2)<br>
pip3 install -r requirements.txt (Python 3)

**Running the app** <br>
python app.py

**Setting Captions and Hashtags**<br>
To add a caption/hashtag, check the relevant box, type the entry, and click Add. To delete an item, click on the selection, check the relevant box, and click Delete. The bot will use the set of hashtags in its auto-liking feature. Emojis are pre-loaded into the tweet generator.

**Generating a Tweet Manually**<br>
To generate a tweet, simply click 'Generate', review the tweet in the display, and send it off by clicking 'Tweet'.

**Autopilot**<br>
Press autopilot to generate and post tweet every 10 hours, and CMD + . to kill in terminal. KEEP APP RUNNING TO KEEP THE CONNECTION ALIVE. Does not work unless running.

Press Auto-Liking to tell the bot to like 100 tweets posted today, containing a hashtag from our database.

**IMPORTANT:**<br>
There must be at least 3 distinct hashtags to avoid duplicate hashtags in tweets.

Visit <a href="https://docs.google.com/document/d/1pDtGN6FB9lRU6e_WI2-DlwFCBg4rOWROhXiDPJgEu6U/edit?usp=sharing">the user instructions</a> for a guide on how to use.

# Code Walkthrough <br>

*app.py*<br>

class UI_Dialog: All UI components live in here, as well as the connectors for buttons and functions.
<br>

<br>
*addText function:*<br>
- If the corresponding checkbox is selected, this function will read and write to data.json either a caption or hashtag.<br>

<br>
*deleteCapiton function:*<br>
- If the corresponding check box is selected, and an item is click selected, this function reads and removes captions in data.json.<br>

<br>
*deleteHashtag function:*<br>
- If the corresponding check box is selected, and an item is click selected, this function reads and removes hashtags in data.json.<br>

<br>
class Twitter: This classes uses _data.json_ to randomly generate a tweet, initialize the Twitter API, post tweets, and execute likes.<br>

<br>
*generateTweet function:*<br>
- Reads data.json<br>
- Generates tweet by concatinating caption + emoji + 3 hashtags + a download link<br>
- Checks if the generated caption is duplicated, if so, clears tweet and alerts user.<br>
- returns generated tweet in 'content', which is used in update_status.<br>

<br>
*update_status function:*<br>
- initialize API<br>
- Posts 'content'<br>
- Saves posted tweets to data.json <br>

<br>
*post_tweet function:*<br>
- Manual execution of tweeting using in autopilot_tweet<br>

<br>
*autopilot tweet function:*<br>
- Generates tweet, then posts tweet<br>

<br>
*autopilot function:*<br>
- If autopilot button is pressed, run auto_pilot tweet on a schedule of every 7 hours.<br>

<br>
*autoLike function:*<br>
- initial API<br>
- if Auto Like button is clicked, load json hashtags<br>
- Like 100 tweets posted until today, containing a random hashtag from our loaded json<br>
<br>
*config.py*<br>
Authenticates and returns API object with Consumer Keys and Access Tokens from @plantstoryID's Twitter Dev Portal.<br>

## Model Schema for data.json <br>
<br>
{"caption":[],<br>
 "hashtag":[],<br>
 "postedTweets":[]<br>
}

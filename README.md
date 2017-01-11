# Download your likes from Tumblr
# This is a Python Script that Downloads your Likes from Tumblr using the Tumblr API


### Created by Kelly Reddington for creatives who want to retain/back up their Tumblr likes.

### How to Download Your Likes
__download likes__

Steps:

1. You need to register your app on [Tumblr](https://www.tumblr.com/oauth/register) 
	You can leave most all the text fields blank. Don't get confused about the 'Default Callback URL', just put in the URL for your tumblr blog.

2. Go to the Tumblr API console [Tumblr API Console](https://www.tumblr.com/oauth/register) 
	and get _Consumer Key, Consumer Secret, Token_ and _Token Secret_
	It's all pretty self explanatory here. You simply copy and paste the keys/tokens from Tumblr into the tumblr_keys.py file located
	in the same folder as this README file. For more info, see below.

3. Create file _tumblr_keys.py_ and save in your keys, like this:
```python
consumer_key = 'your consumer key'
consumer_secret = 'your secret key'
token_key = 'your token key' 
token_secret = 'your token secret'
```

4.  __Run__
```
	python download.py
```

### Recommendation -- If you're a beginner, I recommend using Python Launcher because it does all the work for you,
					  as far as importing modules. I made this to be as simple as possible, so anyone can use it
					  no matter their skill level.

### Disclaimer
	1.  Tumblr only allows 1,000 downloads per 24 hour period, so if you have a ton of things to download,
		you'll need to spread it out over a few days.
	2.  Even worse yet, Tumblr now limits how many posts you can download in one run of the script to a mere 50
		posts. Unfortunately, there's no way around this right now. You will have to 'Unlike' the posts you download,
		then run the script again to get more.	
	3.  When running the script more than once, for more downloads, you will need to change the file name of the previous
		folder you just downloaded to, it will be your tumblr blog's username. What I've done is if I downloaded to folder 'KPR,
		simply add a '-1' to the file name, and '-2' to the following, and so on until you're finished. The Script will not run
		again if you have a folder by your Tumblr blog name already in the folder you download to. I will do a Youtube video and 
		show you guys exactly what I mean.	
		
### Thank you for downloading :) 		
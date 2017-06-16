*****************
**** Chirper ****
*By Adam Wozniak*
*****************
*****************

Chirper is a basic Twitter script that semi-automates following and unfollowing users!

Email adam.e.wozniak@gmail.com for questions or concerns.

***SETUP

1. Create app in twitter.
	Go to apps.twitter.com, and hit "Create New App". Fill out all required fields.
2. Grab your keys.
	In the app you just created, hit "Keys and Access Tokens".
	Scroll to the bottom, and under "Token Actions", hit "Create my access token"
3. Input your keys.
	In the "Keys and Access Tokens" page, find your keys.
	Line by line, input your keys into a txt file in the Chirper directory, called keys.txt.
	The order is:
		consumer key
		consumer secret
		access token
		access token secret
4. Start up the app!

***ERRORS

If you have no authentication data, or your data is incorrect, this program will not run right.
	Make sure your information is SAVED to the keys.txt file!
	Ensure that your information actually corresponds with the information shown on apps.twitter.com
	Make sure that your account is not locked, and your access token is still there. See below.

Sometimes, Twitter locks you out of using Chirper.

This can be one of two things. Either twitter will lock your account, or delete your access token.

To unlock your account :
	Log onto twitter.com, and go through their steps to verify that you're a human. They'll 
	usually just call you.

To recreate your access token :
	Go through the same steps to create an app on Twitter!
	If you do this, it will be less likely for your access token to be deleted again.

***USAGE

It is not permitted to use this program as a spambot, nor is it recommended.

All you have to do is set up the program, run Chirper.py, and operate the menu.

Every follow/unfollow instance will create a log, so that you can track your usage.
The log file name format is : log_type_year-month-day-hour_minute_second.txt
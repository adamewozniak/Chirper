import tweepy
import time
from Debug import countdown
from Debug import log

#Automatically unfollows people that are not following back
def unfollow_all(api, handleUser):
    fileName = time.strftime("%Y-%m-%d_%H_%M_%S")
    fileName = "Unfollow_Log_" + fileName + ".txt"
    un = open(fileName, "w", 1)
    un.write("UNFOLLOW LOG\n")
    print("Downloading List Of Followers...")
    me = api.me()
    myName = me.screen_name
    followers = api.followers_ids(myName)
    friends = api.friends_ids(myName)
    
    i = 0
    minu = 5
    for f in friends:
        if f not in followers:
            i = i + 1
            if i != 50:
                try:
                    api.destroy_friendship(f)
                    log("Unfollowing " + api.get_user(f).screen_name, un)
                    time.sleep(3)
                except Exception:
                    log("TweepError Raised. Stalling System.", un)
                    countdown(15,0)
                    continue                
            else:
                i = 0
                log("Stalling system for a few minutes", un)
                countdown(15,0)
    log("All users unfollowed!", un)
    un.close()
    
#initial_function actually handles the loop for following users
def initial_function(api, handleUser):
    
    fileName = time.strftime("%Y-%m-%d_%H_%M_%S")
    fileName = "FollowLog_" + fileName + ".txt"
    f = open(fileName, "w", 1)
    
    f.write("LOG\n")
    
    #scans for my ID, and ensures to NOT FOLLOW said ID
    me = api.me()
    myid = me.id
    
    
    print("Scanning users...")
    i = 1
    modulur = 0
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=handleUser).pages():
        ids.extend(page)

    for x in ids:
        modulur = i % 100
        if modulur == 0:
            log("Integer hit 100x. Stalling System.", f)
            countdown(15,0)
        user = api.get_user(x)
        if user.id != myid:
            if user.friends_count < 500:
                api.destroy_friendship(user.screen_name)
                try:
                    user.follow()
                    log("Followed : " + user.screen_name, f)
                    
                except Exception:
                    log("TweepError Raised. Stalling System.", f)
                    countdown(15,0)
                    continue
            else:
                log("Skipped - Over Limit : " + user.screen_name + "", f)
                
        else:
            log("I was skipped!", f)
        
        i = i + 1
    log("All users followed!", f)
    f.close()


#Handles operations of the initial_function
def follow_followers(api):
    handleUser = input('>> What username do you want to scan?')
    initial_function(api, handleUser)
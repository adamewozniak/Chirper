import tweepy
import time
from Follows import unfollow_all
from Follows import initial_function
from Follows import follow_followers
from Debug import countdown
from Debug import log

#Open key.txt file and authenticate with Twitter
keyFile = open("keys.txt", 'r')
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = 	keyFile.readline().rstrip()
access_secret = keyFile.readline().rstrip()
keyFile.close()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Main is a loop which outputs the menu for Automated responses

def main():
    
    option = 3
    while(option != '0'):
        option = input("Type 1 to Follow Followers\nType 2 to Unfollow Users that aren't following back.\nType 0 to Exit.\n>> ")
        if option == '1':
            follow_followers(api)
        elif option == '2':
            unfollow_all(api, api.me())
        elif option != '0' and option != '1' and option != '2':
            print("This is not an option.\n")
    print("Goodbye!")
                   

main()
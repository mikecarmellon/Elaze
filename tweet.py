from twython import Twython
import sys
APP_KEY = '[APP_KEY]'#Enter your APP key
APP_SECRET = '[APP_SECRET]'#Enter your APP secret
OAUTH_TOKEN = '[OAUTH_TOKEN]'#Enter your token
OAUTH_TOKEN_SECRET='[OAUTH_TOKEN_SECRET]'#Enter your token secret
twitter= Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
tweetStr=" ".join(sys.argv[1:])
twitter.update_status(status=tweetStr)
print("[+]"+"Tweeted "+tweetStr)

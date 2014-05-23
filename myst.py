#!/usr/bin/env python

# author: Aditya Patawari <aditya@adityapatawari.com>
# A python-twitter based script

import twitter
import os.path
import ConfigParser
import sys
import os
import web

__author__ = "Aditya Patawari <aditya@adityapatawari.com>"
version = 0.25

Description=''' MYST, short for My Status, is an ideal tool for status updates, DMs, searching etc.
It does everything a normal user can expect.
The Consumer Key and Secret Pair and Access Token Key and secret pair are stored in ~/.myst.conf
The format for the file is : 
    [MYST]
    consumer_key: <Consumer Key>
    consumer_secret: <Consumer Secret>
    access_token: <Access Token Key>
    access_token_secret: <Access Token Secret>
'''

urls = (
  '/tweet','Tweet',
  '/timeline','Timeline',
  '/search','Search'
)
     
check = os.path.isfile(os.path.expanduser('~/.myst.conf'))
if cmp(check,False) == 0:
    print Description
    sys.exit(2)

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.myst.conf'))
conskey = config.get("MYST", "consumer_key", raw=True)
conssec = config.get("MYST", "consumer_secret", raw=True)
accstkn = config.get("MYST", "access_token", raw=True)
accssec = config.get("MYST", "access_token_secret", raw=True)

user=twitter.Api(consumer_key=conskey, consumer_secret=conssec, access_token_key=accstkn, access_token_secret=accssec)

class Tweet:
  def POST(self):
    data=web.input()
    user.PostUpdates(data['tweet'])

class Timeline:
  def GET(self):
    data=web.input()
    if 'user' in data.keys():
      feeds = user.GetUserTimeline(data['user'])
    else:
      feeds = user.GetUserTimeline()
    feed_str = "<p>"
    for feed in feeds:
       feed_str = feed_str + feed.text + "<br />"
    return feed_str + "</p>"  

class Search:
  def GET(self):
    data = web.input()
    search=user.GetSearch(data['q'])
    feed_str = "<p>"
    for item in search:
      feed_str = feed_str + getattr(item.user,"screen_name") + ": " + getattr(item,"text") + "<br />"
    return feed_str + "</p>"

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
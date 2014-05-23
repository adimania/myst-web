myst-web
========

A slightly modified version of MYST project to tweet over web when twitter is not accessible 

* Twitter is not available where I am right now, so I have created this small script that can be hosted on any server from where twitter can be accessed.
* A POST request to /tweet will tweet.
* A GET request to /timeline will fetch your timeline
* A GET request to /search with query supplied in variable "q" will get search results. Example: /search?q=fudcon

Requirements
------------

* pip install python-twitter
* Your twitter creds in the following format
```
[MYST]
consumer_key: <consumer_key>
consumer_secret: <consumer_secret>
access_token: <access_token>
access_token_secret: <access_token_secret>
```

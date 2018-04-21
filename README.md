# WhatchaNo?
Our vision is to motivate users that their privacy is worth protecting. The application's purpose is to enlighten the users on their digital footprint in terms of sentiment and location of their publicly shared information.

Local Development Setup
------
### Prerequisites
Install the below prerequisites on your development machine:
* Install Python 3
* Download and install pip [Installation guide](https://packaging.python.org/tutorials/installing-packages/)
* Back-end: Flask API [Installation guide](http://www.flaskapi.org/#installation)
* Setup Virtualenv for Python 3 [Download and setup virtualenv](https://packaging.python.org/tutorials/installing-packages/#optionally-create-a-virtual-environment)<br>
```
virtualenv -p python3 env
```


### Getting Started
1. Clone repository
2. Navigate to the back-end folder and download python dependencies<br>
```
pip3 install -r requirements.txt
```

### API Keys

Twitter and Microsoft Azure Face API keys are requires to run this app.

Face API
https://azure.microsoft.com/en-au/try/cognitive-services/?api=face-api

Twitter API

Once you have the keys, you're required to create the following:

```
touch flask_website/local_settings.py
```

```
vi flask_website/local_settings.py
```

```
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
AZURE_FACE_API_TOKEN = ''
```

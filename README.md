


## Installation

Clone / download this repo onto your local machine, for example on your Desktop. Then navigate there from the command line:

```sh
cd ~/Desktop/slack-pollster-py
```

## Setup

Create and/or activate a virtual environment:

```sh
conda create -n slack-env python=3.8
conda activate slack-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

Configure local ".env" file:

```sh
# credentials for a slack "bot" (xoxb) app
SLACK_SIGNING_SECRET="_____"
SLACK_BOT_TOKEN="_____
```

### Slack Setup

See: https://slack.dev/bolt-python/tutorial/getting-started


Create an app here: https://api.slack.com/apps. On the app's homepage you should see the credentials, to be set in the ".env" file (see setup step above).

Also, "Add Features and Functionality":

  + Enable Interactivity. Set the Request URL as something like "https://my-app.herokuapp.com/slack/callback/interactivity" (we'll need to create a flask app and deploy to heroku to listen to POST requests here).
  + Create a new Slash Command with a command of `/pollster` and a Request URL of something like "https://my-app.herokuapp.com/slack/callback/slash-commands/pollster".


Also setup additional bot token scopes via the Oauth settings page "chat:write" and "reactions:write". Then you'll see the "Bot User OAuth Token", and set it as the `SLACK_BOT_TOKEN` env var.


Oh maybe also "Event Subscriptions" Enable Events, with a Request URL of something like "https://my-app.herokuapp.com/slack/callback/events. EDIT: this actually pings the server (so need to revisit).

Also "Install the app into your Workspace".

## Usage

Run the app:

```sh
python app.py
```

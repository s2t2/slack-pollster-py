import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", default="3000"))
BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

def create_app():
    return App(token=BOT_TOKEN, signing_secret=SIGNING_SECRET)

if __name__ == "__main__":
    app = create_app()
    app.start(port=PORT)

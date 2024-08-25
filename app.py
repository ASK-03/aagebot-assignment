from flask import Flask
from Database import db

app = Flask(__name__)

db.init_db()

@app.route('/')
def home():
    return "Please go to the Telegram bot to get your unique link.<br><br>Click on <a href=\"https://web.telegram.org/a/#7535287425\">Bot Link</a> to talk to telegram bot"

@app.route('/link/<string:uuid>')
def link(uuid):
    telegram_id = db.get_telegram_id(uuid)
    if telegram_id:
        return f"The Telegram user ID associated with this link is: {telegram_id}"
    else:
        return "Invalid Link"

if __name__ == '__main__':
    app.run(debug=False)

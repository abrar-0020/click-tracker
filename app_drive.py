import os
import json
from flask import Flask, redirect, request
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

DATA_FILE = "clicks_drive.json"
SHORT_CODE = "drive123"

def load_db():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            SHORT_CODE: {
                "url": "https://drive.google.com/file/d/1C31u8gfpLHCiLBaTdBCoftF5pLCSAfzS/view?usp=sharing",
                "clicks": 0,
                "log": []
            }
        }

def save_db(db):
    with open(DATA_FILE, "w") as f:
        json.dump(db, f, indent=2)

@app.route('/')
def short_link():
    db = load_db()
    if SHORT_CODE in db:
        ist = timezone('Asia/Kolkata')
        now_ist = datetime.now(ist)
        db[SHORT_CODE]["clicks"] += 1
        db[SHORT_CODE]["log"].append({
            "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
            "time": now_ist.strftime("%d/%m/%Y, %I:%M %p")
        })
        save_db(db)
        return redirect(db[SHORT_CODE]["url"])
    return "Link not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)

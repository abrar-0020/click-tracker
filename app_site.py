from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "clicks_drive.json"  # Use the file that works correctly

def load_db():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route('/stats/<short_code>')
def stats(short_code):
    db = load_db()
    if short_code in db:
        return render_template("stats.html", code=short_code, data=db[short_code])
    return "No stats found for this link", 404

@app.route('/reset/<short_code>', methods=['POST'])
def reset(short_code):
    db = load_db()
    if short_code in db:
        db[short_code]["clicks"] = 0
        db[short_code]["log"] = []
        save_db(db)
        return redirect(f'/stats/{short_code}')
    return "Link not found", 404

# ✅ This route makes http://localhost:5002/ go to stats for drive123
@app.route('/')
def default_stats():
    return redirect('/stats/drive123')

if __name__ == '__main__':
    app.run(debug=True, port=5002)

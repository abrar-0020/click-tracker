# 📊 Click Tracker

A simple **Flask-based Click Tracker** that lets you:
- Shorten any URL
- Track how many times it was clicked
- View IP address and timestamp for every click
- Reset click count anytime

---

## 📂 Project Structure
```
click-tracker/
│
├── app_drive.py         # Short link & tracker for any link (Drive, YouTube, etc.)
├── app_site.py          # Displays stats directly with reset button
├── templates/
│   └── stats.html       # Template to display click statistics
├── clicks_drive.json    # Auto-generated: stores all click logs
├── requirements.txt     # Python dependencies (Flask, pytz)
└── README.md            # Project documentation
```

---

## 🚀 How It Works
1. The app uses a short code (e.g., `drive123`) linked to your URL.
2. Visiting `http://localhost:5001/drive123` redirects to the original link and logs the click.
3. Statistics can be viewed at `http://localhost:5001/stats/drive123`.
4. For the website tracker (`app_site.py`), just open `http://localhost:5002` to view stats.

---

## 🖥️ Local Usage
> This app runs locally, meaning **only you can access the short link and stats unless you deploy it online**.

### 🔹 **Steps to Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/abrar-0020/click-tracker.git
   cd click-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the apps:
   ```bash
   python app_drive.py      # Runs the tracker for links on port 5001
   python app_site.py       # Runs the stats UI with reset on port 5002
   ```

4. Open in browser:
   - Redirect & count: `http://localhost:5001/drive123`
   - Stats page: `http://localhost:5001/stats/drive123`
   - Website stats UI: `http://localhost:5002`

---

## 🌍 Sharing with Others
- The `localhost` URLs **only work on your machine**.  
- To share, you must **deploy it online** (e.g., Fly.io, Render, Replit).  
- After deployment, you'll get a public URL (e.g., `https://yourapp.fly.dev/drive123`) that anyone can use.

---

## 🛠 Features
- ✅ Works with any URL
- ✅ Tracks total clicks, IP & timestamp
- ✅ Reset button to clear stats
- ✅ JSON file stores click data persistently

---

## ✏️ How to Add Your Own Links
1. Open `app_drive.py`.
2. Inside the `db` dictionary, add a new short code:
   ```python
   db = {
       "drive123": {
           "url": "https://yourlink.com",
           "clicks": 0,
           "log": []
       },
       "myvideo": {
           "url": "https://youtube.com/yourvideo",
           "clicks": 0,
           "log": []
       }
   }
   ```
3. Restart the app, and access via `http://localhost:5001/myvideo`.

---

## 📌 Limitations
- Works locally unless deployed online.
- JSON storage is local and persistent until manually deleted or reset.

---

## 📄 License & Copyright
© 2025 **Abrar-0020**  
Licensed under the MIT License.  
Feel free to use and modify, but please give credit.

---

# 🔗 Click Tracker - Flask Project

A simple URL click tracker built with Flask. This project allows you to create short URLs and track the number of clicks along with timestamps and IP addresses. Includes separate apps for tracking Google Drive links and a personal website.

## 📂 Project Structure

```
click-tracker/
│
├── app_drive.py         # Tracks clicks on GDrive short link (port 5000)
├── app_site.py          # Displays stats and reset button for GDrive link (port 5002)
├── templates/
│   └── stats.html       # Shared HTML template to display click stats
├── clicks_drive.json    # Automatically created and updated with each click
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🚀 Features

- ✅ Click counting with timestamp
- ✅ Tracks IP address of the user
- ✅ Reset click count with a single click
- ✅ Displays stats in a clean HTML table
- ✅ Supports multiple short codes (e.g., `drive123`)
- ✅ Works locally on different ports for separation

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abrar-0020/click-tracker.git
cd click-tracker
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Apps

**Start the click tracker (GDrive link):**

```bash
python app_drive.py
# Runs on http://localhost:5001/
```

**Start the stats viewer:**

```bash
python app_site.py
# Runs on http://localhost:5002 (automatically shows stats for drive123)
```


## 🔄 Reset Clicks

Click the **Reset** button on the stats page to reset the click count to 0. This action also clears the click log from `clicks_drive.json`.

## 📋 Requirements

All Python dependencies are listed in `requirements.txt`:

```text
Flask
pytz
```

## 🛡️ License

```
© 2025 Abrar | abrar-0020

This project is open-source and free to use for personal and educational purposes.
Do not use for unethical data tracking or malicious purposes.
```

## 💡 Author

- GitHub: [abrar-0020](https://github.com/abrar-0020)

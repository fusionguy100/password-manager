# 🔐 Password Manager (Tkinter GUI)

A simple and secure password manager built with Python and Tkinter. This app allows you to:
- Generate strong random passwords
- Save login credentials securely in a local JSON file
- Search for saved credentials by website name
- Automatically copy generated passwords to your clipboard



## 📦 Features

### ✅ Password Generation
- Random mix of letters, symbols, and numbers
- Clipboard auto-copy for easy pasting

### ✅ Save Credentials
- Stores website, email/username, and password
- Saves to a `data.json` file using `json` module
- Creates the file if it doesn't exist

### ✅ Search Function
- Enter a website name to quickly find stored login info
- Displays email and password using a messagebox popup

---

## 🖥️ Tech Stack

- **Python 3**
- **Tkinter** (for the GUI)
- **pyperclip** (for clipboard copying)
- **json** (for saving/retrieving data)

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python installed.
3. Install `pyperclip` (if not already installed):
   ```bash
   pip install pyperclip

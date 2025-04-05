# Programming Diary 📝

A simple command-line diary application built with Python and SQLite. Users can write daily programming notes and view their entries.

## ⚙️ Requirements

- Python 3.x (no external dependencies required)

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the app:
   
```bash
python3 app.py
```

## 📌 Features

- Add a new diary entry (content + date)
- View all saved entries
- Automatically creates the database and table if not present

## 📂 Notes

- The database file `data.db` is stored in the `data/` directory.
- All entries are stored in a table called `entries` with columns `content` and `date`.

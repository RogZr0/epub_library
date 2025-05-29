# 📚 Epub Library

A sleek, minimalist EPUB library built with Python and Flask. It displays your books on a virtual shelf using cover images, and clicking a book opens it in your default EPUB reader (Okular).

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/RogZr0/epub_library.git
cd epub_library
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### 🪟 Windows

```bash
venv\Scripts\activate
```

#### 🐧 Linux/macOS

```bash
source venv/bin/activate
```

---

## 📦 Dependencies

Install the required Python packages:

```bash
pip install Flask Pillow ebooklib
```

- **Flask** – Lightweight backend framework  
- **Pillow** – Image processing for covers  
- **EbookLib** – EPUB metadata extraction  

---

## ▶️ Run the App

```bash
python app.py
```

The app will launch locally. Open your browser and visit:

```
http://localhost:5000
```

---

## 📁 Directory Structure

```
epub_library/
├── app.py
├── books/               # Your EPUB files go here
├── static/
│   └── covers/          # Extracted cover images
├── templates/
│   └── index.html       # Main UI
└── venv/                # Virtual environment
```

---

## 🖼️ Preview

A clean bookshelf interface with clickable cover thumbnails. Clicking a cover launches the book in your system’s default reader (e.g., Okular on KDE).

---

## 🛠️ Customization

- Update `BOOK_DIR` and `COVER_DIR` in `app.py` if you use a different structure.
- Add your CSS styles in `static/style.css`.
- To change default epub viewer - change `okular` in `open_book(filename)` function in app.py
```py
def open_book(filename):
    filepath = os.path.abspath(os.path.join(BOOK_DIR, filename))
    subprocess.Popen(['okular', filepath])
    return '', 204
```

---

## ✅ TODO

- [x] Upload new EPUBs via UI  
- [ ] Add search or filter functionality  

---

## 🧑‍💻 Author

**RogZr0**  
_“Arch btw.”_

---

## 📝 License

MIT License — use freely, contribute happily.

from flask import Flask, render_template, send_from_directory
from ebooklib import epub,ITEM_COVER
from PIL import Image
import os
import subprocess
from flask import request, redirect, url_for, flash


app = Flask(__name__)
BOOK_DIR = 'books'
COVER_DIR = 'static/covers'

os.makedirs(COVER_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {'epub'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_book():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            book_path = os.path.join(BOOK_DIR, file.filename)
            file.save(book_path)
            extract_cover(book_path)
            return redirect(url_for('index'))  # redirect to homepage or book list

    return '''
    <!doctype html>
    <title>Upload New Book</title>
    <h1>Upload new EPUB</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept=".epub">
      <input type=submit value=Upload>
    </form>
    '''

def extract_cover(book_path):
    book = epub.read_epub(book_path)
    cover_path = os.path.join(COVER_DIR, os.path.basename(book_path) + '.jpg')

    # Find the actual image file named cover.jpg (or similar)
    for item in book.get_items():
        if item.get_type() == ITEM_COVER and 'cover' in item.get_name().lower():
            with open(cover_path, 'wb') as f:
                f.write(item.get_content())
            return os.path.basename(cover_path)

    return 'default.jpg'

@app.route('/')
def index():
    books = []
    for filename in os.listdir(BOOK_DIR):
        if filename.endswith('.epub'):
            cover = f"{filename}.jpg"
            books.append({'title': filename, 'cover': cover})
    return render_template('index.html', books=books)

@app.route('/open/<filename>')
def open_book(filename):
    filepath = os.path.abspath(os.path.join(BOOK_DIR, filename))
    subprocess.Popen(['okular', filepath])
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

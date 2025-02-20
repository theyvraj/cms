from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(40)  
def is_database_initialized():
    try:
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error:
        return False

if not is_database_initialized():
    try:
        subprocess.run(["python", "init_db.py"], check=True)
        print("Database initialized successfully.")
    except subprocess.CalledProcessError:
        print("Error initializing database.")
else:
    print("Database already initialized.")
def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        secret_key = request.form['secret_key']
        SECRET_SIGNUP_KEY = 'PKQSTecJAHRFI76aEHgtp6ukwP5T7Xj8'
        if secret_key == SECRET_SIGNUP_KEY:
            conn = get_db_connection()
            try:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                flash('Signup successful! You can now log in.')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already exists!')
            finally:
                conn.close()
        else:
            flash('Invalid secret key!')

    return render_template('signup.html')






@app.route('/admin')
def admin():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('admin.html', posts=posts)

@app.route('/view_edit_post/<int:post_id>', methods=['GET', 'POST'])
def view_edit_post(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        date = request.form['date']
        
        conn.execute('UPDATE posts SET title = ?, content = ?, author = ?, date = ? WHERE post_id = ?',
                     (title, content, author, date, post_id))
        conn.commit()
        flash('Post updated successfully!')
        return redirect(url_for('admin'))
    
    post = conn.execute('SELECT * FROM posts WHERE post_id = ?', (post_id,)).fetchone()
    conn.close()
    
    if post is None:
        flash('Post not found!')
        return redirect(url_for('admin'))
    
    return render_template('view_edit_post.html', post=post)

@app.route('/filter', methods=['POST'])
def filter_posts():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    filter_author = request.form.get('filter_author', '')
    conn = get_db_connection()
    if filter_author:
        posts = conn.execute('SELECT * FROM posts WHERE author LIKE ?', ('%' + filter_author + '%',)).fetchall()
    else:
        posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('admin.html', posts=posts, filter_author=filter_author)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials')

    return render_template('login.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        date = request.form['date']

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content, author, date) VALUES (?, ?, ?, ?)',
                     (title, content, author, date))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    return render_template('create.html')

@app.route('/delete_posts', methods=('POST',))
def delete_posts():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    post_ids = request.form.getlist('post_ids')
    if post_ids:
        conn = get_db_connection()
        conn.executemany('DELETE FROM posts WHERE post_id = ?', [(post_id,) for post_id in post_ids])
        conn.commit()
        conn.close()
        flash('Selected posts have been deleted.')

    return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/blogs')
def blogs():
    conn = get_db_connection()
    posts = conn.execute('SELECT post_id, title, content, author, date FROM posts').fetchall()
    conn.close()
    return render_template('blogs.html', posts=posts)

@app.route('/blog_post/<int:post_id>')
def blog_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE post_id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        return "Post not found", 404
    return render_template('blog_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)    
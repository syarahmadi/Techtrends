import sqlite3
import logging
import sys
from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    global total_connection
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    total_connection +=1
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
total_connection=0
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     if post is None:
#       return render_template('404.html'), 404
#     else:
#       return render_template('post.html', post=post)
# Define the post route
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)

    if post is None:
        log_message = "Article not found"
        app.logger.error(log_message)
        return render_template('404.html'), 404
    else:
        log_message = f"{post['title']} Article retrieved"
        app.logger.info(log_message)
        return render_template('post.html', post=post)
# Define the About Us page

@app.route('/about')
def about():
    log_message = 'The about us page is retrieved.'
    app.logger.info(log_message)
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/healthz')
def healthcheck():
    response = app.response_class(
        response=json.dumps({
            "result": "OK - healthy"
        }),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Health status request successfull')
    return response

@app.route("/metrics")
def metrics():
    connection = get_db_connection()
    posts = connection.execute("SELECT COUNT(*) FROM posts").fetchall()

    response = app.response_class(
        response=json.dumps(
            {   "status":"success",
                "db_connection_count": total_connection,
                "post_count": len(posts)
            }
        ),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response


# # start the application on port 3111
# if __name__ == "__main__":
#     # Create a custom logger
#     logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
#
#     app.run(host='0.0.0.0', port='3111')


def configure_logging():
    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Configure the logger to write logs to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # Set the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger


# Rest of your code...

if __name__ == "__main__":
    logger = configure_logging()
    # app = Flask(__name__)
    app.run(host='0.0.0.0', port='3111')

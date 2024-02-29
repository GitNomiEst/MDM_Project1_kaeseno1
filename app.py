from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")  

from markupsafe import escape
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route("/sum")
def sum_even():
    # flask parameters with type and default
    n = request.args.get('n', default=1, type=int)
    # logic
    result = sum([x for x in range(n+1) if x % 2 == 0])
    # return result as json
    return jsonify(sum=result)
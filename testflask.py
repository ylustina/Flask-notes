from flask import Flask, request, render_template

app = Flask(__name__)


# routing or mapping - tying a URL on a site to a Python function
# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')  # root directory
def index():
    return 'Method used: %s' % request.method
# uses GET method, will need POST if user needs to submit info





@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'


@app.route('/info')
def info():
    return '<h2>Flask is great</h2>'


@app.route('/profile/<username>')
def profile(username):
    return 'Hello %s' % username


# for integers:
@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post ID: %s' % post_id




# starts the app
if __name__ == "__main__":
    app.run(debug=True)



# passing in __name__ helps it determine the root path.
# connecting all the pages to a Python function (routing/mapping)

# https://www.youtube.com/watch?v=t3yHNZhSXLE


















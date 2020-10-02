from flask import Flask, render_template, url_for
app = Flask(__name__)

tracks = [
    {
        'title': 'hwo we rock',
        'author': ['jay park', 'haon'],
        'album': 'red tape'

    }
]
@app.route('/')
def index():
    return render_template('index.html', songs = tracks)


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html', songs = tracks)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
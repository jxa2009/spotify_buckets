from flask import Flask, render_template, url_for, request,redirect
from bucket import *
from authorization import *
app = Flask(__name__)

tracks = [
    {
        'title': 'how we rock',
        'author': ['jay park', 'haon'],
        'album': 'red tape'

    }
]
a = auth()
si = sign_in()
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        

        a.generate_code_challenge()

        
        si.setCodeChallenge(a.getCodeChallenge())
        si.process_sign_in()
        return redirect(si.auth_uri)
        # try:
            # return redirect('/buckets')
    else:
        return render_template('login.html', songs = tracks)



# @app.route('/login', methods=['GET','POST'])
# def login():
#     return render_template('login.html', songs = tracks)

@app.route('/buckets', methods=['GET','POST'])
def bucket_page():
    if request.method == 'GET':
        print(request.url)
    return render_template('index.html', songs = tracks)

# Makes a post request using a code retrieved after redirecting to the authorization URI
def retrieveAccessToken(code):
    postBody = {
        "client_id": si.getClientID(),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri" si.getRedirectURI(),
        "code_verifier": a.getCodeVerifier(),
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='63248846791-mbbb1v38juj0r4eslrj07bors6bv1fcv.apps.googleusercontent.com',
    client_secret='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',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={'scope': 'email'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v1/userinfo',
    userinfo_compliance_fix=lambda userinfo: {'sub': userinfo['id']}
)

@app.route('/')
def index():
    if 'google_token' in session:
        resp = google.get('userinfo')
        return 'Logged in as: ' + resp.json()['email']
    return 'Not logged in'

@app.route('/login')
def login():
    return google.authorize_redirect(url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    token = google.authorize_access_token()
    if token is None:
        return 'Access denied'
    session['google_token'] = token
    resp = google.get('userinfo')
    return 'Logged in as: ' + resp.json()['email']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

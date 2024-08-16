from flask import Flask, request, render_template, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Generate CSRF token
def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(16)
    return session['_csrf_token']

# Validate CSRF token
def validate_csrf_token(token):
    return '_csrf_token' in session and session['_csrf_token'] == token

# Vulnerable endpoint that performs a state-changing action
@app.route("/update_profile", methods=['POST'])
def update_profile():
    if request.method == 'POST':
        # Validate CSRF token
        csrf_token = request.form.get('csrf_token')
        if not validate_csrf_token(csrf_token):
            return "CSRF Token Validation Failed", 403

        # Assume this is a vulnerable action that updates the user's profile
        # In a real-world scenario, this action would likely require authentication
        # and other validation checks to ensure it's performed by an authorized user
        new_name = request.form['new_name']
        # Perform the update action (e.g., update the user's name in a database)
        # For demonstration purposes, we'll just print the new name
        print("Updating profile with new name:", new_name)
        return "Profile updated successfully"

# Home page
@app.route("/")
def home():
    # Generate CSRF token
    csrf_token = generate_csrf_token()
    return render_template('task2.html', csrf_token=csrf_token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

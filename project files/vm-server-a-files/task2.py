from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Vulnerable endpoint that performs a state-changing action
@app.route("/update_profile", methods=['POST'])
def update_profile():
    if request.method == 'POST':
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
    return render_template('task2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


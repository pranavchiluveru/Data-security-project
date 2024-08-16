from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        user_input = request.form['user_input']
        sanitized_input = Markup.escape(user_input)  # Sanitize user input
        return "You entered: " + sanitized_input
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

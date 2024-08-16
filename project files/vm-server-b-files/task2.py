from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def serve_malicious_page():
    return render_template('task2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

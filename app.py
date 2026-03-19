from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Duck Creek"

if __name__ == "__main__":
    app.run()
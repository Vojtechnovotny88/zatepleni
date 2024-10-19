from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world! Tohle je moje první aplikace!"

if __name__ == "__main__":
    app.run(debug=True)

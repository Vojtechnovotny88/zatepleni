from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('print_offer.html')  # Změň na název tvého HTML souboru

if __name__ == '__main__':
    app.run(debug=True)

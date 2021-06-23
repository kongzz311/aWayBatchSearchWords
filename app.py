from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    result = request.form
    words = result['words']
    wordsList = words.split()
    print(wordsList)

    return render_template('index.html')


if __name__ == '__main__':
    # ui.run()
    app.run(debug=True)

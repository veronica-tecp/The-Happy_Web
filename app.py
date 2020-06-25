from flask import Flask
from flask import render_template
from flask import request
import model
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())


@app.route('/results', methods=["GET", "POST"])
def results():
    emotion = request.form["emotion"]
    # print(emotion)
    quote = model.get_quote(emotion)
    imageSrc = model.get_image(emotion)
    return render_template('results.html', quote=quote[0], quoteAuthor=quote[1], imgSrc=imageSrc)
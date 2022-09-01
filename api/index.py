import flask
from flask import request, jsonify
from random import choice
import os

app = flask.Flask(__name__)

quote = ["We just human, is a dirt whos given a life by god, Every Human Just Same and will die", "You can buy everything with money, but not happines", "Weeb anime has been broke your life, wheres your life path?", "Everyone has their own path, if that is a muslim, christian, or other we all just same", "If war never happened then the world is place with happiness", "I remember where my mom loves me, but she now gone."]


@app.route('/', methods=['GET'])
def home():
    return '<p> This are used for Quote API, Go to this domain again but add /quote </p>'

@app.route('/quote', methods=['GET'])
def sendquote():
    genquote = choice(quote)
    loadquote = {
            "author": "Ender", 
            "quote": genquote
    }
    return jsonify(loadquote)


app.run()

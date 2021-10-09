#-*- coding: utf-8 -*-
import os
from translate import Transliteration
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['*'])
transliteration = Transliteration()

@app.route('/', methods=['GET'])
def main():
  return jsonify({'메시지': '헬로우, 월드!'})

@app.route('/', methods=['POST'])
def transliterate():
  input = request.form['input']
  output = transliteration.run(input)
  learned = transliteration.is_learned(input)
  return jsonify({'input': input, 'output': output, 'learned': learned})

if __name__ == '__main__':
  app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

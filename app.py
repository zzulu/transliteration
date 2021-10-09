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
  if request.json:
    input = request.json.get('input', '')
    output = transliteration.run(input) if input else ''
    learned = transliteration.is_learned(input)
  else:
    input, output, learned = '', '', False
  return jsonify({'input': input, 'output': output, 'learned': learned})

if __name__ == '__main__':
  app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

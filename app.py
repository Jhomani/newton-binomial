from flask import Flask, render_template, send_from_directory, request
import json
from main import developBinomio

print(__name__)
app = Flask(__name__)

@app.post('/binomio')
def binomio():
  body = request.json

  jsonResult = developBinomio(
    body['pow'], 
    body['firstTerm'], 
    body['secTerm'], 
  )

  return jsonResult

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/static/<path:path>')
def statics(path):
  print(path)
  return send_from_directory('static', path)

if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, request
from flask_cors import CORS
from controllers.Central import Central

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello world'

@app.route('/central', methods=['GET'])
def getAll():
    return (Central.list())

@app.route('/central', methods=['POST'])
def insert():
    body =  request.json
    return (Central.insert(body))

@app.route('/central', methods=['DELETE'])
def delete():
    body = request.json
    return (Central.delete(body))



if __name__ == '__main__':
 app.run(port = 3000, debug=True)


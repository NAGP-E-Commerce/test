from flask import Flask,jsonify,request,render_template,copy_current_request_context
from flask_cors import CORS,cross_origin
import json
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

@app.route('/gettime' , methods=['GET'])
@cross_origin()
def return_time():
    value = str(time.time())
    return jsonify({"time": value})

@app.route('/test' , methods=['GET'])
@cross_origin()
def test():
    value = str(time.time())
    return jsonify({"value": "hello world ..this is test!!!!"})

@app.route('/test1' , methods=['GET'])
@cross_origin()
def test1():
    value = str(time.time())
    return jsonify({"value": "this is test!!!!!"})

app.run(port=5001,host='0.0.0.0',debug=True)
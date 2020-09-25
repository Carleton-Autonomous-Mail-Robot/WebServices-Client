from flask import Flask,request,jsonify
from client import Client

app = Flask(__name__)
client = Client()

@app.route('/inbox',methods=['GET','POST'])
def inbox():
	return client.recieve(request.get_json())
	


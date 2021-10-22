from flask import Flask
app = Flask(__name__)

@app.route("/")
def hallo_wereld():  
	return "Hallo, wereld"
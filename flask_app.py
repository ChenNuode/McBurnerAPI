
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'send your data to /sendmefood/'


c_dict = {1:""}

@app.route('/sendmefood/<foodids>', methods=["GET"])
def work(foodids):
	foodidlist = foodids.split(",")
	returnstring = ""
	for item in foodidlist:
		returnstring = returnstring + str(item) + "<br>"

	return str([("Running: 5 mph (12 min/mile)",30, (240,298,355))])

@app.route("/upload_data", methods = ['POST'])
def submit_food_data():
	return

if __name__ == "__main__":
    app.run(debug=True)

# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'


#c_dict = {1:""}

@app.route('/sendmefood/<foodids>', methods=["GET"])
def work(foodids):
	foodidlist = foodids.split(",")
	returnstring = ""
	for item in foodidlist:
		returnstring = returnstring + str(item) + "<br>"

  
	return returnstring


@app.route("/upload_data", methods = ['POST'])
def submit_food_data():
	return

if __name__ == "__main__":
    app.run(debug=True)
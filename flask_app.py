
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'send your data to /sendmefood/'

c_dict = {12: ("Fillet-of-fish",332), 78:("McSpicy",522), 78:("McChicken",385),78:("McChicken",385),68:("Big Mac",522),14:("Hashbrown",149)}

@app.route('/sendmefood/<foodids>', methods=["GET"])
def work(foodids):
	total_calories = 0

	foodidlist = foodids.split(",")
	returnstring = ""
	
	for item in foodidlist:
		total_calories += c_dict[int(item)][1]
	
	#total calories that need to burned

	print(str(total_calories))

	#exercises Excercises, number of mins of that exercise to do
	exercises = {"Push-ups":8.56,"Curl-ups":7.29,"Lunges":9.33,"Pull-ups":9.95}

	resultcount = []
	calorieleft = total_calories

	for i, item in enumerate(exercises):

		smallnum = calorieleft/(len(exercises) - i)

		numofreps = int(smallnum/exercises[item])
		calorieleft = calorieleft - exercises[item]*numofreps
		resultcount.append((item,numofreps))

	return str(resultcount)

if __name__ == "__main__":
    app.run(debug=True)
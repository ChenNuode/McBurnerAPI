
# A very simple Flask Hello World app for you to get started with...
import json
from flask import Flask
import random 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'send your data to /sendmefood/'

c_dict = {
	1: ("Fillet-of-fish",332),
	2: ("Double Fillet-of-fish",474),
	3: ("McSpicy",522),
	4: ("Double McSpicy",800),
	5: ("McChicken",385),
	6: ("Big Mac",522),
	7: ("Hashbrown",149),
	8:("Coca-Cola - Medium",213),
	9:("Sprite - Medium",233),
	10:("Orange Juice",184),
	11:("French Fries - Medium",346),
}

@app.route('/sendmefood/<foodids>', methods=["GET"])
def work(foodids):
	total_calories = 0

	foodidlist = foodids.split(",")
	returnstring = ""
	
	for item in foodidlist:
		total_calories += c_dict[int(item)][1]
	
	#total calories that need to burned

	print(str(total_calories))

	#exercises Excercises, num of calories burned doing the exercise in 1 min
	exercises = {"Push-ups":8.56/20,"Curl-ups":7.29/20,"Lunges":9.33/20,"Pull-ups":9.95/20,"Squats":0.32,"Running/km":70}
	#running {4:,5.2, 6.7,7.5,8.6,10,12, 14}

	resultcount = []
	calorieleft = total_calories

	for i, item in enumerate(exercises):

		smallnum = calorieleft/(len(exercises) - i)
		if item != "Running/km":
			numofreps = int(smallnum/exercises[item])
		else:
			numofreps = round(smallnum/exercises[item],3)

		calorieleft = calorieleft - exercises[item]*numofreps
		resultcount.append((item,numofreps))

	returneddict = {"workouts" : [resultcount,resultcount]}
	loaded_r = json.dumps(returneddict)

	return loaded_r


def generate_crap():
	foodidlist = random.sample(list(c_dict.values()),2)
	total_calories = 0

	mystr = ""
	for item in foodidlist:
		mystr += str(item[0]) + " || "
		total_calories += item[1]
	
	#total calories that need to burned

	print("bought",mystr,'total cal',str(total_calories))

	#exercises Excercises, num of calories burned doing the exercise in 1 min
	exercises = {"Push-ups":8.56/20,"Curl-ups":7.29/20,"Lunges":9.33/20,"Pull-ups":9.95/20,"Squats":0.32,"Running/km":70}
	#running {4:,5.2, 6.7,7.5,8.6,10,12, 14}

	resultcount = []
	calorieleft = total_calories

	for i, item in enumerate(exercises):

		smallnum = calorieleft/(len(exercises) - i)
		if item != "Running/km":
			numofreps = int(smallnum/exercises[item])
		else:
			numofreps = round(smallnum/exercises[item],3)

		calorieleft = calorieleft - exercises[item]*numofreps
		resultcount.append(item + " " + str(numofreps))
		finaldict = {"title":"", "data":resultcount}

	return finaldict,total_calories


@app.route('/sendmefood2/', methods=["GET"])
def work2():
	returneddict = {'returned_data':[]}
	for i in range(2):
		w1,tc1 = generate_crap()
		returneddict["returned_data"].append(w1)
		#returneddict["total_calories"].append(tc1)

	loaded_r = json.dumps(returneddict)

	return loaded_r




if __name__ == "__main__":
    app.run(debug=True)
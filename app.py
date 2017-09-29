from twilio.rest import Client
from csv_reader import CSV_reader
from main import match_algo
from flask import Flask, request, render_template
app = Flask(__name__)
 
account = "AC944e61af65b03b17801242f9b82b6f34"
token = "802fa929a1ae729f95b2622e6544f339"
client = Client(account, token)

USERS = []

def find_location_from_users(memberID):
	for user in USERS:
		if(user.name == memberID):
			return user.location
	return None

def find_user(memberID):
	for user in USERS:
		if(user.name == memberID):
			return user
	return None

def find_contact_of_user(memberID):
	for user in USERS:
		if(user.name == memberID):
			return user.number

	return None

def send_message(message):
	message = client.messages.create(to="+19143090430",
                           from_="+12019879174",
                           body=message)

@app.route("/", methods=['GET'])
def hello():
	memberID = request.args['memberID']

	dates = request.args['date']
	if(dates.find(", ") >= 0):
		dates = dates.split(", ")
	else:
		dates = [dates]

	startTime = request.args['startTime']
	if(startTime.find(", ") >= 0):
		startTime = startTime.split(", ")
	else:
		dates = [dates]

	endTime = request.args['endTime']
	if(endTime.find(", ") >= 0):
		endTime = endTime.split(", ")
	else:
		endTime = [endTime]

	numKids = request.args['numKids']

	paymentMax = request.args['paymentMax']

	location = find_location_from_users(memberID)

	# number = find_contact_of_user(memberID)
	# algoresult = match_algo(memberID, location, dates, startTime, endTime, numKids, paymentMax)
	algoresult = [
		['Mary', 0.923],
		['Sophia', 0.91],
		['Olivia', 0.91],
		['Emma', 0.91],
		['Isabelle', 0.91],
		['Madison', 0.89]
	]

	topusers = []

	i = 0
	while i < 5:
		u = find_user(algoresult[i][0])
		topusers.append([u.name, u.number, u.location, str(u.min_amt) + ' - ' + str(u.max_amt)])
		i += 1

	send_message(topusers)
	return render_template('result.html', topusers = topusers)

if __name__ == "__main__":
	cs = CSV_reader()
	cs.read_file()
	USERS = cs.users
	app.run()
from twilio.rest import Client
from csv_reader import CSV_reader
from flask import Flask, request, render_template
app = Flask(__name__)
 
account = "AC944e61af65b03b17801242f9b82b6f34"
token = "802fa929a1ae729f95b2622e6544f339"
client = Client(account, token)

USERS = []

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
	
	# number = find_contact_of_user(memberID)
	# send_message("blah blah")

	return render_template('output.html')

if __name__ == "__main__":
	cs = CSV_reader()
	cs.read_file()
	USERS = cs.users
	app.run()
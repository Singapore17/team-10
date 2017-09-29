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
			return user

	return None

@app.route("/", methods=['GET'])
def hello():
	# memberID = request.form['memberID']
	memberID = request.args['memberID']
	# date = request.form['date'] (array)
	# startTime = request.form['startTime'] (array)
	# endTime = request.form['endTime'] (array)
	numKids = request.args['numKids']
	# paymentMax = request.form['paymentMax']

	print(find_contact_of_user('Mary'))

	return render_template('output.html')

if __name__ == "__main__":
	cs = CSV_reader()
	cs.read_file()
	USERS = cs.users
	app.run()
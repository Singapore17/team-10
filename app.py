from flask import Flask, request
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello():
	memberID = request.form['memberID']
	date = request.form['date']

	print(date)

	print(memberID)

	return "Hello World!"
 
if __name__ == "__main__":
    app.run()
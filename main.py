# import address algo part
from address import address
from csv_reader import *
from numOfKids import *
from payment import *
from timeMatching import *
from operator import itemgetter
import datetime
# import time from time.py(LATER)

# import time algo part

# import pay algo part

# import read csv method

def match_algo(nric, req_location, date, startTime, endTime, req_num_kids, req_pay_amt):


	score = 0

	cs = CSV_reader()
	cs.read_file()
	weighted_users = []
	time_date = {}
	# print(date)
	# print(cs.users)
	# print("hello")
	for i in range(len(date)):
		current_date = date[i].split('-')
		int_date = map(int, current_date)
		day_of_week = str(datetime.date(int_date[0], int_date[1], int_date[2]).weekday() + 1)
		duration = startTime[i] + '-' + endTime[i] 

		
		if (day_of_week) in time_date.keys():
			time_date[day_of_week].append(duration)
		else:
			time_date[day_of_week] = []
			time_date[day_of_week].append(duration)
	for u in cs.users:
		if (u.id == nric):
			continue
		num_kids = numOfKids(req_num_kids, u.n_kids)
		pay_amt = payment(req_pay_amt, u.min_amt)
		# print(time_date)
		# print(u.time_available)
		time_matched = timeMatching(time_date, u.time_available)
		distance = address(u.location, req_location)

		if (time_matched==0 | num_kids==0):
			continue
		
		score = 0.5*float(time_matched) + 0.3*float(distance) + 0.2*float(pay_amt)
		weighted_users.append([u.id, score])

	sorted_weighted_users = sorted(weighted_users, key=itemgetter(1), reverse=True)
	print(sorted_weighted_users) 

def main():
	date_arr = ["2012-03-10", "2012-04-10"]
	startTime_arr = ["09.30", "10.30"]
	endTime_arr = ["16.30", "14.00"]
	match_algo("S1234567G", "600000", date_arr, startTime_arr, endTime_arr, 2, 5)
	
if __name__ == '__main__':
	main()
	
	# address val * address weightage
	# address_val = address(550147, 822104)

	# time val * address weightage

	# pay val * pay weightage



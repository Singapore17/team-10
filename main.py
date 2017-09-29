# import address algo part
from address import address
from csv_reader import *
from numOfKids import *
from payment import *
# import time from time.py(LATER)

# import time algo part

# import pay algo part

# import read csv method

def match_algo(nric, date, startTime, endTime, req_num_kids, req_pay_amt, users):

	cs = CSV_reader()
	cs.read_file()
	weighted_users = []
	for(u in users):
		if (u.id == nric):
			continue
		num_kids = numOfKids(num_req_kids, users.n_kids)
		pay_amt = payment(req_pay_amt, users.min_amt)
		time_date = {}
		for i in len(date):
			current_date = date[i].split('-')
			int_date = map(int, current_date)
			day_of_week = date(int_date[0], int_date[1], int_date[2]).weekday() + 1
			duration = startTime[i] + '-' + endTime[i] 

			
			if (day_of_week) in time_date.keys():
				time_available[day_of_week].append(duration)
			else:
				time_available[day_of_week] = []
				time_available[iday_of_week].append(duration)



		time = time() 


	# address val * address weightage
	# address_val = address(550147, 822104)

	# time val * address weightage

	# pay val * pay weightage



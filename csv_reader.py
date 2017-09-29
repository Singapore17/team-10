import csv
from decimal import Decimal

class CSV_reader:
    users = []
    class User:
        def __init__ (self, name, number, time_available, location, min_amt, max_amt, n_kids):
            self.name = name
            self.number = number
            self.location = location
            self.time_available = time_available
            self.min_amt = min_amt
            self.max_amt = max_amt
            self.n_kids = n_kids

    def read_file(self):
        file_name = 'codeforgood.csv'
        firstline = True
        with open(file_name, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if firstline:
                    firstline = False
                    continue
                name = row[0]
                number = row[1]
                time_available = {}
                time_list = row[2].split(',')
                #print(time_list)
                for n in time_list:
                    # if not n:
                        n_dict = n.split(':')
                        #print(n_dict)
                        if int(n_dict[0]) in time_available.keys():
                            time_available[int(n_dict[0])].append(n_dict[1])
                        else:
                            time_available[int(n_dict[0])] = []
                            time_available[int(n_dict[0])].append(n_dict[1])
                # print(time_available)
                location = row[3]
                min_amt = Decimal(row[4])
                max_amt = Decimal(row[5])
                n_kids = int(row[6])
                self.users.append(self.User(name,number,time_available,location,min_amt,max_amt,n_kids))

cs = CSV_reader()
cs.read_file()
for u in cs.users:
    print(u.name)
    print(u.number)
    print(u.location)
    print(u.time_available)
    print(u.min_amt)
    print(u.max_amt)
    print(u.n_kids)





import csv
from decimal import Decimal

class CSV_reader:
    users = []
    class User:
        def __init__ (self, id, name, number, time_available, location, min_amt, max_amt, n_kids):
            self.id = id
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
                id = row[0]
                name = row[1]
                number = row[2]
                time_available = {}
                time_list = row[3].split(',')
                #print(time_list)
                for n in time_list:
                    # if not n:
                        # print(n)
                        n_dict = n.split(':')
                        # print(n_dict)
                        if int(n_dict[0]) in time_available.keys():
                            time_available[int(n_dict[0])].append(n_dict[1])
                        else:
                            time_available[int(n_dict[0])] = []
                            time_available[int(n_dict[0])].append(n_dict[1])
                # print(time_available)
                location = row[4]
                min_amt = Decimal(row[5])
                max_amt = Decimal(row[6])
                n_kids = int(row[7])
                self.users.append(self.User(id,name,number,time_available,location,min_amt,max_amt,n_kids))

cs = CSV_reader()
cs.read_file()
# for u in cs.users:
#     print(u.name)
#     print(u.number)
#     print(u.location)
#     print(u.time_available)
#     print(u.min_amt)
#     print(u.max_amt)
#     print(u.n_kids)





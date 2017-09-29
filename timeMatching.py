def timeMatching(request, provider):
		
		# Check day coincides
		requestList = list(request.keys())
		nDays = len(request)
		maxWeight = 100
		weightPerDay = maxWeight/nDays
		currentWeight = maxWeight

		for x in range(0, nDays):
			if requestList[x] not in provider.keys():
				#Person B cannot provide on that particular day
				currentWeight -= weightPerDay
				continue;
			else:
				#Person B can provide on that particular day --> Check time slot
				#Get request: [["9.30-15.30"],["17.00-19.30"]]
				#Get provider: [["11.30-16.30"],["18.00-20.00"]]
				timingRequest = request.get(requestList[x])
				timingProvider = provider.get(requestList[x])
				#For each time slot, parse and convert to number.
				#Create new list to store

				timingRequestNum = [];
				timingProviderNum = [];
				totalTime = [];
				for y in range(0, len(timingRequest)):
					
					totalTime.append(0)
					timingRequestNumIndiv = timingRequest[y].split("-")
					timingRequestNumIndiv[0] = timingRequestNumIndiv[0].replace('30','50')
					timingRequestNumIndiv[1] = timingRequestNumIndiv[1].replace('30','50')
					timeIndivRequestEnd = float(timingRequestNumIndiv[1])
					timeIndivRequestStart = float(timingRequestNumIndiv[0])
					timeIndiv = timeIndivRequestEnd - timeIndivRequestStart
					totalTime[y] += timeIndiv
					timingRequestNum.append(timingRequestNumIndiv)
					weightPerHour = weightPerDay/totalTime[y]

					fulfilledTime = 0
					toCont = 1

					while (toCont == 1):
						for z in range(0, len(timingProvider)):

							timingProviderNumIndiv = timingProvider[z].split("-")
							timingProviderNumIndiv[0] = timingProviderNumIndiv[0].replace('30','50')
							timingProviderNumIndiv[1] = timingProviderNumIndiv[1].replace('30','50')
							timeIndivProviderEnd = float(timingProviderNumIndiv[1])
							timeIndivProviderStart = float(timingProviderNumIndiv[0])

							if timeIndivRequestStart >= timeIndivProviderStart and timeIndivRequestEnd <= timeIndivProviderEnd:
								fulfilledTime = 0;
								toCont = 0
								continue
							elif timeIndivRequestEnd < timeIndivProviderStart:
								continue
							elif timeIndivRequestStart > timeIndivProviderEnd:
								fulfilledTime = -totalTime[y]
								toCont = 0
								continue
							else:
								if timeIndivRequestStart < timeIndivProviderStart:
									fulfilledTime -= timeIndivProviderStart - timeIndivRequestStart
								if timeIndivRequestEnd > timeIndivProviderEnd:
									fulfilledTime -= timeIndivRequestEnd - timeIndivProviderEnd
								if timeIndivRequestStart <= timeIndivProviderStart and timeIndivRequestEnd >= timeIndivProviderEnd:
									toCont = 0
									continue
							
					# End of calculating fulfilled time
					fulfilledTime += totalTime[y]
					hoursNotFulfilled = totalTime[y] - fulfilledTime
					currentWeight -= weightPerHour * hoursNotFulfilled

		print(currentWeight)





def main():
	#Data structure of timing: Hashmap/Dictionary {int day : list of list}
	#1: [["9.30-15.30"],["17.00-19.30"]]

	a = {'1':["9.30-12.30","13.00-19.30"],'2':["9.30-15.30","17.00-19.30"]}
	b = {'1':["10.30-11.30","20.00-23.30"],'2':["9.30-15.30","17.00-19.30"]}
	timeMatching(a,b)

if __name__ == '__main__':
    main()

def timeMatching(request, provider):
		print(request)
		print(type(request))
		print(provider)
		print(type(provider))
		
		# Check day coincides
		requestList = list(request.keys())
		nDays = len(request)
		maxWeight = 100
		weightPerDay = maxWeight/nDays
		currentWeight = maxWeight
		timeCount = [];

		for x in range(0, nDays):
			timeCount.append(0)
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

				for n in range(0, len(timingRequest)):
					timingRequestNumIndiv = timingRequest[n].split("-")
					timingRequestNumIndiv[0] = timingRequestNumIndiv[0].replace('30','50')
					timingRequestNumIndiv[1] = timingRequestNumIndiv[1].replace('30','50')
					timeIndivRequestEnd = float(timingRequestNumIndiv[1])
					timeIndivRequestStart = float(timingRequestNumIndiv[0])
					timeIndiv = timeIndivRequestEnd - timeIndivRequestStart
					timeCount[x] += timeIndiv
					timingRequestNum.append(timingRequestNumIndiv)

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

					
					for z in range(0, len(timingProvider)):
						while (toCont == 1):
							# print(z)

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
					currentWeight -= weightPerDay/ timeCount[x] * hoursNotFulfilled
		print(currentWeight)
		return(currentWeight)


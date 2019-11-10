
class Match:

	def match(self,mentee,mentors):
		sortedMentors=[]
		keys=['ethnicity','gender','career','degree','location']
		matchList=[]
		for mentor in mentors:
			simIndex=0
			if mentor==mentee.keys()[0]:
				continue
			for key in keys:
				if (key=='location' and mentor['location']['state']==mentee['location']['state']):
					simIndex+=1	
				elif (mentor[key]==mentee[key]):
					simIndex+=1

			matchList.append([simIndex,mentor])
		print (matchList)
		matchList.sort(reverse=True, key=lambda x: x[0])

		for match in matchList:
			sortedMentors.append(match[1]['email'])

		return sortedMentors


			


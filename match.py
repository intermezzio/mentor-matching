
class Match:

	def match(self,mentee,mentors):
		sortedMentors=[]
		keys=['ethnicity','gender','position','degree','state']
		matchList=[]
		for mentor in mentors:
			simIndex=0
			if mentor['email']==mentee['email']:
				continue
			for key in keys:
				
				if (mentor[key]==mentee[key]):
					simIndex+=1

			matchList.append([simIndex,mentor])

		matchList.sort(reverse=True, key=lambda x: x[0])

		for match in matchList:
			sortedMentors.append(match[1]['email'])

		return sortedMentors


			


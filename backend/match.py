
mentee={
'id':'mentor1',
 'cred':{
'username': 'eflores',
'password':'123456',
},
'firstname': 'Emilia',
'lastname': 'Flores',
'email': 'eflores@gmail.com',
'school': 'Princeton University',
'hobbies':'Baseball',
'company': 'Microsoft',

'ethnicity': 'African American',
'gender': 'Female',
'career': 'Software Engineer',
'degree': 'Mechanical Aerospace Engineer',
'location': {
    'city': 'New York City',
    'state': 'New York'
},
	'ismentor': False,
	'ismentee': True

}
mentors=[{
'id':'mentor1',
'username': 'jdoe',
'password':'123456',

'firstname': 'Joanna',
'lastname': 'Doe',
'email': 'jdoe@gmail.com',
'school': 'Princeton University',
'hobbies':'Volleyball, Tennis, League of Legends',
'company': 'Facebook',

'ethnicity': 'African American',
'gender': 'Female',
'career': 'Software Engineer',
'degree': 'Computer Science',
'location': {
    'city': 'New York City',
    'state': 'New York'
},
	'ismentor': True,
	'ismentee': False
},
{
'id':'mentor2',
'username': 'jgonzalez',
'password':'123456',
'firstname': 'Juan',
'lastname': 'Gonzalez',
'email': 'bsmith@gmail.com',
'school': 'Olin University',
'hobbies':'Soccer, Fishing, Anime',
'company': 'iCIMS',

'ethnicity': 'Hispanic',
'gender': 'Female',
'career': 'Data Science',
'degree': 'Statistics',
'location': {
    'city': 'San Jose',
    'state': 'California'
},
	'ismentor': True,
	'ismentee': False
}

]

sortedList={}
matchList={}
keys=['ethnicity','gender','career','degree']

for mentor in mentors:
	simIndex=0
	if mentor==mentee.keys()[0]:
		continue
	for key in keys:
		if (mentor[key]==mentee[key]):
			simIndex+=1

	matchList[simIndex]=mentor['firstname']

print (matchList)

sk= sorted(matchList,reverse=True)
print(sk)
for k in sk:
	sortedList[k]=matchList[k]
print(sortedList)
	


			


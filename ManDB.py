import pymongo
import urllib
import copy

class ManDB:
	"""
	Creating Users
	Updating + Reading Users' Data
	Logging In

	"""
	login_private_key = open("keys/login-db.txt", "r").read().strip()

	def __init__(self, user="andrew", password=None):
		self.client = pymongo.MongoClient(f"mongodb+srv://{user}:{password or open('keys/loginpass.txt').read().strip()}@cluster0-codlf.mongodb.net/test?retryWrites=true&w=majority")
		# self.client = pymongo.MongoClient()
		self.user = user
		self.loginDB = self.client["users"]
		# self.loginDB.authenticate('amascillaro@gmail.com', open('keys/personal_mongodb_pass.txt').read())
		self.loginCol = self.loginDB["login-info"]
	
	def createUser(self, password, firstname, lastname, email, bio="", school=None, birthdate=0, hobbies=list(), company=None, ethnicity=None, gender=None, position="Lead Systems Engineer", degree="", city="Princeton", state="NJ", ismentor=False, ismentee=False, mentoravailability=False, menteeavailability=False):
		emailSearchCursor = self.loginCol.find({"email": email})
		foundUsers = [user for user in emailSearchCursor]
		if foundUsers:
			raise Exception("That email address is already taken")
		userProfile = {
			"password": password,
			"firstname": firstname,
			"lastname": lastname,
			"email": email,
			"bio": bio,
			"school": school,
			"birthdate": birthdate,
			"hobbies": hobbies,
			"company": company,
			"ethnicity": ethnicity,
			"gender": gender,
			"position": position,
			"degree": degree,
			"city": city,
			"state": state,
			"ismentor": ismentor,
			"ismentee": ismentee,
			"mentoravailability": mentoravailability,
			"menteeavailability": menteeavailability
		}
		self.loginCol.insert_one(userProfile)

	def login(self, email, password):
		get_user = self.loginCol.find_one({"email": email, "password": password})
		
		if get_user:
			return email
		
		raise Exception("Invalid logon attempt")

	def accessData(self, email):
		get_user = self.loginCol.find_one({"email": email})
		if get_user:
			return get_user
		
		raise Exception("This user does not exist")

	def updateData(self, password=None, firstname=None, lastname=None, email=None, bio=None, school=None, birthdate=None, hobbies=None, company=None, ethnicity=None, gender=None, position=None, degree=None, city=None, state=None, ismentor=None, ismentee=None, mentoravailability=None, menteeavailability=None):
		args = locals()
		
		self.accessData(email)
		
		newargs = dict()
		for key, value in args.items():
			if value is not None and key is not "self":
				newargs[key] = value
		print(newargs)
		
		print(self.loginCol.update_one(
			{"email": email},
			{"$set": newargs}
		))

		return 0

	def deleteUser(self, email):
		self.accessData(email)
		
		self.loginCol.delete_one({"email": email})

		return 0


if __name__ == "__main__":
	m = ManDB()
	mentee={
		'password':'123456',
		'firstname': 'Emilia',
		'lastname': 'Flores',
		'email': 'eflores@gmail.com',
		'school': 'Princeton University',
		'hobbies':'Baseball',
		'company': 'Microsoft',

		'bio': 'I have been a software engineer for many years now, and I love it!',
		'birthdate': "02/12/1985",
		'ethnicity': 'African American',
		'gender': 'Female',
		'position': 'Software Engineer',
		'degree': 'Mechanical Aerospace Engineer',
		'city': 'New York City',
		'state': 'New York',
		'ismentor': False,
		'ismentee': True,
		'mentoravailability': False,
		'menteeavailability': True
	}


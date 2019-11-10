import pymongo
import urllib

class ManDB:
	"""
	Creating Users
	Updating + Reading Users' Data
	Logging In

	"""
	login_private_key = open("keys/login-db.txt", "r").read().strip()

	def __init__(self, user="andrew", password=None):
		self.client = pymongo.MongoClient(f"mongodb+srv://{user}:{password or open('keys/loginpass.txt').read()}@cluster0-codlf.mongodb.net/test?retryWrites=true&w=majority")
		self.user = user
		self.loginDB = self.client["users"]
		self.loginDB.authenticate('amascillaro@gmail.com', open('keys/personal_mongodb_pass.txt').read())
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
			"location": {
				"city": city,
				"state": state
			},
			"ismentor": ismentor,
			"ismentee": ismentee,
			"mentoravailability": mentoravailability,
			"menteeavailability": menteeavailability
		}
		self.client.insert_one(userProfile)

	def login(self, email, password):
		get_user = self.loginCol.find({"credentials": {"email": email, "password": password}})
		if get_user:
			return email
		else:
			raise Exception("Invalid logon attempt")

	def accessData(self, email):
		get_user = self.loginCol.find_one({"credentials": {"email": email}})
		if get_user:
			return get_user
		else:
			raise Exception("Who are you, really?")
 
		return get_user

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

		'ethnicity': 'African American',
		'gender': 'Female',
		'position': 'Software Engineer',
		'degree': 'Mechanical Aerospace Engineer',
		'city': 'New York City',
		'state': 'New York',
		'ismentor': False,
		'ismentee': True
	}


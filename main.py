import re
import os
import numpy as np
import pandas as pd
import requests
from ManDB import ManDB

user_db = ManDB()

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Response, send_file, jsonify
# from flask.ext.session import Session

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '124ed87acnjkhna87ed'
SESSION_TYPE="redis"
# Session(app)

@app.route("/", methods=["GET", "POST"])
def indexPage():
	return render_template("landingpage.html")


@app.route("/index.html", methods=["GET", "POST"])
def alsoIndexPage():
	return render_template("landingpage.html")

@app.route("/auth.html", methods=["GET", "POST"])
def authenticate():
	req = request.form
	print(req)
	try:
		print(1)
		email = req["email"]
		print(2)
		password = req["password"]
		print(3)
	except KeyError as e:
		error_msg = "Please input a valid email and password"
		print(error_msg)
		print(e)
		return redirect("/signin.html")
	print(email)
	print(password)
	try:
		email_addr = user_db.login(email, password)
		print("email:", email_addr)
	except Exception as e:
		error_msg = e
		print(e)
		return redirect("/signin.html")

	if email_addr:
		session["email"] = email_addr

	return render_template("dashboardmatching.html")	

@app.route("/signin.html", methods=["GET", "POST"])
def loginAuth(error_msg=""):
	print("start signin")
	if request.method == "POST":
		req = request.form

		try:
			email, password = req["email"], req["password"]
		except KeyError:
			error_msg = "Please input a valid email and password"
			return redirect("/signin.html", error_msg=error_msg)

		try:
			email_addr = user_db.login()
			print("email:", email_addr)
		except Exception as e:
			error_msg = e
			print(e)
			return redirect("/signin.html", error_msg=error_msg)

		if email_addr:
			session["email"] = email_addr

			return render_template("dashboardmatching.html")
	else:
		print('ha!')
	return render_template("signin.html", error_msg=error_msg)

@app.route("/signout.html")
def signOut():
	session['email'] = ''
	return redirect("/")

@app.route("/registerme.html", methods=["GET", "POST"])
def registerMe():
	if request.method == "POST":
		req = request.form

		if user_db.createUser(**req) == 0:
			session["email"] = req["email"]
		return redirect("/dashboardmatching.html")


@app.route("/dashboardmatching.html")
def dashboardMatching():
	return render_template("dashboardmatching.html")

@app.route("/profile.json", methods=["POST"])
def retProfile():
	"""
	create static site with this boi
	"""
	req = request.form

@app.route("/registerpage.html")
def registerKELLY():
	return render_template("registerpage.html")


@app.route("/profile/str:profname")
def getProfile(profname):
	pass

@app.route("/profile/str:profname/info.json")
def accessProfileJSON(profname):
	pass

if __name__ == "__main__":
	app.run(debug=True, port=2727)
import re
import os
import numpy as np
import pandas as pd
import requests
from ManDB import ManDB

user_db = ManDB()

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Response, send_file, jsonify
from flask.ext.session import Session

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '124ed87acnjkhna87ed'
SESSION_TYPE="redis"
Session(app)

@app.route("/", methods=["GET", "POST"])
def indexPage():
	return render_template("index.html")


@app.route("/index.html", methods=["GET", "POST"])
def alsoIndexPage():
	return render_template("index.html")

@app.route("/login.html", methods=["GET", "POST"])
def loginAuth(error_msg=""):
	if request.method == "POST":
		req = request.form

		try:
			email, password = req["email"], req["password"]
		except KeyError:
			error_msg = "Please input a valid email and password"
			return redirect("/login.html", error_msg=error_msg)

		try:
			email_addr = user_db.login()
		except Exception as e:
			error_msg = e
			return redirect("/login.html", error_msg=error_msg)

		if(email_addr):
			session["email"] = email_addr

	return render_template("login.html", error_msg=error_msg)

# def

@app.route("/profile.json", methods=["POST"])
def retProfile():
	"""
	create static site with this boi
	"""
	req = request.form


@app.route("/profile/str:profname")
def getProfile(profname):
	pass

@app.route("/profile/str:profname/info.json")
def accessProfileJSON(profname):
	pass

if __name__ == "__main__":
	app.run(debug=True, port=2727)
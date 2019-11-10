import re
import os
import numpy as np
import pandas as pd
import requests
from ManDB import ManDB
# from timeit import timeit
# from time import sleep
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from xml.etree import ElementTree
# from multiprocessing import Process
# from sympy import solveset, Eq, symbols
import datetime

user_db = ManDB()

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Response, send_file
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '124ed87acnjkhna87ed'

@app.route("/", methods=["GET", "POST"])
def indexPage():
	return render_template("index.html")


@app.route("/index.html", methods=["GET", "POST"])
def alsoIndexPage():
	return render_template("index.html")

@app.route("/login.html", methods=["GET", "POST"])
def loginAuth():
	if request.method == "POST":
		req = request.form

		try:
			email, password = req["email"], req["password"]
		except KeyError:
			error_msg = "Please input a valid email and password"
			return redirect("smth.html", error_msg=error_msg)
	

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
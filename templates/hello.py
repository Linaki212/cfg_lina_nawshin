from flask import Flask, render_template, request
import requests
app = Flask("MyApp")

def send_simple_message(email):
    return 'bla'

@app.route("/")
def hello():
	return "Hi"

@app.route("/<name>")
def hello_someone(name):

	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	email = form_data["email"]
	send_simple_message(email)
	return "Email Sent to: {}".format(email)
app.run(debug=True)


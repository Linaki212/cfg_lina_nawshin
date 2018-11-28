from flask import Flask, render_template, request
import requests
app = Flask("MyApp")

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd834653d14c84cd7945e1502411e43b2.mailgun.org/messages",
        auth=("api", "3a9fd2de4a899477c74ebd700570a71e-4412457b-c1b04314"),
        data={"from": "Excited User <mailgun@sandboxd834653d14c84cd7945e1502411e43b2.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

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


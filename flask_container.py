from flask import Flask, request, render_template
import os
import configuration
import time


app = Flask(__name__)


@app.route("/")
def splash_screen():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def post_new_credentails():
    network = request.form['network']
    credentials = request.form['credentials']

    configuration.run(net=network, cred=credentials)
    submission_splash()
    time.sleep(5)
    os.system("reboot")

    return render_template("submission_form.html")


def submission_splash():
    print("in the splash zone! ;)")
    return render_template("submission_form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

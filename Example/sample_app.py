#!/usr/bin/env python3

# This is a Example application that demonstrates how it is possible to use the 365id WEB Id Verification SDK
#
# It imports the License Key i.e Client Id and Client Secret from the file credentials.py
# It uses the crentials to get an access token that then is used to start the WEB SDK.
#
# The way the server is set up you shall be able to access the python web server using the URL http://localhost:5001

from flask import Flask, render_template, json, send_from_directory
from pathlib import Path
import requests

from credentials import client_id, client_secret, access_token_url


payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "allowed_origin": "*://localhost/*",
    "transfer_device_domain_url": "http://localhost:5001/transfer_to_second_device"
}

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

app = Flask(__name__, static_folder="static")

# Defines the path to where the node modules are kept
NODE_MODULES = Path(__file__).parent / "node_modules"

# Defines where the SDK dist folder is located
DIST_ROOT = NODE_MODULES / "@365id" / "id-verification" / "dist"

@app.route("/vendor/<path:filepath>")
def vendor(filepath: str):
    target_root = DIST_ROOT
    return send_from_directory(target_root, filepath, conditional=True)

# Defines where the public files have been placed
PUBLIC_ROOT = NODE_MODULES / "@365id" / "id-verification" / "dist" / "public"
@app.route("/public/<path:filepath>")
def public(filepath: str):
    target_root = PUBLIC_ROOT
    return send_from_directory(target_root, filepath, conditional=True)

# The root folder on the webserver for the SDK.
@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/idverification")
def base():

    # Make the POST request to get the access token
    response = requests.post(access_token_url,
                         data=json.dumps(payload),
                         headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Access token received:")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
        return {"error": response.text}, 400

    access_token = response.json()["access_token"]
    print(access_token)

    return render_template(
        "idverification.html",
        app_token=access_token
    )

@app.route("/error")
def error():
    return render_template(
        "error.html"
    )

@app.route("/secondary_device")
def secondary_device():
    return render_template(
        "secondary_device.html"
    )

@app.route("/completed")
def completed():
    return render_template(
        "completed.html"
    )

@app.route("/user_pressed_cancel")
def user_pressed_cancel():
    return render_template(
        "canceled.html"
    )

@app.route("/transfer_to_second_device")
def transfer_to_second_device():
    return render_template(
        "second_device.html"
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

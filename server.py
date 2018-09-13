from flask import Flask, request
import json
import os
from openapi_core import create_spec
from openapi_core.shortcuts import RequestValidator
from openapi_core.wrappers.flask import FlaskOpenAPIRequest
from pprint import pprint

app = Flask(__name__)

with open(f"{os.path.dirname(os.path.abspath(__file__))}/openapi.json") as f:
    openapi_file = json.load(f)


spec = create_spec(openapi_file)
validator = RequestValidator(spec)


@app.before_request
def validate():
    openapi_request = FlaskOpenAPIRequest(request)
    result = validator.validate(openapi_request)

    if result.errors:
        pprint(result.errors)


@app.route("/cars", methods=["POST"])
def new_car():
    # creating new car:
    pprint(request.json)
    return "created"


app.run(port=8080)

import uuid
from flask import Flask

app = Flask(__name__)


@app.route("/register")
def register():
    return str(uuid.uuid1())

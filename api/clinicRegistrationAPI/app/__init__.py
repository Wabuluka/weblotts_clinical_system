from flask import Flask

app = Flask(__name__)

from app.routes.view import route_url
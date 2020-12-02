from typing import Any

from flask import Flask


def create_app(config_object="application.settings"):
	app = Flask(__name__.split(".")[0])
	app.config.from_object(config_object)
	return app

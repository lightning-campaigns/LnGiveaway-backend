from flask import Flask

import os

from application_configs import ApplicationConstant
from route.campaign_route import campaign_route

app = Flask(__name__)

app.register_blueprint(campaign_route, url_prefix="/campaign")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=ApplicationConstant.port)

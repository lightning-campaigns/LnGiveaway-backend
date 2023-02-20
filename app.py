from flask import Flask
from flask_migrate import Migrate
from api.helper.db import db


from api.helper.application_configs import ApplicationConstant
from api.route.campaign_route import campaign_route

app = Flask(__name__)
# app.config.from_pyfile('api/helper/database_config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = ApplicationConstant.sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = ApplicationConstant.sqlalchemy_track_modifications

db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(campaign_route, url_prefix="/campaign")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=ApplicationConstant.port)



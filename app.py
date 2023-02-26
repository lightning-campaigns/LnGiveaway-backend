from flask import Flask, redirect, url_for
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_migrate import Migrate
from api.helper.db import db
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound



from api.helper.application_configs import ApplicationConstant
from api.route.campaign_route import campaign_route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ApplicationConstant.sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = ApplicationConstant.sqlalchemy_track_modifications
app.config['SECRET_KEY'] = ApplicationConstant.app_secret_key
app.config['TWITTER_CONSUMER_KEY'] = ApplicationConstant.twitter_consumer_key
app.config['TWITTER_CONSUMER_SECRET'] = ApplicationConstant.twitter_consumer_secret
app.config['TWITTER_ACCESS_KEY'] = ApplicationConstant.twitter_access_key
app.config['TWITTER_ACCESS_SECRET'] = ApplicationConstant.twitter_access_secret
app.config['LN_API_KEY'] = ApplicationConstant.ln_api_key

db.init_app(app)

migrate = Migrate(app, db)
login_manager = LoginManager(app)

twitter_blueprint = make_twitter_blueprint(api_key=ApplicationConstant.twitter_consumer_key, api_secret=ApplicationConstant.twitter_consumer_secret)

app.register_blueprint(campaign_route, url_prefix="/campaign")
app.register_blueprint(twitter_blueprint,  url_prefix="/login")


class User(UserMixin, db.Model):
    __tablename__ = "users"


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)

    def __repr__(self):
        return f"<User {self.username}>"

class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = "oauth"

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

    def __repr__(self):
        return f"<OAuth {self.user_id}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


twitter_blueprint.backend = SQLAlchemyStorage(OAuth, db.session, user=current_user)


@app.route('/twitter')
def twitter_login():
    print("Got HEre")
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/settings.json')
    account_info_json = account_info.json()

    return '<h1> Your  Twitter name is @{}'.format(account_info_json['screen_name'])


@oauth_authorized.connect_via(twitter_blueprint)
def twitter_logged_in(blueprint, token):
    account_info = blueprint.session.get('account/settings.json')

    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['screen_name']

        query = User.query.filter_by(username=username)

        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        login_user(user)

@app.route('/')
@login_required
def index():
    print(">>>>> current_user ", current_user)
    return '<h1> You are logged in as {} </h1>'.format(current_user)


@app.route('/logout')
@login_required
def logout():
    load_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=ApplicationConstant.port)



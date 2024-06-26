from decouple import config
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registering blueprints
from localizeapp.auth.models import User
from localizeapp.auth.views import auth_blueprint
from localizeapp.core.views import core_blueprint
from localizeapp.localize.views import localize_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(core_blueprint)
app.register_blueprint(localize_blueprint)

login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500

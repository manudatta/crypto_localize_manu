from flask import Blueprint, render_template
from flask_login import login_required

core_blueprint = Blueprint("core", __name__)


@core_blueprint.route("/")
@login_required
def home():
    return render_template("core/index.html")

import datetime
import mongoengine as me

from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    session,
    current_app,
    send_file,
    abort,
)
from flask_login import login_user, logout_user, login_required, current_user

from funlab.models import users
from .. import oauth2
from .. import acl
from .. import forms

module = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@module.route("/")
def index():
    return render_template("dashboards/index.html")
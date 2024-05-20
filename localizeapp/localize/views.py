import lokalise
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

localize_blueprint = Blueprint("localize", __name__)
import pdb

from .forms import TaskForm

client = None
_token = None
_project_id = None
_key = None
_langs = None
_user = None


def get_client():
    from flask import current_app as app

    global client, _token, _project_id, _key, _user, _langs
    if not client:
        _token = app.config.get("LOCALIZE_API_KEY")
        _project_id = app.config.get("LOCALIZE_PORJECT_ID")
        _key = app.config.get("LOCALIZE_PROJECT_KEY")
        _user = app.config.get("LOCALIZE_PORJECT_USER")
        client = lokalise.Client(_token)
        _langs = [
            (l.lang_id, l.lang_name, l.lang_iso)
            for l in client.project_languages(_project_id).items
        ]
    return client


def create_task(client, form):
    target_lang = None
    i = None
    choice = None
    for i, i_choice in form.target_language.choices:
        if i == int(form.target_language.data):
            choice = i_choice
            break
    for i, lang_name, lang_iso in _langs:
        if choice in lang_name:
            target_lang = (i, lang_iso)
            break
    params = {}
    params["keys"] = [_key]
    params["title"] = form.title.data
    params["source_language_iso"] = "en"
    params["languages"] = [{"language_iso": target_lang[1], "users": [_user]}]
    return client.create_task(_project_id, params)


@login_required
@localize_blueprint.route("/localize/tasks", methods=["GET", "POST"])
def tasks():
    client = get_client()
    form = TaskForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            create_task(client, form)
    tasks = client.tasks(_project_id)
    return render_template("localize/tasks.html", form=form, tasks=tasks)

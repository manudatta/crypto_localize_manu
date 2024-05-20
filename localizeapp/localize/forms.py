from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SelectField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from localizeapp.auth.models import User


class TaskForm(FlaskForm):
    title = StringField(
        "title",
        validators=[
            DataRequired(),
            Length(
                min=10,
                max=255,
                message="Kindly add meaningful title b/n 10 to 255 characters of length",
            ),
        ],
    )
    target_language = SelectField(
        "target_language", choices=[(1, "Hindi"), (2, "Spanish"), (3, "Japanese")]
    )

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from blog.models import User


class UserRegisterForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0, "Usernames must have only letters, numbers, dots or underscores"),
        ],
    )
    email = StringField("Email", validators=[DataRequired(), Email(), Length(6, 255)])
    password = PasswordField(
        "Password", validators=[DataRequired(), EqualTo("confirm_password", message="Passwords must match.")]
    )
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    # is_staff = BooleanField("Staff")
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")

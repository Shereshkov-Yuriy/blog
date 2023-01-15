from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(6, 255)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

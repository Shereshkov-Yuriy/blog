from flask_wtf import FlaskForm
from wtforms import (SelectMultipleField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired


class CreateArticleForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])
    tags = SelectMultipleField("Tags", coerce=int)
    submit = SubmitField("Publish")

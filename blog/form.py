from flask_wtf import form
from wtforms import StringField, validators
from author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog Name', [
        validators.Required(),
        validators.Length(max=80)
        ])
    
from flask_wtf import Form
from my_blog import settings
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('username', [
        validators.Required(),
        validators.Length(min=settings.AUTHOR_STRING_LENGHT_MIN, 
            max=settings.AUTHOR_USERNAME_STRING_LENGHT)
        ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', 
        message = 'Passwords muyst match'),
        validators.Length(min=settings.AUTHOR_STRING_LENGHT_MIN, 
            max=settings.AUTHOR_PASSWORD_STRING_LENGHT)
        ])
    confirm = PasswordField('Repeat Password', [
        validators.Required()
        ])
        
class LoginForm(Form):
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=settings.AUTHOR_STRING_LENGHT_MIN,
            max=settings.AUTHOR_USERNAME_STRING_LENGHT)
        ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=settings.AUTHOR_STRING_LENGHT_MIN,
            max=settings.AUTHOR_PASSWORD_STRING_LENGHT)
        ])
    
    
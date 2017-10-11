from flask_wtf import Form as FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.validators import Length, DataRequired, EqualTo
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    fullname = StringField('Full Name', [validators.DataRequired()])
    email = EmailField('Email', [validators.DataRequired()])
#    username = StringField('username',
#        [validators.Required()
#        , validators.Lenght(min=4, max=25)
#        ])
    username = StringField('username',
        validators = [DataRequired(), Length(min=4, max=25)])

#    password = PasswordField('New Password',
#        [validators.DataRequired(),
#        validators.EqualTo('confirm', 
#        message = 'Passwords muyst match')
#        , validators.Lenght(min=4, max=80)
#        ])

    password = PasswordField('New Password',
        validators = [DataRequired(),
        EqualTo('confirm', message='Passwords must match'),
        Length(min=4,max=80)])
    confirm = PasswordField('Repeat Password', 
        [validators.DataRequired()])
        
        
    
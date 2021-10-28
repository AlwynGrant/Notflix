from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

def email_is_email(form, field):
    email = field.data
    if '@' not in email:
        raise ValidationError('Please enter a valid email address.')

def password_str(form, field):
    password = field.data
    if len(password) <= 5:
        raise ValidationError('Password must be longer than 5 characters.')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), user_exists, email_is_email])
    password = StringField('Password', validators=[DataRequired(), password_str])

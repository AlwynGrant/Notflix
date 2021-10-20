from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class NewProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    profile_img = StringField('profile_img')
    kids = BooleanField('kids', validators=[DataRequired()])

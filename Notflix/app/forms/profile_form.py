from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class NewProfileForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    kids = BooleanField('kids', validators=[DataRequired()])

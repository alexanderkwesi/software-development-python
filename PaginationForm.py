from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PForm(FlaskForm):
    #username = StringField('first_row', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    first_row = IntegerField('first_row')
    last_row = IntegerField('last_row')
    total_rows = StringField('total_rows')
    #remember_me = BooleanField('Remember Me')
    submit_previous = SubmitField('< previous')
    submit_next = SubmitField('next >')
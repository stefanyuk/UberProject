from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LeadForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=30)])
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Заказать консультацию')

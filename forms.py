from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    organization = StringField('Organization', validators=[DataRequired()])
    federal_permit_number = StringField('Federal Permit Number', validators=[Optional()])
    state_permit_number = StringField('State Permit Number', validators=[Optional()])
    contact_person_name = StringField('Contact Person Name', validators=[DataRequired()])
    country = StringField('Country', validators=[Optional()])
    mailing_address = StringField('Mailing Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[Optional()])
    postal_code = StringField('Postal Code', validators=[Optional()])
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    website_url = StringField('Website URL', validators=[Optional()])
    time_zone = StringField('Time Zone', validators=[Optional()])
    submit = SubmitField('Register')

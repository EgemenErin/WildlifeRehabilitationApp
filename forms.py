from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TelField, SelectField, DateTimeField, IntegerField, TextAreaField, SubmitField
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


class NewPatientForm(FlaskForm):
    # Basic Case Information
    case_year = SelectField('Case Year', choices=[('2024', '2024'), ('2023', '2023'), ('2022', '2022')],
                            validators=[DataRequired()])
    date_admitted = DateTimeField('Date Admitted', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    reference_number = StringField('Reference Number', validators=[Optional()])
    microchip_number = StringField('Microchip Number', validators=[Optional()])

    # Species Information
    common_name = StringField('Common Name', validators=[DataRequired()])
    morph = SelectField('Morph', choices=[
        ('Red', 'Red'), ('Gray', 'Gray'), ('Brown', 'Brown'), ('White', 'White'),
        ('Blue', 'Blue'), ('Dark', 'Dark'), ('Light', 'Light'), ('Albino', 'Albino'),
        ('Leucistic', 'Leucistic'), ('Piebald', 'Piebald'), ('Silver', 'Silver'), ('Black', 'Black')
    ], validators=[Optional()])
    number_of_patients = IntegerField('Number of Patients', default=1, validators=[DataRequired()])

    # Rescuer Contact Information
    entity = SelectField('Entity', choices=[
        ('General Public', 'General Public'),
        ('Individual Wildlife Rehabilitator', 'Individual Wildlife Rehabilitator'),
        ('Wildlife Rehabilitation Organization', 'Wildlife Rehabilitation Organization'),
        ('For-profit Organization', 'For-profit Organization'),
        ('Non-profit Organization', 'Non-profit Organization'),
        ('Federal (National) Agency / Biologist', 'Federal (National) Agency / Biologist'),
        ('State (Regional) Agency / Biologist', 'State (Regional) Agency / Biologist'),
        ('Local Animal Control Agency', 'Local Animal Control Agency'),
        ('Research Lab', 'Research Lab'),
        ('Law Enforcement Agency', 'Law Enforcement Agency'),
        ('Veterinary Facility', 'Veterinary Facility'),
        ('Other (specify in notes)', 'Other (specify in notes)')
    ], validators=[DataRequired()])
    organization = StringField('Organization', validators=[Optional()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    alt_phone_number = StringField('Alt. Phone Number', validators=[Optional()])
    email = StringField('Email', validators=[Optional()])
    address = StringField('Address', validators=[DataRequired()])
    city_province = StringField('City, Province', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[Optional()])
    notes_about_rescuer = TextAreaField('Notes About Rescuer', validators=[Optional()])

    # Donation Information
    donation_method = SelectField('Method', choices=[('Cash', 'Cash'), ('Credit', 'Credit'), ('Online', 'Online')],
                                  validators=[Optional()])
    donation_value = IntegerField('Value', validators=[Optional()])
    donation_comments = TextAreaField('Comments', validators=[Optional()])

    # Intake Information
    admitted_by = StringField('Admitted By', validators=[DataRequired()])
    transported_by = StringField('Transported By', validators=[Optional()])
    address_found = StringField('Address Found', validators=[DataRequired()])
    city_found = StringField('City Found, Province Found', validators=[DataRequired()])
    date_found = DateTimeField('Date Found', format='%Y-%m-%d', validators=[DataRequired()])
    reasons_for_admission = TextAreaField('Reasons for Admission', validators=[DataRequired()])
    care_by_rescuer = StringField('Care by Rescuer', validators=[Optional()])
    notes_about_rescue = TextAreaField('Notes About Rescue', validators=[Optional()])

    # Submit Button
    submit = SubmitField('Add Patient')
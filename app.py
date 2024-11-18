from flask import Flask, render_template, request, redirect, url_for, flash
from database import create_connection, init_db, add_user, get_user_by_email, add_patient_to_db
from werkzeug.security import generate_password_hash
from forms import RegistrationForm, NewPatientForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the email already exists
        if get_user_by_email(form.email.data):
            flash('Email already registered. Please use a different email.', 'danger')
            return render_template('register.html', form=form)
        else:
            # Hash the password
            password_hash = generate_password_hash(form.password.data)

            # Form data for insertion
            form_data = {
                'email': form.email.data,
                'password_hash': password_hash,
                'organization': form.organization.data,
                'federal_permit_number': form.federal_permit_number.data or None,
                'state_permit_number': form.state_permit_number.data or None,
                'contact_person_name': form.contact_person_name.data,
                'country': form.country.data or None,
                'mailing_address': form.mailing_address.data,
                'city': form.city.data,
                'state': form.state.data or None,
                'postal_code': form.postal_code.data or None,
                'phone_number': form.phone_number.data,
                'website_url': form.website_url.data or None,
                'time_zone': form.time_zone.data or None
            }

            # Add the user to the database
            add_user(form_data)

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    else:
        # Flash form errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    return render_template('register.html', form=form)


@app.route('/addpatient', methods=['GET', 'POST'])
def addpatient():
    form = NewPatientForm()

    if form.validate_on_submit():
        # Collect form data
        patient_data = {
            'case_year': form.case_year.data,
            'date_admitted': form.date_admitted.data,
            'reference_number': form.reference_number.data,
            'microchip_number': form.microchip_number.data,
            'common_name': form.common_name.data,
            'morph': form.morph.data,
            'number_of_patients': form.number_of_patients.data,
            'entity': form.entity.data,
            'organization': form.organization.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'phone_number': form.phone_number.data,
            'alt_phone_number': form.alt_phone_number.data,
            'email': form.email.data,
            'address': form.address.data,
            'city_province': form.city_province.data,
            'postal_code': form.postal_code.data,
            'notes_about_rescuer': form.notes_about_rescuer.data,
            'donation_method': form.donation_method.data,
            'donation_value': form.donation_value.data,
            'donation_comments': form.donation_comments.data,
            'admitted_by': form.admitted_by.data,
            'transported_by': form.transported_by.data,
            'address_found': form.address_found.data,
            'city_found': form.city_found.data,
            'date_found': form.date_found.data,
            'reasons_for_admission': form.reasons_for_admission.data,
            'care_by_rescuer': form.care_by_rescuer.data,
            'notes_about_rescue': form.notes_about_rescue.data
        }

        # Add patient data to the database
        try:
            add_patient_to_db(patient_data)
            flash("Patient successfully added!", "success")
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or another appropriate page
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('addpatient.html', form=form)



if __name__ == '__main__':
    init_db()
    app.run()

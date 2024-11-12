from flask import Flask, render_template, request, redirect, url_for, flash
from database import create_connection, init_db, add_user, get_user_by_email
from werkzeug.security import generate_password_hash
from forms import RegistrationForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
@app.route('/')
def index():  # put application's code here
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

if __name__ == '__main__':
    init_db()
    app.run()

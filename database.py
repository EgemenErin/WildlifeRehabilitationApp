import os
import sqlite3
import bcrypt
from werkzeug.security import generate_password_hash

def create_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'wildlife_rescue.db')
    print(f"Database path: {db_path}")
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                organization TEXT NOT NULL,
                federal_permit_number TEXT,
                state_permit_number TEXT,
                contact_person_name TEXT NOT NULL,
                country TEXT,
                mailing_address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT,
                postal_code TEXT,
                phone_number TEXT NOT NULL,
                website_url TEXT,
                time_zone TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"An error occurred while initializing the database: {e}")
    finally:
        conn.close()

def get_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_user(form_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (
            email,
            password_hash,
            organization,
            federal_permit_number,
            state_permit_number,
            contact_person_name,
            country,
            mailing_address,
            city,
            state,
            postal_code,
            phone_number,
            website_url,
            time_zone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        form_data['email'],
        form_data['password_hash'],
        form_data['organization'],
        form_data.get('federal_permit_number'),
        form_data.get('state_permit_number'),
        form_data['contact_person_name'],
        form_data.get('country'),
        form_data['mailing_address'],
        form_data['city'],
        form_data.get('state'),
        form_data.get('postal_code'),
        form_data['phone_number'],
        form_data.get('website_url'),
        form_data.get('time_zone')
    ))
    conn.commit()
    conn.close()

def add_patient_to_db(patient_data):
    conn = create_connection()
    cursor = conn.cursor()

    # SQL query to insert new patient data
    cursor.execute('''
        INSERT INTO Patients (
            case_year, date_admitted, reference_number, microchip_number,
            common_name, morph, number_of_patients, entity, organization,
            first_name, last_name, phone_number, alt_phone_number, email,
            address, city_province, postal_code, notes_about_rescuer,
            donation_method, donation_value, donation_comments,
            admitted_by, transported_by, address_found, city_found,
            date_found, reasons_for_admission, care_by_rescuer, notes_about_rescue
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        patient_data['case_year'],
        patient_data['date_admitted'],
        patient_data['reference_number'],
        patient_data['microchip_number'],
        patient_data['common_name'],
        patient_data['morph'],
        patient_data['number_of_patients'],
        patient_data['entity'],
        patient_data['organization'],
        patient_data['first_name'],
        patient_data['last_name'],
        patient_data['phone_number'],
        patient_data['alt_phone_number'],
        patient_data['email'],
        patient_data['address'],
        patient_data['city_province'],
        patient_data['postal_code'],
        patient_data['notes_about_rescuer'],
        patient_data['donation_method'],
        patient_data['donation_value'],
        patient_data['donation_comments'],
        patient_data['admitted_by'],
        patient_data['transported_by'],
        patient_data['address_found'],
        patient_data['city_found'],
        patient_data['date_found'],
        patient_data['reasons_for_admission'],
        patient_data['care_by_rescuer'],
        patient_data['notes_about_rescue']
    ))

    conn.commit()
    conn.close()

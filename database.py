import sqlite3
import bcrypt

def create_connection():
    conn = sqlite3.connect('wildlife_rescue.db')
    return conn

def init_db():
    conn = create_connection()
    cursor = conn.cursor()

    # Create the Users table
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

def get_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

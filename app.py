from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'student_marks_db'
}

# Function to get database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to initialize database
def init_db():
    try:
        # Connect without database first to create it
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cursor.close()
        conn.close()
        
        # Now connect to the database and create table
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    roll_no VARCHAR(50) NOT NULL,
                    mark1 INT NOT NULL,
                    mark2 INT NOT NULL,
                    mark3 INT NOT NULL
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            print("MySQL Database initialized successfully!")
    except Error as e:
        print(f"Error initializing database: {e}")

# Initialize database when app starts
init_db()

# Route: Home/Landing page - redirects to register
@app.route('/')
def index():
    return redirect(url_for('register'))

# Route: Registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Route: Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route: Home page (main application page)
@app.route('/home')
def home():
    return render_template('home.html')

# Route: Add student (POST)
@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        # Get form data
        name = request.form['name']
        roll_no = request.form['roll_no']
        mark1 = int(request.form['mark1'])
        mark2 = int(request.form['mark2'])
        mark3 = int(request.form['mark3'])
        
        # Insert into database
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, roll_no, mark1, mark2, mark3)
                VALUES (%s, %s, %s, %s, %s)
            ''', (name, roll_no, mark1, mark2, mark3))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'success': True, 'message': 'Student added successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Database connection failed'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

# Route: Get all students (GET)
@app.route('/get_students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM students ORDER BY id DESC')
            students = cursor.fetchall()
            cursor.close()
            conn.close()
            
            # Convert to list of dictionaries
            students_list = []
            for student in students:
                students_list.append({
                    'id': student['id'],
                    'name': student['name'],
                    'roll_no': student['roll_no'],
                    'mark1': student['mark1'],
                    'mark2': student['mark2'],
                    'mark3': student['mark3'],
                    'total': student['mark1'] + student['mark2'] + student['mark3'],
                    'average': round((student['mark1'] + student['mark2'] + student['mark3']) / 3, 2)
                })
            
            return jsonify({'success': True, 'students': students_list})
        else:
            return jsonify({'success': False, 'message': 'Database connection failed'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Student Marks Management System

A simple web application built with Python Flask and SQLite to manage student marks.

## Features
- Student registration and login pages (simple redirect-based)
- Add student records with name, roll number, and three marks
- View all student records in a table
- Automatic calculation of total and average marks
- SQLite database for persistent storage

## Project Structure
```
saturday1/
├── app.py                  # Main Flask application
├── students.db            # SQLite database (created automatically)
└── templates/
    ├── register.html      # Registration page
    ├── login.html         # Login page
    └── home.html          # Main application page
```

## Requirements
- Python 3.x
- Flask

## Installation Steps

### Step 1: Install Python
Make sure Python 3.x is installed on your system. Check by running:
```bash
python --version
```

### Step 2: Install Flask
Open terminal/command prompt in the project directory and run:
```bash
pip install flask
```

### Step 3: Run the Application
Navigate to the project directory and run:
```bash
python app.py
```

You should see output like:
```
Database initialized successfully!
 * Running on http://127.0.0.1:5000
```

### Step 4: Access the Application
Open your web browser and go to:
```
http://127.0.0.1:5000
```

## How to Use

1. **Registration Page**: 
   - Enter username, email, and password
   - Click "Register" button
   - You'll be redirected to the login page

2. **Login Page**:
   - Enter username and password
   - Click "Login" button
   - You'll be redirected to the home page

3. **Home Page** (Main Application):
   - Enter student details:
     - Student Name
     - Roll Number
     - Mark 1, Mark 2, Mark 3 (0-100)
   - Click "Add Student" to save the record
   - Click "Refresh Data" to reload the student table
   - View all students in the table below with:
     - Name, Roll No, Individual Marks
     - Total (sum of all marks)
     - Average (calculated automatically)

## API Endpoints

- `GET /` - Redirects to registration page
- `GET /register` - Shows registration form
- `GET /login` - Shows login form
- `GET /home` - Shows main application page
- `POST /add_student` - Adds a new student to database
- `GET /get_students` - Fetches all students from database

## Database Schema

**Table: students**
| Column   | Type    | Description              |
|----------|---------|--------------------------|
| id       | INTEGER | Primary key (auto-increment) |
| name     | TEXT    | Student name             |
| roll_no  | TEXT    | Roll number              |
| mark1    | INTEGER | First subject mark       |
| mark2    | INTEGER | Second subject mark      |
| mark3    | INTEGER | Third subject mark       |

## Notes
- The database file `students.db` is created automatically when you first run the application
- No actual authentication is implemented - login is just a redirect
- The application runs in debug mode by default (port 5000)
- To stop the server, press `Ctrl+C` in the terminal

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Install Flask using `pip install flask`

**Problem**: Port 5000 already in use
- **Solution**: Change the port in `app.py` (last line) to another port like 5001

**Problem**: Database not saving data
- **Solution**: Make sure you have write permissions in the project directory

## Author
Created as a beginner-friendly Flask project for learning purposes.

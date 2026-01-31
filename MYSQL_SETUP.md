# MySQL Setup Instructions

## Step 1: Install MySQL Connector
```bash
pip install mysql-connector-python
```

## Step 2: Configure MySQL Database

### In MySQL Workbench:
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Update the credentials in `app.py`:
   - Line 8: `'user': 'root'` (your MySQL username)
   - Line 9: `'password': ''` (your MySQL password)

### Option A: Let the app create the database automatically
- Just run the Flask app, it will create `student_db` database and `students` table automatically

### Option B: Create manually in MySQL Workbench
```sql
-- Create database
CREATE DATABASE IF NOT EXISTS student_db;

-- Use the database
USE student_db;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    roll_no VARCHAR(50) NOT NULL,
    mark1 INT NOT NULL,
    mark2 INT NOT NULL,
    mark3 INT NOT NULL
);
```

## Step 3: Update app.py Configuration

Edit the DB_CONFIG section in `app.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # Your MySQL username
    'password': 'your_password',  # Your MySQL password
    'database': 'student_db'
}
```

## Step 4: Run the Application
```bash
python app.py
```

## Common MySQL Errors:

**Error: Access denied for user**
- Check your username and password in DB_CONFIG

**Error: Unknown database 'student_db'**
- The app will create it automatically, or create manually using the SQL above

**Error: No module named 'mysql.connector'**
- Run: `pip install mysql-connector-python`

## Verify Data in MySQL Workbench:

After adding students through the web app, you can check in MySQL Workbench:

```sql
USE student_db;
SELECT * FROM students;
```

Or use the query editor to view the table data visually.

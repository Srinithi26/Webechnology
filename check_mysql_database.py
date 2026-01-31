import mysql.connector
from mysql.connector import Error

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'student_db'
}

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Show table structure
    print("=" * 80)
    print("TABLE STRUCTURE")
    print("=" * 80)
    cursor.execute("DESCRIBE students")
    columns = cursor.fetchall()
    for col in columns:
        print(f"{col[0]:<15} {col[1]:<20} {col[2]:<10} {col[3]:<10}")
    
    print("\n" + "=" * 80)
    print("STUDENT RECORDS")
    print("=" * 80)
    
    # Get all students
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    
    print(f"\nTotal Records: {len(rows)}\n")
    
    if len(rows) == 0:
        print("No student records found in MySQL database.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Roll No':<12} {'Mark1':<7} {'Mark2':<7} {'Mark3':<7} {'Total':<7} {'Avg':<7}")
        print("-" * 80)
        
        for row in rows:
            student_id, name, roll_no, mark1, mark2, mark3 = row
            total = mark1 + mark2 + mark3
            average = round(total / 3, 2)
            print(f"{student_id:<5} {name:<20} {roll_no:<12} {mark1:<7} {mark2:<7} {mark3:<7} {total:<7} {average:<7}")
    
    print("\n" + "=" * 80)
    
    cursor.close()
    conn.close()
    
except Error as e:
    print(f"Error: {e}")

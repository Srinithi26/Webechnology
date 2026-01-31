import sqlite3

# Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Get all students
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

print("=" * 80)
print("STUDENT DATABASE RECORDS")
print("=" * 80)
print(f"\nTotal Records: {len(rows)}\n")

if len(rows) == 0:
    print("No student records found in the database.")
else:
    print(f"{'ID':<5} {'Name':<20} {'Roll No':<12} {'Mark1':<7} {'Mark2':<7} {'Mark3':<7} {'Total':<7} {'Avg':<7}")
    print("-" * 80)
    
    for row in rows:
        student_id, name, roll_no, mark1, mark2, mark3 = row
        total = mark1 + mark2 + mark3
        average = round(total / 3, 2)
        print(f"{student_id:<5} {name:<20} {roll_no:<12} {mark1:<7} {mark2:<7} {mark3:<7} {total:<7} {average:<7}")

print("\n" + "=" * 80)

# Close connection
conn.close()

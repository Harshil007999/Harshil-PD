import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.executescript('''
    CREATE TABLE students (
        id INT,
        name VARCHAR(50),
        age INT,
        city VARCHAR(50),
        dept VARCHAR(10)
    );

    INSERT INTO students VALUES (1, 'Harshil', 20, 'Surat', 'IT');
    INSERT INTO students VALUES (2, 'Raj', 21, 'Ahmedabad', 'CS');
    INSERT INTO students VALUES (3, 'Priya', 20, 'Surat', 'IT');
    INSERT INTO students VALUES (4, 'Amit', 22, 'Mumbai', 'CS');
    INSERT INTO students VALUES (5, 'Sneha', 21, 'Surat', 'IT');
    INSERT INTO students VALUES (6, 'Vikas', 20, 'Ahmedabad', 'CS');
    INSERT INTO students VALUES (7, 'Neha', 22, 'Mumbai', 'IT');
    INSERT INTO students VALUES (8, 'Rohan', 21, 'Surat', 'CS');

    CREATE TABLE grades (
        student_id INT,
        subject VARCHAR(50),
        marks INT
    );

    INSERT INTO grades VALUES (1, 'Maths', 85);
    INSERT INTO grades VALUES (1, 'Python', 90);
    INSERT INTO grades VALUES (2, 'Maths', 72);
    INSERT INTO grades VALUES (2, 'Python', 68);
    INSERT INTO grades VALUES (3, 'Maths', 91);
    INSERT INTO grades VALUES (3, 'Python', 88);
    INSERT INTO grades VALUES (4, 'Maths', 65);
    INSERT INTO grades VALUES (4, 'Python', 70);
    INSERT INTO grades VALUES (5, 'Maths', 89);
    INSERT INTO grades VALUES (5, 'Python', 92);
    INSERT INTO grades VALUES (6, 'Maths', 75);
    INSERT INTO grades VALUES (6, 'Python', 78);
    INSERT INTO grades VALUES (7, 'Maths', 93);
    INSERT INTO grades VALUES (7, 'Python', 95);
    INSERT INTO grades VALUES (8, 'Maths', 60);
    INSERT INTO grades VALUES (8, 'Python', 63);
''')


print("Q1 — Students from Surat:")
cursor.execute("SELECT name FROM students WHERE city = 'Surat'")
print(cursor.fetchall())


print("\nQ2 — IT students ordered by name:")
cursor.execute("SELECT name FROM students WHERE dept = 'IT' ORDER BY name")
print(cursor.fetchall())


print("\nQ3 — Students per department:")
cursor.execute("SELECT dept, COUNT(1) AS num_stu FROM students GROUP BY dept")
print(cursor.fetchall())


print("\nQ4 — City with most students:")
cursor.execute("SELECT city, COUNT(1) AS num_stu FROM students GROUP BY city ORDER BY num_stu DESC LIMIT 1")
print(cursor.fetchall())


print("\nQ5 — Average marks per subject:")
cursor.execute("SELECT subject, AVG(marks) FROM grades GROUP BY subject")
print(cursor.fetchall())


print("\nQ6 — Students above 80 in Python:")
cursor.execute("SELECT student_id, marks FROM grades WHERE subject = 'Python' AND marks > 80")
print(cursor.fetchall())


print("\nQ7 — Student name with total marks:")
cursor.execute("""
    SELECT s.name, SUM(marks) AS total_marks
    FROM grades AS g
    JOIN students AS s ON g.student_id = s.id
    GROUP BY s.name
""")
print(cursor.fetchall())


print("\nQ8 — IT students with average marks:")
cursor.execute("""
    SELECT s.name, AVG(marks) AS avg_marks
    FROM grades AS g
    JOIN students AS s ON g.student_id = s.id
    WHERE s.dept = 'IT'
    GROUP BY s.name
""")
print(cursor.fetchall())


print("\nQ9 — Department average marks:")
cursor.execute("""
    SELECT s.dept, AVG(marks) AS avg_marks
    FROM grades AS g
    JOIN students AS s ON g.student_id = s.id
    GROUP BY s.dept
""")
print(cursor.fetchall())


print("\nQ10 — Top 3 students by total marks:")
cursor.execute("""
    SELECT s.name, SUM(marks) AS total_marks
    FROM grades AS g
    JOIN students AS s ON g.student_id = s.id
    GROUP BY s.name
    ORDER BY total_marks DESC
    LIMIT 3
""")
print(cursor.fetchall())
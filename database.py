import sqlite3

def initialize_db():
    try:
        connection = sqlite3.connect("student_reviews.db")
        cursor = connection.cursor()
        create_tables(cursor)



        return (connection, cursor)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None, None



def create_tables(cursor):
    tables = """   



CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    template TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Lessons (
    lesson_number INTEGER PRIMARY KEY,
    lesson_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS LessonSubjects (
    lesson_number INTEGER,
    subject_id INTEGER,
    vocabulary TEXT,
    PRIMARY KEY (lesson_number, subject_id),
    FOREIGN KEY (lesson_number) REFERENCES Lessons(lesson_number),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_number INTEGER,
    student_id INTEGER,
    evaluation TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lesson_number) REFERENCES Lessons(lesson_number),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
"""
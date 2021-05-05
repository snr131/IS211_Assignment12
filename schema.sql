CREATE TABLE IF NOT EXISTS students(
   student_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS quizzes(
   quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
   subject TEXT NOT NULL,
   num_questions INTEGER NOT NULL,
   date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS results(
   result_id INTEGER PRIMARY KEY AUTOINCREMENT,
   student_id INTEGER NOT NULL,
   quiz_id INTEGER NOT NULL, 
   result INTEGER NOT NULL
);

INSERT INTO students (first_name, last_name)
VALUES("John", "Smith");

INSERT INTO quizzes (subject, num_questions, date)
VALUES("Python Basics", 5, "February, 5th, 2015");

INSERT INTO results (student_id, quiz_id, result)
VALUES(1, 1, 85);
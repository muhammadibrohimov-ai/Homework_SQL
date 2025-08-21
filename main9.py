from main import *


create_table('students', id='serial primary key', name='varchar(100)', age='int', group_id='int')
create_table('exams', id='serial primary key', subject='varchar(100)')
create_table('results', id='serial primary key', student_id='int references students(id)', exam_id='int references exams(id)', grade='int')


students_data = [
    "insert into students (name, age, group_id) values ('Alice', 20, 1);",
    "insert into students (name, age, group_id) values ('Bob', 21, 1);",
    "insert into students (name, age, group_id) values ('Charlie', 22, 2);",
    "insert into students (name, age, group_id) values ('David', 20, 2);",
    "insert into students (name, age, group_id) values ('Eva', 23, 3);",
    "insert into students (name, age, group_id) values ('Frank', 21, 3);",
    "insert into students (name, age, group_id) values ('Grace', 22, 4);",
    "insert into students (name, age, group_id) values ('Hannah', 20, 4);",
    "insert into students (name, age, group_id) values ('Ian', 23, 5);",
    "insert into students (name, age, group_id) values ('Jane', 21, 5);"
]

exams_data = [
    "insert into exams (subject) values ('Math');",
    "insert into exams (subject) values ('Physics');",
    "insert into exams (subject) values ('Chemistry');",
    "insert into exams (subject) values ('Biology');",
    "insert into exams (subject) values ('History');",
    "insert into exams (subject) values ('Geography');",
    "insert into exams (subject) values ('English');",
    "insert into exams (subject) values ('Computer Science');",
    "insert into exams (subject) values ('Art');",
    "insert into exams (subject) values ('Music');"
]

results_data = [
    "insert into results (student_id, exam_id, grade) values (1,1,90);",
    "insert into results (student_id, exam_id, grade) values (2,2,85);",
    "insert into results (student_id, exam_id, grade) values (3,3,78);",
    "insert into results (student_id, exam_id, grade) values (4,4,88);",
    "insert into results (student_id, exam_id, grade) values (5,5,92);",
    "insert into results (student_id, exam_id, grade) values (6,6,81);",
    "insert into results (student_id, exam_id, grade) values (7,7,79);",
    "insert into results (student_id, exam_id, grade) values (8,8,95);",
    "insert into results (student_id, exam_id, grade) values (9,9,87);",
    "insert into results (student_id, exam_id, grade) values (10,10,90);"
]

for q in students_data + exams_data + results_data:
    get_info(q)


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} - {i[1]} - {i[2]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = """
SELECT st.name, ex.subject, r.grade
FROM results r
JOIN students st ON r.student_id = st.id
JOIN exams ex ON r.exam_id = ex.id;
"""
show_data(get_info(query))

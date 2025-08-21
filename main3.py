from main import *

create_table('teachers', id='serial primary key', name='varchar(100)')
create_table('subjects', id='serial primary key', name='varchar(100)', teacher_id='int references teachers(id)')

teachers_data = [
    "insert into teachers (name) values ('Mr. Smith');",
    "insert into teachers (name) values ('Ms. Johnson');",
    "insert into teachers (name) values ('Mr. Brown');",
    "insert into teachers (name) values ('Ms. Davis');",
    "insert into teachers (name) values ('Mr. Wilson');",
    "insert into teachers (name) values ('Ms. Martinez');",
    "insert into teachers (name) values ('Mr. Anderson');",
    "insert into teachers (name) values ('Ms. Thomas');",
    "insert into teachers (name) values ('Mr. Jackson');",
    "insert into teachers (name) values ('Ms. White');"
]

subjects_data = [
    "insert into subjects (name, teacher_id) values ('Math', 1);",
    "insert into subjects (name, teacher_id) values ('English', 2);",
    "insert into subjects (name, teacher_id) values ('Physics', 3);",
    "insert into subjects (name, teacher_id) values ('Chemistry', 4);",
    "insert into subjects (name, teacher_id) values ('Biology', 5);",
    "insert into subjects (name, teacher_id) values ('History', 6);",
    "insert into subjects (name, teacher_id) values ('Geography', 7);",
    "insert into subjects (name, teacher_id) values ('Computer Science', 8);",
    "insert into subjects (name, teacher_id) values ('Art', 9);",
    "insert into subjects (name, teacher_id) values ('Music', 10);"
]


for q in teachers_data + subjects_data:
    get_info(q)


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} - {i[1]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = """
SELECT t.name, s.name
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id;
"""
show_data(get_info(query))

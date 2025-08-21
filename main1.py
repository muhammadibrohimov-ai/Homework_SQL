'''
    Avval 'main.py' fayli ko'ring va o'zingizga sozlang
'''

from main import *

create_table('departments', id = "serial primary key", name = 'varchar(150)')
create_table('employees', id = "serial primary key", name = 'varchar(150)', year = "int not null", department_id = 'int references departments(id)')


queries = [
    "insert into departments (name) values ('Support');",
    "insert into departments (name) values ('Services');",
    "insert into departments (name) values ('Marketing');",
    "insert into departments (name) values ('Legal');",
    "insert into departments (name) values ('Business Development');",
    "insert into departments (name) values ('Training');",
    "insert into departments (name) values ('Product Management');",
    "insert into departments (name) values ('Legal');",
    "insert into departments (name) values ('Business Development');",
    "insert into departments (name) values ('Support');",
    "insert into employees (name, year, department_id) values ('Lowell Barkly', 2001, 5);",
    "insert into employees (name, year, department_id) values ('Kelila Pelman', 2006, 6);",
    "insert into employees (name, year, department_id) values ('Constantina Breckwell', 1999, 7);",
    "insert into employees (name, year, department_id) values ('Mata Subhan', 2006, 6);",
    "insert into employees (name, year, department_id) values ('Wash Tomasi', 1993, 1);",
    "insert into employees (name, year, department_id) values ('Duff Charteris', 1993, 3);",
    "insert into employees (name, year, department_id) values ('Hersh Pepye', 2006, 6);",
    "insert into employees (name, year, department_id) values ('Padriac Friedman', 2004, 1);",
    "insert into employees (name, year, department_id) values ('Lula Garland', 1988, 8);",
    "insert into employees (name, year, department_id) values ('Minnie Letch', 2008, 6);"
]
for query in queries:
    get_info(query)

data = get_info("SELECT e.name, d.name FROM employees e JOIN departments d ON e.department_id = d.id;")

if data:
    for i in data:
        print(f'{i[0]} - {i[1]}')

else :
    print("Hech qanday ma'lumot kelmadi")
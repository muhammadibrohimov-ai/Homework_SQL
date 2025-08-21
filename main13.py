from main import *

def show_data(data):
    if data:
        for i in data:
            print(i)
        print()
    else:
        print("Hech qanday ma'lumot kelmadi")

extra_commands("ALTER TABLE employees ADD COLUMN salary DECIMAL(8,2) DEFAULT 1000.00;")
show_data(get_info("SELECT * FROM employees WHERE department_id IN (SELECT id FROM departments WHERE name = 'IT');"))
extra_commands("UPDATE employees SET salary = salary * 1.10 WHERE department_id IN (SELECT id FROM departments WHERE name = 'IT');")
show_data(get_info("SELECT * FROM employees WHERE department_id IN (SELECT id FROM departments WHERE name = 'IT');"))


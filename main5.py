from main import *


extra_commands("""
UPDATE employees
SET salary = salary * 1.10
WHERE 2025 - year >= 5;
""")


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} - {i[1]} - {i[2]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = "SELECT name, year, salary FROM employees;"
show_data(get_info(query))

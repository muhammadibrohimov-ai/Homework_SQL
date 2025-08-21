from main import *

query = "SELECT name, salary FROM employees WHERE salary > 3000 ORDER BY salary DESC;"

def show_data(data):
    if data:
        print(f'Eng yuqori maoshli hodim:\n{data[0][0]} - {data[0][1]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

show_data(get_info(query))

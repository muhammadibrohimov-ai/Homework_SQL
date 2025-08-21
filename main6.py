from main import *


extra_commands("""
UPDATE orders
SET status='Completed'
WHERE status='Pending';
""")


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} - {i[1]} - {i[2]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = "SELECT id, customer_id, status FROM orders;"
show_data(get_info(query))

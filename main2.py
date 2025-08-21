from main import *


create_table('customers', id='serial primary key', first_name='varchar(100)', last_name='varchar(100)', country='varchar(50)', city='varchar(50)')
create_table('orders', id='serial primary key', customer_id='int references customers(id)', order_date='date', status='varchar(50)')

customers_data = [
    "insert into customers (first_name, last_name, country, city) values ('John', 'Doe', 'USA', 'NY');",
    "insert into customers (first_name, last_name, country, city) values ('Ali', 'Karimov', 'Uzbekistan', 'Samarkand');",
    "insert into customers (first_name, last_name, country, city) values ('Sara', 'Smith', 'UK', 'London');",
    "insert into customers (first_name, last_name, country, city) values ('Nurlan', 'Azimov', 'Uzbekistan', 'Tashkent');",
    "insert into customers (first_name, last_name, country, city) values ('Anna', 'Brown', 'USA', 'LA');",
    "insert into customers (first_name, last_name, country, city) values ('Tim', 'Johnson', 'Canada', 'Toronto');",
    "insert into customers (first_name, last_name, country, city) values ('Lina', 'Ivanova', 'Russia', 'Moscow');",
    "insert into customers (first_name, last_name, country, city) values ('Olim', 'Bek', 'Uzbekistan', 'Bukhara');",
    "insert into customers (first_name, last_name, country, city) values ('Megan', 'White', 'UK', 'Manchester');",
    "insert into customers (first_name, last_name, country, city) values ('Rustam', 'Yuldashov', 'Uzbekistan', 'Fergana');"
]

orders_data = [
    "insert into orders (customer_id, order_date, status) values (1, '2025-01-01', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (2, '2025-01-02', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (3, '2025-01-03', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (4, '2025-01-04', 'Completed');",
    "insert into orders (customer_id, order_date, status) values (5, '2025-01-05', 'Cancelled');",
    "insert into orders (customer_id, order_date, status) values (6, '2025-01-06', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (7, '2025-01-07', 'Completed');",
    "insert into orders (customer_id, order_date, status) values (8, '2025-01-08', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (9, '2025-01-09', 'Pending');",
    "insert into orders (customer_id, order_date, status) values (10, '2025-01-10', 'Cancelled');"
]


for q in customers_data + orders_data:
    get_info(q)


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} {i[1]} - {i[2]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = """
SELECT c.last_name, o.order_date, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.id;
"""
show_data(get_info(query))

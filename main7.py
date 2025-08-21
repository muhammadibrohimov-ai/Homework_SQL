from main import *


create_table('cars', id='serial primary key', model='varchar(100)', mileage='int', price='decimal(10,2)')


cars_data = [
    "insert into cars (model, mileage, price) values ('Toyota Camry', 210000, 15000);",
    "insert into cars (model, mileage, price) values ('Honda Accord', 180000, 14000);",
    "insert into cars (model, mileage, price) values ('BMW 320', 250000, 20000);",
    "insert into cars (model, mileage, price) values ('Mercedes C200', 220000, 22000);",
    "insert into cars (model, mileage, price) values ('Audi A4', 190000, 21000);",
    "insert into cars (model, mileage, price) values ('Ford Focus', 230000, 12000);",
    "insert into cars (model, mileage, price) values ('Chevrolet Malibu', 200000, 13000);",
    "insert into cars (model, mileage, price) values ('Nissan Altima', 240000, 14000);",
    "insert into cars (model, mileage, price) values ('Kia Optima', 195000, 12500);",
    "insert into cars (model, mileage, price) values ('Hyundai Sonata', 205000, 13500);"
]

for q in cars_data:
    get_info(q)


extra_commands("""
UPDATE cars
SET price = price * 0.8
WHERE mileage > 200000;
""")


def show_data(data):
    if data:
        for i in data:
            print(f'{i[0]} - {i[1]} - {i[2]}')
    else:
        print("Hech qanday ma'lumot kelmadi")

query = "SELECT model, mileage, price FROM cars;"
show_data(get_info(query))

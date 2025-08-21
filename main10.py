from main import *

name = input("Talaba ismi: ")
age = int(input("Talaba yoshi: "))
group_id = int(input("Group ID: "))

try:
    get_info(f"INSERT INTO students (name, age, group_id) VALUES ('{name}', {age}, {group_id});")
    print("Yangi talaba qo'shildi.")
except Exception as e:
    print(f"Xatolik: {e}")

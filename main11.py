from main import *

customer_id = int(input("Customer ID: "))
product_id = int(input("Product ID (examplar uchun 1-10): "))
quantity = int(input("Quantity: "))

try:
    get_info(f"INSERT INTO orders (customer_id, order_date, status) VALUES ({customer_id}, CURRENT_DATE, 'Pending');")
    print("Yangi buyurtma qo'shildi.")
except Exception as e:
    print(f"Xatolik: {e}")

    # Rollback main.py faylida qilinadi

from main import *

order_id = int(input("Yangilash uchun order_id: "))
extra_commands(f"UPDATE orders SET status='Completed' WHERE id={order_id};")
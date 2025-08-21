import psycopg2

def get_connection():

    return psycopg2.connect(
        database = "fn34", # ma'lumotlar bazasi nomini yozing
        user = "postgres", # o'zingizning postgresql username ngizni yozing
        password = "197346825@Miu#", #o'zingizning parolingizni yozing
        host = "localhost",
        port = "5432"
    )

def get_cursor(db : object):
    return db.cursor()

def create_table(table_name, **kwargs):
    with get_connection() as db:
        with get_cursor(db) as dbc:
            query = f'''
            CREATE TABLE IF NOT EXISTS {table_name}(\n
            '''

            columns = []

            for key, value in kwargs.items():
                columns.append(f'{key} {value.upper()}')

            query += ',\n'.join(columns) + ');'

            try :
                dbc.execute(query)
                db.commit()
            except Exception as e:
                print(f"Xatolik yuzaga keldi :\n{e}\nROLLBACK qilindi.")
                db.rollback()
                return None
def get_info(query):
    with get_connection() as db:
        with get_cursor(db) as dbc:
            try:
                dbc.execute(query)
                if query.lower().strip().startswith("select"):
                    result = dbc.fetchall()
                    return result if result else None
                db.commit()
            except Exception as e:
                print(f"Xatolik yuzaga keldi :\n{e}\nROLLBACK qilindi.")
                db.rollback()
                return None

def extra_commands(query):
    with get_connection() as db:
        with get_cursor(db) as dbc:
            try:
                dbc.execute(query)
                print("O'zgardi")
                db.commit()
            except Exception as e:
                print(f"Xatolik yuzaga keldi :\n{e}\nROLLBACK qilindi.")
                db.rollback()
                return None
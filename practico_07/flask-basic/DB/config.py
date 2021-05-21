import sqlite3


def db_connection():
    # Create database or connect
    connect = sqlite3.connect("./DB/contact_book.db")

    # Create cursor
    cursor = connect.cursor()
    create_table(cursor)

    return connect, cursor


def db_connection_close(connect):
    # Commit changes
    connect.commit()

    # Connection close
    connect.close()


def create_table(cursor):
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts' ''')

    # if the count is 1, then table exists
    if cursor.fetchone()[0] == 1:
        print('Table exists.')
    else:
        cursor.execute("""CREATE TABLE contacts (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zip_code integer,
        phone text,
        email text
        )""")

        cursor.execute("INSERT INTO contacts VALUES ("
                       ":first_name, :last_name, :address, :city, :state, "
                       ":zip_code, :phone, :email)", {
                           'first_name': 'Larry',
                           'last_name': 'Danny',
                           'address': '123 str',
                           'city': 'Dhaka',
                           'state': 'Dhaka',
                           'zip_code': 1212,
                           'phone': '1234567',
                           'email': 'larry@gmail.com',
                       })

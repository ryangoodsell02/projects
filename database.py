import sqlite3

db_name = "customers.db"  # global variable


def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("Connect to DB.")
    return db_conn, db_cursor


def create_table(db_cursor):
    sql = "create table customers (customer_id integer, customer_name text, customer_email text, phone integer, last_purchase text, address text)"
    db_cursor.execute(sql)
    print("Table Created.")


def drop_table(db_cursor):
    sql = "drop table if exists customers"
    db_cursor.execute(sql)
    print("Table Dropped.")


def insert_row(db_cursor):
    sql = "insert into customers values (?, ?, ?, ?, ?, ?)"
    customer_id = int(input("Enter your customer ID (int): "))
    customer_name = input("Enter you First Name (str): ")
    customer_email = input("Enter your e-mail (str): ")
    phone = int(input("Enter you 10 digit phone number without spaces or dashes (int): "))
    last_purchase = input("Enter your last_purchase (str): ")
    address = input("Enter your address (str): ")
    tuple_of_values = (customer_id, customer_name, customer_email, phone, last_purchase, address)
    db_cursor.execute(sql, tuple_of_values)
    print("Row inserted into the table")
    # TODO - ASK FOR VALUES
    # TODO - ASK FOR CUSTOMER ID
    # TODO - ADK FOR CUST NAME
    # TODO - ASK FOR CUST EMAIL
    # TODO - ASK FOR PHONE
    # TODO - ASK FOR LAST PURCHASE
    # TODO - ASK FOR ADDRESS
    # TODO - PACKAGE VARIABLE TOGETHER AND PUT THEM IN A TUPLE


def select_all(db_cursor):
    sql = "select * from customers"

    result_set = db_cursor.execute(sql)

    print("\nTable now has the following rows:")
    for row in result_set:
        print(row)


def select_row(db_cursor):
    # TODO - select with a where clause
    sql = "select * from customers where customer_id = ?"

    cust_id = int(input("Please enter the customer ID (int) you want to search for: "))

    tuple_of_value = (cust_id, )

    result_set = db_cursor.execute(sql, tuple_of_value)

    print("\nHere is the row that you have selected")
    for row in result_set:
        print(row)
    print()


def update_row(db_cursor):
    sql = "update customers set phone = ?, last_purchase = ? where customer_id = ?"

    # TODO - ASK USER FOR 3 VALUES

    # TODO - ASK FOR CUSTOMER ID
    customer_id = int(input("Enter the customer ID (int) for the book you would like to update: "))

    # TODO - ASK USER FOR LAST PURCHASE
    purchase = input("Enter the last purchase (str): ")

    # TODO - ASK FOR PHONE
    phone = input("Enter the new phone (int): ")

    tuple_of_values = (phone, purchase, customer_id)

    db_cursor.execute(sql, tuple_of_values)

    print("The row has been updated:")

def delete_row(db_cursor):
    sql = "delete from customers where customer_id = ?"

    cust_id = int(input("Enter the customer ID (int) that you want to delete: "))

    tuple_of_value = (cust_id, )

    db_cursor.execute(sql, tuple_of_value)

    print("The row is deleted.")


def display_menu(db_conn, db_cursor):
    # TODO - LOOP
    while True:
        print("Menu:")
        print("Enter S to get started and create a new database")
        print("Enter C to create a new row")
        print("Enter R to retrieve data")
        print("Enter U to update a row")
        print("Enter D to delete a row")
        print("Enter Q to quit the program")
        # print("Enter your choice:")
        choice = input("Enter your choice: ").upper()
        if choice == "S":
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == "C":
            insert_row(db_cursor)
        elif choice == "R":
            select_row(db_cursor)
        elif choice == "U":
            update_row(db_cursor)
        elif choice == "D":
            delete_row(db_cursor)
        elif choice == "Q":
            print("Goodbye")
            break
        else:
            print("That is an invalid choice of", choice)
        db_conn.commit()
        select_all(db_cursor)

        # TODO - DISPLAY THE MENU
        # TODO - ASK THE USER FOR THEIR MENU CHOICE
        # TODO - CALL THE APPROPRIATE FUNCTION
        # TODO - (AFTER EACH MENU ACTION) - COMMIT
        # TODO - (AFTER MENU ACTION) - select_all - see what data is in the db


def main():
    # TODO - call connect_to_db
    db_conn, db_cursor = connect_to_db()
    # TODO - call display_menu
    display_menu(db_conn, db_cursor)
    # TODO  - close the db
    db_conn.close()


main()

import psycopg2
from psycopg2 import Error

def menu():

    menu = {}
    menu['1']="Check postgres server info." 
    menu['2']="Add entry to database."
    menu['3']="See entries in database"
    menu['4']="Convert to XML." 
    menu['5']="Exit"

    while True: 
        options=menu.keys()
        print("======================================================")
        for entry in options: 
            print (entry, menu[entry])
        
        selection=input("Please Select:") 
        if selection =='1': 
            get_server_info()
        elif selection == '2': 
            print( "2 selected")
        elif selection == '3':
            print( "3 selected") 
        elif selection == '4':
            print("4 selected")
        elif selection == '5':     
            break
        else: 
            print( "Unknown Option Selected!") 

    
def get_server_info():
    
    print("======================================================")
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="core-consulting")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            
            cursor.close()
            connection.close()
            print("Connection Succesfull! PostgreSQL connection is closed")


if __name__ == "__main__":
    menu()
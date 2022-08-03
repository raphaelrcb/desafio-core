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
            getServerInfo()
        elif selection == '2': 
            addEntry()
        elif selection == '3':
            seeTable()
        elif selection == '4':
            tableToXML()
        elif selection == '5':     
            break
        else: 
            print( "Unknown Option Selected!") 
    
def getServerInfo():
    
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

def seeTable():
        # Connect to an existing database
    columnList = []
    print("======================================================")
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="core-consulting")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("SELECT column_name from information_schema.columns where table_name = 'pessoa'")
        columns = cursor.fetchall()

        for column in columns:
            columnList.append(column[0])

        cursor.execute("SELECT * FROM pessoa")
        rows = cursor.fetchall()

        print(columnList)
        print(rows)

        if (not rows) :
            print("tables is empty")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            
            cursor.close()
            connection.close()
            print("Connection Succesfull! PostgreSQL connection is closed")

def addEntry(): 

    columnList = []
    print("======================================================")
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="core-consulting")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("SELECT column_name from information_schema.columns where table_name = 'pessoa'")
        columns = cursor.fetchall()

        for column in columns:
            columnList.append(column[0])

        print("These are the entries you need to add:")
        print(columnList[1:])
        print("*Dates in format YYYY-MM-DD")

        records_to_insert = getInputs(columnList[1:])
        print(records_to_insert)
        
        psql_insert = "INSERT INTO pessoa (nome, nome_mae, local_nascimento, data_nascimento) VALUES (%s, %s, %s, %s)"
        cursor.execute(psql_insert, (records_to_insert))
        
        connection.commit()
        
        count = cursor.rowcount
        print(count, "Record inserted successfully into pessoa table")
    
    except (Exception, Error) as error:
        print( "Failed to insert record into pessoa table", error) 

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to DB closed")
    
def getInputs(columnList):

    inputs = []
    for col in columnList:
        print("type value for %s: ", col)
        inputs.append(input())

    print(inputs)
    return inputs

def tableToXML():

    columnList = []
    fileName   = 'pessoa.xml'
    print("======================================================")
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="core-consulting")

        cursor = connection.cursor()
        cursor.execute("SELECT column_name from information_schema.columns where table_name = 'pessoa'")
        columns = cursor.fetchall()

        for column in columns:
            columnList.append(column[0])

        cursor.execute("SELECT * FROM pessoa")
        rows = cursor.fetchall()

        outfile = open(fileName, 'w')

        outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        outfile.write('<pessoa>\n')

        for row in rows:
            outfile.write('\t<row>\n')
            for i in range(len(columnList)):
                outfile.write('\t\t<%s>%s</%s>\n' % (columnList[i], row[i], columnList[i]))
            outfile.write('\t</row>\n')
        outfile.write('</pessoa>\n')
        outfile.close() 


    except (Exception, Error) as error:
        print( "Cant connect to database", error) 

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to DB closed")


if __name__ == "__main__":
    menu()
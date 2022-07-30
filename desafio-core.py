import psycopg2
from psycopg2 import Error

def menu():

    menu = {}
    menu['1']="Check postgres server info." 
    menu['2']="Add entry to database."
    menu['3']="See entrie in database"
    menu['4']="Convert to XML." 
    menu['5']="Exit"

    while True: 
        options=menu.keys()
        print("======================================================")
        for entry in options: 
            print (entry, menu[entry])
        
        selection=input("Please Select:") 
        if selection =='1': 
            print( "1 selected") 
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

    


if __name__ == "__main__":
    menu()
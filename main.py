from dbFile.Database import Database
from utils.ErrorClass import ErrorClass

def pick():
    ErrorClass.data_type_error('your choice: ', int)

def menu():
    print("""
                Menu
        1. Insert Data
        2. Read Data
        3. Delete Data
        4. Search Data
        5. Exit
    """)


def main():
    db = Database()

    run = True

   while run:
        choose = pick()
        if choose == 1:
            firstName = input("What is your first name: ")
            lastName = input("What is your last name: ")
            password = input("What is your password")
            age = int(input("What is your age: "))
            address = input("What is your age: ")
            school = input("What school do you study: ")

            
            db.insert_data("persons", {'password': password, 'firstName' : firstName, 'lastName' : lastName,
                'age' : age, 'address' : address, 'school' : school})

            cont = input("Do you want to fill up your vital signs: ")


        elif choose == 2:

        elif choose == 3:

        elif choose == 4:

        elif choose == 5:
            run = False
        
        else:
            print("Invalid choice!, Please Try Again!")


if __name__ == '__main__':
    main()

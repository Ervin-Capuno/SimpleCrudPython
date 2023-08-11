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
        5. Update Data
        6. Exit
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

            
            cont = input("Do you want to fill up your vital signs[y/n]: ")
            
            if cont == 'y' or cont == 'Y':
                weight = int(input("What is your weight [kg]: "))
                height = int(input("What is your height [m]: "))
                BMI = weight / (height ** 2)
                personId = ""
                db.insert("vitalSigns", {'personId' : "" , 'weight' : weight, 'height' : height})
                print("Thank you for the fill-up!")
            else:
                break
        elif choose == 2:
            table = input("What table do you want to read: ")
            
            read = input("What do you want to read [y] for specific or [n] for all of the data")
            if(read.lower() == 'y'):
                db.read_data_all(table)
            elif(read.lower() == 'n'):
                db.read_data_all(table, 'vitalSigns', 'INNER JOIN', 'personId')
            else:
                print("Input cannot recognized!")
                break
        elif choose == 3:
            table = input("What table's data do you want to delete[persons/vitalSigns]")
            t_id = int(input("What id  do you want to delete"))
            if(table == 'persons'):
                del_data(table, t_id, "personId", t_id)
            elif(table == 'vitalSigns'):
                del_data(table, "personId", t_id)

        elif choose == 4:
            pass
        
        elif choose = 5:
            pass
        elif choose == 6:
            run = False
        
        else:
            print("Invalid choice!, Please Try Again!")


if __name__ == '__main__':
    main()

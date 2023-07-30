from dbFile.Database import Database
from utils.ErrorClass import ErrorClass

def pick():
    return int(input("What do you want do do: "))
    

def menu():
    print("""
                Menu
        1. Insert Data
        2. Read Data
        3. Delete Data
        4. Search Data
    """)


def main():
    name = input("What is your name: ")
    sanitized_name = Database.sanitize_input(name)
    print(sanitized_name)

if __name__ == '__main__':
    main()

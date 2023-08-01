import sqlite3
import re
from tabulate import tabulate

class Database:
    """
    A class representing a Database

    Args:
        db_name(str): the file name of the database where the data will directly stored
    
    Methods:
        insert_data: inserting the data to the database file
        read_data_all: read all the data
        show_tables: showing all the tables in the database file
        read_data_one: read specific data
        sanitized_input(staticmethod): sanitized the input to prevent sql injection
        del_data: delete the data from the database
        search_data: search the data from the database
        update_data: update the data from the database
        __str__: String representation of the Database object
        __repr__: Representation of the Database object

    """


    def __init__(self, db_name='myData.db'):
        """
        Initialize the Database class
        
        Args:
            db_name(str): name of the database 
        Example:
            db = Database() if there is an exist database
            db = Database('database.db') if there are no existing database
        """

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_data(self, table, data):
        """
        Inserting a data to the database

        Args:
            table(str): the name of the table to insert the data
            data(dict): the data that will insert on the table

        Example:
            users_table(str) : the table  
            'name', 'age', 'school'(str): the columsn of the table

            db.insert_data(users_table, { 'name' : 'ervin', 'age': 19, 'school' : 'school Address'})
        """

        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")
                
        table = Database.sanitize_input(table)
        data = {Database.sanitize_input(key): Database.sanitize_input(key) for key, value in data.items()}

        placeholders = ', '.join(['?' for item in data])
        columns = ', '.join(data.keys())
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        
        try:
            # Begin transaction
            self.conn.execute('BEGIN TRANSACTION')
            
            # Execute the query with the values
            self.cursor.execute(query, values)
            
            # Commit the transaction
            self.conn.commit()

        except Exception as e:
            # Rollback in case of an error
            self.conn.execute('ROLLBACK')
            print("An error occurred:", str(e))
        
        finally:
            # End the transaction
            self.conn.execute('END TRANSACTION')


    def read_data_all(self, table, table_join=None, type_of_join=None, name_of_PK=None):
        """
        Read all data from a specific table

        if table_join is specified the the condition and the name_of_PK must be specified

        Args:
            table(str): The name of the table
            tabe_join(str, optional): The name of the table to perform the joins
            type_of_join(str, optional): The condition where if it is inner join, left join, and right join
            name_of_PK(str, optional): The name of the primary key of the the two table

        Returns:
            list: A list of dictionaries, where each dictionary represents a row from the table.
                The keys of dictionary are the columns, and the values of dictionary is the data

        Example:
            Assuming there a table named 'users' with columns of 'name', 'age', and  'school'

            >>>db = Database('myData.db')
            >>>all_data = db.read_data_all('users')
            >>>print(all_data)
            [{'name': 'John', 'age': 30, 'address': 'New York'},
            {'name': 'John', 'age': 30, 'address': 'New York'},
            {'name': 'John', 'age': 30, 'address': 'New York'},
            {'name': 'John', 'age': 30, 'address': 'New York'},
            other rows
            ]

            To perform an inner join or any joining condition assuming there
            is another table named 'orders' and a primary key of userId
            >>>all_data_with_join = db.read_data_all('persons', 'orders', 'INNER JOIN', 'userId')

        """
        if table_join and type_of_join and name_of_PK:
            condition = f"{table}.{name_of_PK} = {table_join}.{name_of_PK}"
            query = f"SELECT * FROM {table} {type_of_join} {table_join} ON {condition}"
        else:
            query = f"SELECT * FROM {table}"

        try:
            self.cursor.execute(query)
            columns = [col[0] for col in self.cursor.execute.description]
            all_data = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            return all_data

            #header = all_data[0].keys()
            #table = [list(row.values) for row in all_data]
            #print(tabulate(table, headers=headers, tablefmt = "grid"))

        except Exception as e:
            print("An error occured  while reading the data", str(e))
            return []


    def show_tables(self):
        """
        Show all the tables of a database

        Output:
            string: name of the tables existed in the database
        """
        query = "SELECT * FROM sqlite_master WHERE type='table';"
        self.cursor.execute(query)
        tables = [table[0] for table in self.cursor.fetchall()]

        print("Tables in the Database")

        for table in tables:
            print(f"table")

    @staticmethod
    def sanitize_input(input_str):
        """
        Sanitize the input to prevent sql injection.

        Args:
            input_str(str): The input string to be sanitized.

        Returns: 
            str: The sanitized input string.
        """

        sanitized_input = re.sub(r"[^a-zA-Z0-9\s]", "", input_str)
        return sanitized_input


    def del_data(self, table, primary_key, data_to_be_deleted):
        """
        Delete a row from specific data  based n the primary key.

        Args:
            table(str): The name of the table from which data will be deleted
            primary_key(str): The value of the primary key that is uniquely identifiees the row
            data_to_be_deleted(str) : The data to be deleted

        """
        table = Database.sanitize_input(table)
        primary_key = Database.sanitize_input(primary_key)

        query = f"SELECT * FROM {table} WHERE {primary_key} = ?"

        try:
            self.cursor.execute(query, (data_to_be_deleted,))
            self.conn.commit()


            if self.cursor.rowcount > 0:
                print("The data is succesfully deleted!")
    
        except Exception as e:
            print("An error occured while deleting the data", str(e))

    def search_data(self, table, table_join = None, join_condition = None, primary_key = None, condition = None, data_to_search=None):
        """
        Search data from specific table with optional and custom conditions.

        Args:
            table(str):
            table_join(str):
            joinc_condition(str):
            primary_key(str):
            condition(str):

        """
        table = Database.sanitize_input(table)
        query = ""

        if condition:
            condition = Database.sanitize_input(condition)
            query = f"SELECT * FROM {table} WHERE {condition}"
        
        elif table_join and join_condition and primary_key:
            table_join = Database.sanitize_input(table_join)
            join_condition = Database.sanitize_input(join_condition)
            primary_key = Database.sanitize_input(primary_key)
            query = f"SELECT * FROM {table} {join_condition} {table_join} ON {table}.primary_key = {table_join}.primary_key"
        
        else:
            primary_key = Database.sanitize_input(primary_key)
            data_to_search = Database.sanitize_input(data_to_search)
            query = f"SELECT * FROM {table} WHERE {primary_key} = data_to_search"

        try:
            self.cursor.execute(query)
            column = [col[0] for col  in self.cursor.description]
            all_data = [dict(zip(column, row)) for row in self.cursor.fetachall()]
            
        except Exception as e:
            print(f"There was an error occured {e}")


        
        
    def update_data(self, table, data, condition = None):
        """
        Update data in a specific table with optional custom condition.

        Args:
            table(str): The name of the table to update.
            data(dict): A dictionary containing the column-value pairs to be upadated.
            condition(str, optional): The custom condition for updating in the table.
        """
        table = Database.sanitize_input(table)
        santized_data = {Database.sanitize_input(key): Database.sanitize_input(value) for key, value in data.items()}

        placeholders= ", ".join(f"{key} = ?" for key in sanitized_data)
        values = tuple(sanitized_data.values())

        query = f"UPDATE {table} SET {placeholders}"


        if condition:
            condition= Database.sanitize_input(condition)
            query += f"WHERE {condition}"


        try:
            self.conn.execute("BEGIN TRANSACTION")
            self.cursor.execute(query, values)
            self.conn.commit()

        exception Exception as e;
            self.conn.execute("ROLLBACK")
            print("An Error occurred while updating the data: ", str(e))

        finally:
            self.conn.execute('END TRANSACTION')

    def __str__(self):
        return f"Database({self.db_name})"

    def __repr__(self):
        return f"{type(self).__name__}(db_name='{self.db_name}')"

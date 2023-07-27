import sqlite3
import re

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

    def read_data_one(self):
        """
        Read a specific row of data 

        Returns:
            
        """
        pass

    def del_data(self, primary_key):
        pass

    def search_data(self, data, condition):
        pass

    def __str__(self):
        return f"Database({self.db_name})"

    def __repr__(self):
        return f"{type(self).__name__}(db_name='{self.db_name}')"

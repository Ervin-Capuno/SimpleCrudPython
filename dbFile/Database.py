import sqlite3

class Database:
    """
    A class representing a Database

    Args:
        db_name(str): the file name of the database where the data will directly stored
    
    Methods:
        insert_data: inserting the data to the database file
        read_data_all: read all the data 
        read_data_one: read specific data
        del_data: delete the data from the database
        search_data: search the data from the database
        __str__: String representation of the Database object
        __repr__: Representation of the Database object
    """


    def __init__(self):
        """
        Initialize the database class

        Args:
            db_name(str) -> the file name of the database where the data will directly stored
        """
        self.conn = sqlite3.connect('myData.db')
        self.cursor = self.conn.cursor()

    def insert_data(self, table, data):
        """
        Inserting a data to the database

        Args:
            table(str): the name of the table to insert the data
            data(dict): the data that will insert on the table
        """


        if not isinstance(table, str):
            raise ValueError("Table name must be a string.")
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        placeholders = ', '.join(['?' for _ in data])
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
        pass

    def read_data_all(self):
        pass

    def read_data_one(self):
        pass

    def del_data(self):
        pass

    def search_data(self):
        pass

    def __str__(self):
        return f"Database({self.db_name})"

    def __repr__(self):
        return f"{type(self).__name__}(db_name='{self.db_name}')"

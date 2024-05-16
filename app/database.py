import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file):
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            print(f"Connection to SQLite DB successful: {db_file}")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_query(self, query, parameters=()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, parameters)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query, parameters=()):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, parameters)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            return result

    def initialize_database(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS your_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            column1 TEXT NOT NULL,
            column2 TEXT NOT NULL
        );
        """
        self.execute_query(create_table_query)

        insert_data_query = """
        INSERT INTO your_table (column1, column2)
        VALUES
        ('Value 1', 'Value 2'),
        ('Value 3', 'Value 4');
        """
        self.execute_query(insert_data_query)

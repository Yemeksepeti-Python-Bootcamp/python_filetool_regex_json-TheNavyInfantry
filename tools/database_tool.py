import sqlite3
from sqlite3 import Error
from models.db_model import User
from datetime import datetime


class Db_tool(object):
    def __init__(self, db_name):
        """Initialize database name"""
        self.db_name = db_name

    def create_table_name(self):
        """Creates a table name with timestamp"""
        timestamp = datetime.strftime(datetime.now(), str("%Y%m%d_%H%M%S"))
        table_name = "data_" + timestamp

        return table_name

    def create_connection(self):
        """Creates a database connection to a SQLite database"""
        try:
            conn = sqlite3.connect(self.db_name) #Try to connect to the requested database
            return conn #Return connection if successfull

        except Error as e: #Return error message if any error occurs during connection
            return e

    def create_table(self):
        """Creates a table for the database"""
        conn = self.create_connection() #Try to connect to the requested database
        try:
            cur = conn.cursor() #Connect cursor with connection which is our operator for operations

            """Table query"""
            table_query = f"""CREATE TABLE {self.create_table_name()} (
                                email text,
                                username text,
                                name_surname text,
                                emailuserlk integer,
                                usernamelk integer,
                                doy integer,
                                dom integer,
                                dod integer,
                                state text,
                                a_p integer default 1);"""

            cur.execute(table_query) #Execute the given table query

        except Error as e: #Return error message if any error occurs during connection
            return e

        finally:
            conn.close() #Close connection to database

    def insert_data(self, user: User):
        """Inserts data to the table"""
        conn = self.create_connection() #Try to connect to the requested database
        try:
            """Insert query"""
            insert_query = f'''
            INSERT INTO {self.create_table_name()}
            (email,username,name_surname,emailuserlk,usernamelk, doy, dom, dod, state, a_p)
            VALUES (?,?,?,?,?,?,?,?,?,?)'''

            cur = conn.cursor() #Connect cursor with connection which is our operator for operations
            cur.execute(insert_query, (user.email, user.username, user.name_surname, user.emailuserlk, user.usernamelk,
                                       user.doy, user.dom, user.dod, user.state, user.a_p)) #Execute the given insert query
            conn.commit() #Commit ends a transaction within database

        except Error as e: #Return error message if any error occurs during connection
            return e

        finally:
            conn.close() #Close connection to database
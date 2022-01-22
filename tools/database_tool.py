import sqlite3
from sqlite3 import Error
from models.db_model import User
from datetime import datetime


class Db_tool(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table_name(self):
        timestamp = datetime.strftime(datetime.now(), str("%Y%m%d_%H%M%S"))
        table_name = "data_" + timestamp

        return table_name

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn

        except Error as e:
            return e

    def create_table(self):
        conn = self.create_connection()
        try:
            cur = conn.cursor()

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

            cur.execute(table_query)

        except Error as e:
            return e

        finally:
            conn.close()

    def insert_data(self, user: User):
        conn = self.create_connection()
        try:
            insert_query = f'''
            INSERT INTO {self.create_table_name()}
            (email,username,name_surname,emailuserlk,usernamelk, doy, dom, dod, state, a_p)
            VALUES (?,?,?,?,?,?,?,?,?,?)'''

            cur = conn.cursor()
            cur.execute(insert_query, (user.email, user.username, user.name_surname, user.emailuserlk, user.usernamelk,
                                       user.doy, user.dom, user.dod, user.state, user.a_p))
            conn.commit()

        except Error as e:
            return e

        finally:
            conn.close()
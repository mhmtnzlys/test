"""
This module consists ConnectMySql class
to create a database, table, drop them,
add data into table and delete it.
"""
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_DATA_HOST = os.environ.get("MYSQL_ACCESS_DATA_HOST")
ACCESS_DATA_USER = os.environ.get("MYSQL_ACCESS_DATA_USER")
ACCESS_DATA_PASSWORD = os.environ.get("MYSQL_ACCESS_DATA_PASSWORD")


class ConnectMySql(object):
    """The class consists methods to create databases and tables,
    to drop databases and tables, to show databases and tables,
    to insert new rows into tables and to give output of the tables."""

    def __init__(self):
        """This creates mysql connection and cursor."""
        self.conn = mysql.connector.connect(
            host=ACCESS_DATA_HOST,
            user=ACCESS_DATA_USER,
            password=ACCESS_DATA_PASSWORD)
        self.cursor = self.conn.cursor()

    def create_db(self, db_name):
        """This method creates the database if not exists
        given by the db_name parameter."""
        sql_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        self.cursor.execute(sql_query)
        return

    def delete_db(self, db_name):
        """This method deletes the database if exists
        given by the db_name parameter."""
        sql_query = f"DROP DATABASE IF EXISTS {db_name}"
        self.cursor.execute(sql_query)
        return

    def show_databases(self):
        """This method shows existed databases."""
        sql_query = "SHOW DATABASES"
        self.cursor.execute(sql_query)
        return [db[0] for db in self.cursor.fetchall()]

    def create_table(self, db_name, table_name):
        """This method creates tables inside the database
        given by db_name and table_name parameters."""
        sql_query = f"CREATE TABLE IF NOT EXISTS {db_name}.{table_name}" \
            + "(id INT NOT NULL AUTO_INCREMENT," \
            + "name VARCHAR(20)," \
            + "PRIMARY KEY (id))"
        self.cursor.execute(sql_query)
        return

    def delete_table(self, db_name, table_name):
        """This method deletes table inside the database
        given by db_name and table_name parameters."""
        sql_query = f"DROP TABLE IF EXISTS {db_name}.{table_name}"
        self.cursor.execute(sql_query)
        return

    def show_tables(self, db_name):
        """This method shows existed tables inside the database
        given by db_name parameter."""
        sql_query = f"SHOW TABLES FROM {db_name};"
        self.cursor.execute(sql_query)
        return [table[0] for table in self.cursor.fetchall()]

    def insert_table(self, db_name, table_name):
        """This method inserts rows into table which is inside
        the database given by parameters."""
        sql_query = f"INSERT INTO {db_name}.{table_name} (NAME)" \
            + "VALUES('TestName')"
        self.cursor.execute(sql_query)
        self.conn.commit()
        return

    def select_table(self, db_name, table_name):
        """This method gives output of the table which is inside
        the database given by parameters."""
        sql_query = f"SELECT * FROM {db_name}.{table_name}"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def close(self):
        """This method closes the database connection."""
        self.conn.close()
        return

a = ConnectMySql()
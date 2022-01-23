from tools.database_tool import Db_tool
from tools.json_tool import Json_tool
import argparse

"""
    Run the given code below in the CLI to run the project

    python3 main.py --file "dataregex.json" --db "dataregex.db"
"""

def main():

    parser = argparse.ArgumentParser() #Create the parser
    parser.add_argument("--file", type=str, required=True) #Add --file argument
    parser.add_argument("--db", type=str, required=True) #Add --db argument
    args = parser.parse_args() #Parse the argument

    file = args.file #Set file as argument
    db = args.db #Set db as argument

    try:
        file_process = Json_tool(file) #Calls -> "dataregex.json"
        db_process = Db_tool(db) #Calls -> "dataregex.db"
        db_process.create_table() #Create table
        access_user_data = file_process.create_user_from_data() #Access created users

        for each_user in access_user_data: #Iterate over accessed user data
            db_process.insert_data(each_user) #Insert those to the database

        print(f"NOTIFICATION: Both '{db}' created and '{file}' processed")

    except:
        print(f"NOTIFICATION: Neither '{db}' was created nor '{file}' was processed")

main()
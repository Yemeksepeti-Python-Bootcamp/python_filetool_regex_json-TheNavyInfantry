from tools.database_tool import Db_tool
from tools.json_tool import Json_tool
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--db", type=str, required=True)
    args = parser.parse_args()

    file = args.file
    db = args.db

    file_process = Json_tool(file) #"dataregex.json"
    db_process = Db_tool(db) #"dataregex.db"
    db_process.create_table()
    access_user_data = file_process.create_user_from_data()

    for each_user in access_user_data:
        db_process.insert_data(each_user)

main()
from tools.database_tool import Db_tool
from tools.json_tool import Json_tool

def main():

    file_process = Json_tool("dataregex.json")
    db_process = Db_tool("dataregex.db")
    db_process.create_table()
    access_user_data = file_process.create_user_from_data()

    for each_user in access_user_data:
        db_process.insert_data(each_user)

main()
from models.db_model import User
from tools.regex_tool import Regex_tool
import json


class Json_tool():

    def __init__(self, filename):
        self.filename = filename

    def get_json(self):
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)

            return data

    def create_user_from_data(self):
        json_data = self.get_json()
        rgx = Regex_tool()

        user_data = list()

        for data in json_data:
            user = User()
            user.email = data["email"]
            user.username = data["username"]
            user.name_surname = data["profile"]["name"]
            user.emailuserlk = rgx.email_validate(data["email"], data["username"])
            user.usernamelk = rgx.username_validate(data["username"], data["profile"]["name"])
            user.doy, user.dom, user.dod = rgx.birth_date_validate(data["profile"]["dob"])
            user.state = data.get("profile").get("address").split()[-1]

            user_data.append(user)

        return user_data
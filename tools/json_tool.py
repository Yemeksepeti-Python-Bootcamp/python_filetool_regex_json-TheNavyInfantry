from models.db_model import User
from tools.regex_tool import Regex_tool
import json

class Json_tool():

    def __init__(self, filename):
        """Initialize filename"""
        self.filename = filename

    def get_json(self):
        """Parse json and return parsed data"""
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)

            return data

    def create_user_from_data(self):
        """Creates user with parsed data"""
        json_data = self.get_json() #Calls parsed data
        rgx = Regex_tool() #Calls regex methods

        user_data = list() #Create a list for user data

        for data in json_data: #Iterate over parsed data
            user = User() #Calls database model
            user.email = data["email"] #Set email from parsed data
            user.username = data["username"] #Set username from parsed data
            user.name_surname = data["profile"]["name"] #Set name from parsed data
            user.emailuserlk = rgx.email_validate(data["email"], data["username"]) #Validate emailusrlk with email_validate and Set its value
            user.usernamelk = rgx.username_validate(data["username"], data["profile"]["name"]) #Validate usernamelk with username_validate and Set its value
            user.doy, user.dom, user.dod = rgx.birth_date_validate(data["profile"]["dob"]) #Split birth date as year(doy), month(dom), day(dod) with regex of birth_date_validate
            user.state = data.get("profile").get("address").split()[-1] #Access address and Set 'state' value

            user_data.append(user) #Append created user to the user_data list

        return user_data #Return created list that contains user data
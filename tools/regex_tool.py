import re

class Regex_tool():

    def birth_date_validate(self, birth_date):
        pattern = r'([0-9]{4})-([0-9]{2})-([0-9]{2})'
        match = re.search(pattern, birth_date)
        doy, dom, dod = match.group(1), match.group(2), match.group(3)

        return doy, dom, dod

    def email_validate(self, email, username):
        pattern_username = r'(^.{0,3})'
        match_username = re.search(pattern_username, username)
        username_group = match_username.group(1)

        pattern_email = r'\b([A-Za-z0-9._%+-]+)@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match_email = re.search(pattern_email, email)
        email_group = match_email.group(1)

        if username_group in email_group:
            return 1
        else:
            return 0

    def username_validate(self, username, name_surname):
        pattern = r"^\b(\w+)\b(.*)\b(\w+)\b"
        match = re.search(pattern, name_surname)
        name_group = match.group(1)

        return 0 if username.find(name_group.lower()) else 1
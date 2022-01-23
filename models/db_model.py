class User:
    def __init__(self, email="null", username="null", name_surname="null", emailuserlk=0,
                 usernamelk=0, doy=0, dom=0, dod=0, state="null", a_p=1):
        self.email = email
        self.username = username
        self.name_surname = name_surname
        self.emailuserlk = emailuserlk
        self.usernamelk = usernamelk
        self.doy = doy
        self.dom = dom
        self.dod = dod
        self.state = state
        self.a_p = a_p
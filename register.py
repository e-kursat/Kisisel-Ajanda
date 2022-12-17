from get_json import get_data
import json


class Register:

    def __init__(self, username: str, upassword: str, name: str, surname: str, email: str, user_type: str = "USER"):
        self.username = username
        self.upassword = upassword
        self.name = name
        self.surname = surname
        self.email = email
        self.user_type = user_type

        self.accounts = get_data()

        self.id = self.set_id()

        if self.id == None:
            self.id = 10
        else:
            self.id = self.set_id()

        self.accounts[self.username] = {}
        self.accounts[self.username]["id"] = self.id
        self.accounts[self.username]["name"] = self.name
        self.accounts[self.username]["surname"] = self.surname
        self.accounts[self.username]["email"] = self.email
        self.accounts[self.username]["upass"] = self.upassword
        self.accounts[self.username]["user_type"] = self.user_type

        # self.accounts[self.id] = {}
        # self.accounts[self.id]["name"] = self.name
        # self.accounts[self.id]["surname"] = self.surname
        # self.accounts[self.id]["uname"] = self.username
        # self.accounts[self.id]["upass"] = self.upassword
        # self.accounts[self.id]["email"] = self.email
        # self.accounts[self.id]["user_type"] = self.user_type

        with open('accounts.json', 'w') as user_json:
            json.dump(self.accounts, user_json)

    def set_id(self):
        data_accounts = get_data()

        try:
            max_id = int(max([data_accounts[account]['id']
                         for account in data_accounts]))
        except:
            return None
        else:
            user_id = max_id + 1

        return user_id

    @classmethod
    def with_id(cls, username: str, upassword: str, name: str, surname: str, email: str, user_type: str, id: str):
        return cls(username, upassword, name, surname, email, user_type, id)


# Register("a", "b", "c", "d", "e")
# Register("x", "y", "z", "w", "m")

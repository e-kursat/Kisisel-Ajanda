from get_json import get_data
from admin import Admin
from premium import Premium


class Login:
    def __init__(self, uname, upass):
        self.uname = uname
        self.upass = upass

        self.status = False

        accounts_data = get_data()

        # for id in accounts_data:
        #     if uname == accounts_data[id]['uname'] and upass == accounts_data[id]['upass']:
        #         print("giriş başarılı!")

        #         self.status = True
        #         break

        if self.uname in accounts_data:
            if self.upass == accounts_data[self.uname]['upass']:
                print("Giriş başarılı!")
                self.status = True

                if accounts_data[self.uname]['user_type'] == "ADMIN":
                    Admin()
                    
                if accounts_data[self.uname]['user_type'] == "PREMIUM":
                    Premium()
            else:
                print("Hatalı şifre!")
        else:
            print("Bu kullanıcı adına sahip bir kullanıcı bulunamamaktadır!")

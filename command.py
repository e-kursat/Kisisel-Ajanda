from register import Register
from login import Login
from get_json import get_data


class Command:

    def __init__(self, process_type: str, command: int):
        self.process_type = process_type
        self.command = command

        self.status = False

        if process_type == "main":
            self.main_check_command()

        elif process_type == "admin":
            self.admin_check_command()

        elif process_type == "premium":
            self.premium_check_command()

    @staticmethod
    def main_screen():
        print('-'*20)
        print("1 - Giriş yap.")
        print("2 - Kayıt ol.")
        print("0 - Ekranı kapat.")
        print('-'*20)

    def main_check_command(self):
        # Close screen
        if self.command == 0:
            print("İşlem sonlandırıldı..")

        # login
        elif self.command == 1:
            self.status = self.login()

        # register
        elif self.command == 2:
            self.register()

        else:
            print("Hatalı seçim!")

    @staticmethod
    def admin_screen():
        print('-'*20)
        print("1 - Admin ekle.")
        print("2 - Premium kullanıcı ekle.")
        print("0 - Ekranı kapat.")
        print('-'*20)

    def admin_check_command(self):
        # close screen
        if self.command == 0:
            print("İşlem sonlandırıldı..")

        # register
        elif self.command == 1:
            self.register()

        elif self.command == 2:
            self.register()

    @staticmethod
    def premium_screen():
        print('-'*20)
        print("1 - Plan oluştur.")
        print("2 - Plan sil.")
        print("0 - Ekranı kapat.")
        print('-'*20)

    def premium_check_command(self):
        # close screen
        if self.command == 0:
            print("İşlem sonlandırıldı..")

        # create a plan
        elif self.command == 1:
            pass

        # delete a plan
        elif self.command == 2:
            pass

    def register(self):
        accounts_data = get_data()

        name = str(input("İsim: "))

        while True:
            if len(name) < 2:
                print("Lütfen, minimum 2 karakter giriniz!")
                name = str(input("İsim: "))
            else:
                break

        surname = str(input("Soyisim: "))

        while True:
            if len(surname) < 2:
                print("Lütfen, minimum 2 karakter giriniz!")
                surname = str(input("Soyisim: "))
            else:
                break

        email = str(input("Email: "))

        is_have_mail = False

        while True:
            for account in accounts_data:
                if email == accounts_data[account]['email']:
                    is_have_mail = True
                    break
                else:
                    is_have_mail = False

            if '@' in email:
                if is_have_mail == False:
                    break
                else:
                    print("Bu mail ile kayıtlı bir hesap bulunmaktadır!")
                    print("Lütfen başka bir mail giriniz.")
                    email = str(input("Email: "))
            else:
                print("Lütfen geçerli bir mail giriniz!")
                email = str(input("Email: "))

        username = str(input("Kullanıcı adı: "))

        is_have_uname = False

        while True:
            for account in accounts_data:
                if username == account:
                    is_have_uname = True
                    break
                else:
                    is_have_uname = False

            if len(username) >= 5:
                if is_have_uname == False:
                    break
                else:
                    print("Bu kullanıcı adıyla kayıtlı bir hesap bulunmaktadır!")
                    print("Lütfen başka bir kullanıcı adı giriniz.")
                    username = str(input("Kullanıcı adı: "))
            else:
                print("Lütfen, minimum 5 karakter giriniz!")
                username = str(input("Kullanıcı adı: "))

        password = str(input("Şifre: "))

        while True:
            if len(password) < 5:
                print("Lütfen, minimum 5 karakter giriniz!")
                password = str(input("Şifre: "))
            else:
                break

        # USER TYPE
        if self.process_type == "main":
            Register(username, password, name, surname, email)

        # ADMIN TYPE
        elif self.process_type == "admin" and self.command == 1:
            Register(username, password, name, surname, email, "ADMIN")

        # PREMIUM TYPE
        elif self.process_type == "admin" and self.command == 2:
            Register(username, password, name, surname, email, "PREMIUM")

    def login(self):
        username = str(input("Kullanıcı adı: "))
        password = str(input("Şifre: "))

        acc = Login(username, password)

        if acc.status == True:
            return True

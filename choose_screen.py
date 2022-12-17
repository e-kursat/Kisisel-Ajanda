from command import Command


def screen(screen_type):
    while True:

        # Show menu
        if screen_type == "main":
            Command.main_screen()

        elif screen_type == "admin":
            Command.admin_screen()

        elif screen_type == "premium":
            Command.premium_screen()

        try:
            choose = int(input("Yapmak istediğiniz işlem: "))
        except:
            print("Rakam girmelisiniz!")
        else:
            check = Command(screen_type, choose)

            if choose == 0:
                break

            if check.status == True:
                break

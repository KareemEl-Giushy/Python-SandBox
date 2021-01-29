# ------------------------
# Login And Admin Thing #
# ------------------------

admins = ['kareem', 'mohammed', 'ibraheem']

name = input("Enter You're Login Name: ").strip().lower()

if name in admins:
    print(f"Hello {name}. You're An Admin")
    option = input("Del / Update: ").strip().lower()
    if option == "del" or option == 'delete':
        admins.remove(name)
        print("Name Deleted !!")
        print(admins)
    elif option == "update" or option == "up":
        newName = input("Enter Your New Name: ")
        admins[admins.index(name)] = newName
        print("Name Updated !!")
        print(admins)
    else:
        print("Command Not Found :(")
else:
    print("You Don't Have Access :(")
    answer = input("You Want To Be an admin (y / N): ".title()).strip().lower()
    if answer == 'yes' or answer == 'y':
        admins.append(name)
        print("you Were Added to admins :)")
        print(admins)
    else:
        exit()
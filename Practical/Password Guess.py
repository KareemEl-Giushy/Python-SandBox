# ------------------------
#  Simple Password Guess#
# ------------------------

tries = 4

mainPassword = "kareem123"

while tries > 0:
    inputPassword = input("Write Your Password: ").strip()
    
    if inputPassword == mainPassword and tries == 4:
        print("In The First Guess , Me3alem ;)")
        break
    elif inputPassword == mainPassword:
        print("That Is The Right Guess :) :0 ....")
        break
    else:
        print("Bad Guess :_ ....")
        print(f"You Have [{tries-1 if tries-1 != 0 else 'No'}] Tries Left")
    
    tries -= 1
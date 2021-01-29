# ------------------------
# Bookmark app for websites #
# ------------------------

tries = 5

while tries >= 1:

    try:
        print("Enter A Valid Absoulute Path To Open The File")
        print("-You Have [{}] tries".format(tries))
        
        thepath = input("Enter Path:\n").strip()
        
        thefile = open(thepath, "r")

        print("-->> The File Says :")
        print(thefile.read())
        thefile.close()
    
    except FileNotFoundError:
        print("That's Enough. Exist, Sorry") if tries == 1 else print("The File Not Found(404) Try Again, Please")
        print("=" * 20)
    
    except:
        print("There An Unknown Error :( ...")
    else:
        break
    
    finally:
        tries -= 1
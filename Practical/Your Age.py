# ------------------------
# Calculate Your Age (Advanced) #
# ------------------------

age = int(input("What is Your Age ?\n").strip())

unit = input("Please Enter The Unit (Month, Weeks, Days, Hours, Minutes, Seconds)(m, w, d, h, u, s): ").strip().lower()

if unit == "m" or unit == "months":
    print("Your Age In Months: %0.3f \n" % (age * 12))
elif unit == "w" or unit == "weeks":
    print("Your Age In Weeks: %0.3f \n" % (age * 12 * 4))
elif unit == "d" or unit == "days":
    print("Your Age In Days: %0.3f \n" % (age * 365.25))
elif unit == "h" or unit == "hours":
    print("Your Age In Hours: %0.3f \n" % (age * 12 * 4 * 24))
elif unit == "u" or unit == "minutes":
    print("Your Age In Minutes: %0.3f \n" % (age * 12 * 4 * 24 * 60))
elif unit == "s" or unit == "seconds":
    print("Your Age In Seconds: %0.3f \n" % (age * 12 * 4 * 24 * 60 * 60))
else:
    print("You Entered An Invalid Unit ...")
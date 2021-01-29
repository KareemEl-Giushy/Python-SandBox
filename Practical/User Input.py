# ------------------------
# User INput #
# ------------------------
fname = input("First Name: ").strip()
mname = input("Middle Name: ").strip()
lname = input("Last Name: ").strip()

print("your full name is %s" % (fname + " " + mname[:1] + " " + lname).title())
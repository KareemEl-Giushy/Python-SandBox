# ------------------------
# User INput # Your Age
# ------------------------

age = int(input("What is your age ? ").strip())

months = age * 12
weeks = months * 4
days = age *365.25
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("you lived for :\nmonths {} \nweeks {} \ndays {} \nhours {} \nminutes {} \nseconds {}".format(months, weeks, days, hours, minutes, seconds))
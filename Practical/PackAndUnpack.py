# ------------------------
# Function ... & Pack & Unpack Training#
# ------------------------
mySkills = {
    "Python": '50%',
    "MySQL": "71%",
    "MongoDB": "78%"
}

def show_mySkills(name, *skills, **skillsP):
    print("Hello Eng.{:s}".format(name))
    if bool(skills):
        print("Skills Without Progress Is:")
        for skill in skills:    
            print("=> " + skill.capitalize())
        print('=' * 50)
    if bool(skillsP):
        print("Skills With Progress:")
        for skill, value in skillsP.items():
            print(skill + " => " + value)

show_mySkills("El-Giushy", "Html", "Css", "js", "php", "laravel", **mySkills, R="0%")

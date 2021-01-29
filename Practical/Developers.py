# ------------------------
# Nested Loop #
# ------------------------

# Nested for Loop
developers = {
    "Kareem": {
        "Python": "80%",
        "PHP": "90%",
        "SQL": "70%",
        "C#": "85%"
    },
    "Sayed": {
        "Python": "10%",
        "PHP": "70%",
        "SQL": "50%",
        "C#": "99%"
    },
    "Mahmoud": {
        "HTML/HTML5": "80%",
        "CSS": "90%",
        "SQL": "70%",
        "C#": "85%"
    },
}

item = input("Enter Compare Skill: ").strip().lower()
top = ["none", 0]

for dev in developers:
    print("- Eng." + dev)
    for skill in developers[dev]:
        progress = developers[dev][skill] 
        print(skill + " => " + progress)

        if skill.lower() == item:
            if int(progress.replace("%", "")) > top[1]:
                top[0] = dev
                top[1] = int(progress.replace("%", ""))
else:
    print(f"The Top {item} Developer Is {top[0]} With Score Of {top[1]}%".title())
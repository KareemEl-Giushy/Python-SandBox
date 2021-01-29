# ------------------------
# Function ... Recursion#
# ------------------------

# test [wworrrlddd]

def removeExtra(word):
    if len(word) <= 1:
        return word
    print(word.center(len(word) + 4,"#"))
    if word[0] == word[1]:
        return removeExtra(word[1:])
    print(word.center(len(word) + 4, "$"))
    return word[0] + removeExtra(word[1:])


print(removeExtra("wwooooorrrlddd"))
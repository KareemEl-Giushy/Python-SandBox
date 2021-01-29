# ------------------------
# Bookmark app for websites #
# ------------------------

bookmarks = []

maxMarks = int(input("Enter How Many Bookmarks?: ").strip())

while maxMarks > 0:
    website = input("Enter Website https://").strip().lower()
    if website not in bookmarks:
        bookmarks.append(website)
        print("Website Added")
        maxMarks -= 1
    else:
        print("Website Already added")


print(bookmarks)
print("Bookmarks Is Full you can't add more".title())
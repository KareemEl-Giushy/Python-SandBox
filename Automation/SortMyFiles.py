# ------------------------
# Sort My Folders Python#
# ------------------------
import os
import shutil

# print(os.getcwd())
# myPath = r"C:\Users\AUC\Documents\PyProjects\fileTests/"
# print(os.getcwd() + r"\fileTests/" + "1" + ".jpg")

myPath = input("Enter A Path To Clean: \n").strip() + "/"

if bool(myPath) and not myPath.isspace() and os.path.isdir(myPath):
    pass
else:
    print("Not Executed. Double Check Your Path")
    exit()


# My Extentions
texts = ('txt', 'doc', 'docx', 'pdf', 'rtf', 'odt')

imgs = ('jpg', 'jpeg', 'png', 'gif', 'jfif')

videos = ('mp4', 'mkv', 'avi', 'mov', 'wmv', 'webm')

audios = ('mp3', 'wav')

comps = ("rar","zip")

exes = ('exe', 'msi')

for f in os.listdir(myPath):
    # print(f) if f.endswith(imgs) else "" # Testing
    if f.endswith(imgs):
        os.mkdir(myPath + "[kareem]Images") if not os.path.exists(myPath + "[kareem]Images") else ""
        shutil.move(myPath + f, myPath + "[kareem]Images")
        # shutil.copy(myPath + f, myPath + "Images")
        # os.remove(myPath + f)
        print("Image Done...")
    
    if f.endswith(texts):
        os.mkdir(myPath + "[kareem]Docs") if not os.path.exists(myPath + "[kareem]Docs") else ""
        shutil.move(myPath + f, myPath + "[kareem]Docs")
        # shutil.copy(myPath + f, myPath + "Docs")
        # os.remove(myPath + f)
        print("Document Done...")

    if f.endswith(videos):
        os.mkdir(myPath + "[kareem]Vids") if not os.path.exists(myPath + "[kareem]Vids") else ""
        shutil.move(myPath + f, myPath + "[kareem]Vids")
        # shutil.copy(myPath + f, myPath + "Vids")
        # os.remove(myPath + f)
        print("Video Done...")

    if f.endswith(audios):
        os.mkdir(myPath + "[kareem]Sound") if not os.path.exists(myPath + "[kareem]Sound") else ""
        shutil.move(myPath + f, myPath + "[kareem]Sound")
        # shutil.copy(myPath + f, myPath + "Sound")
        # os.remove(myPath + f)
        print("Audio Done...")

    if f.endswith(comps):
        os.mkdir(myPath + "[kareem]Comps") if not os.path.exists(myPath + "[kareem]Comps") else ""
        shutil.move(myPath + f, myPath + "[kareem]Comps")
        # shutil.copy(myPath + f, myPath + "Comps")
        # os.remove(myPath + f)
        print("Compressed Done...")

    if f.endswith(exes):
        os.mkdir(myPath + "[kareem]Programs") if not os.path.exists(myPath + "[kareem]Programs") else ""
        shutil.move(myPath + f, myPath + "[kareem]Programs")
        # shutil.copy(myPath + f, myPath + "Comps")
        # os.remove(myPath + f)
        print("Installer Done...")

    if f.endswith("iso"):
        os.mkdir(myPath + "[kareem]Iso") if not os.path.exists(myPath + "[kareem]Iso") else ""
        shutil.move(myPath + f, myPath + "[kareem]Iso")
        # shutil.copy(myPath + f, myPath + "Comps")
        # os.remove(myPath + f)
        print("Iso Done...")

else:
    print("Done. Enjoy :)")
# ------------------------
# Sort My Folders Python#
# ------------------------
import os
import shutil

print(os.getcwd())
myPath = r"C:\Users\AUC\Documents\PyProjects\fileTests/"
# print(os.getcwd() + r"\fileTests/" + "1" + ".jpg")

# Create Junk Files
# for n in range(5):
#     open(os.getcwd() + r"\fileTests/" + str(n) + ".mp3", "x")

# My Extentions
texts = ('txt', 'doc', 'docx', 'pdf', 'rtf', 'odt')

imgs = ('jpg', 'jpeg', 'png', 'gif')

videos = ('mp4', 'mkv', 'avi', 'mov', 'wmv')

audios = ('mp3', 'wav')

comps = ("rar","zip")

for f in os.listdir(myPath):
    # print(f) if f.endswith(imgs) else "" # Testing
    if f.endswith(imgs):
        os.mkdir(myPath + "Images") if not os.path.exists(myPath + "Images") else ""
        # shutil.move(f, myPath + "/Images")
        shutil.copy(myPath + f, myPath + "Images")
        os.remove(myPath + f)
    
    if f.endswith(texts):
        os.mkdir(myPath + "Docs") if not os.path.exists(myPath + "Docs") else ""
        # shutil.move(f, myPath + "/Images")
        shutil.copy(myPath + f, myPath + "Docs")
        os.remove(myPath + f)

    if f.endswith(videos):
        os.mkdir(myPath + "Vids") if not os.path.exists(myPath + "Vids") else ""
        # shutil.move(f, myPath + "/Images")
        shutil.copy(myPath + f, myPath + "Vids")
        os.remove(myPath + f)
    
    if f.endswith(audios):
        os.mkdir(myPath + "Sound") if not os.path.exists(myPath + "Sound") else ""
        # shutil.move(f, myPath + "/Images")
        shutil.copy(myPath + f, myPath + "Sound")
        os.remove(myPath + f)

    if f.endswith(comps):
        os.mkdir(myPath + "Comps") if not os.path.exists(myPath + "Comps") else ""
        # shutil.move(f, myPath + "/Images")
        shutil.copy(myPath + f, myPath + "Comps")
        os.remove(myPath + f)

import os
import sys
import shutil
import exts


def organize_folder(folder):
    files = set(os.listdir(folder))
    if files == []:
        return
    if "Audio" not in files:
        os.mkdir(folder+"/Audio")
    if "Video" not in files:
        os.mkdir(folder+"/Video")
    if "Documents" not in files:
        os.mkdir(folder+"/Documents")
    if "Softwares" not in files:
        os.mkdir(folder+"/Softwares")
    if "Compressed" not in files:
        os.mkdir(folder+"/Compressed")
    if "Other" not in files:
        os.mkdir(folder+"/Other")

    for file in files:
        extension = os.path.splitext(file)[1]
        if extension == "":
            continue
        else:
            extension = extension.lower()
            if extension in exts.audio:
                shutil.move(folder+"/"+file, folder+"/Audio")
            elif extension in exts.video:
                shutil.move(folder+"/"+file, folder+"/Video")
            elif extension in exts.docs:
                shutil.move(folder+"/"+file, folder+"/Documents")
            elif extension in exts.soft:
                shutil.move(folder+"/"+file, folder+"/Softwares")
            elif extension in exts.comp:
                shutil.move(folder+"/"+file, folder+"/Compressed")
            else:
                shutil.move(folder+"/"+file, folder+"/Other")


def validate(folder):
    if (os.path.splitext(folder)[1] != ""):
        print("hhh")
        return 0
    else:
        if(folder[len(folder)-1] == '/' or folder[len(folder)-1] == '\\'):
            folder = folder[0:len(folder)-1]
        return folder


if __name__ == '__main__':
    l = len(sys.argv)
    if l == 1:
        organize_folder(".")
    elif l == 2:
        res = validate(sys.argv[1])
        if(res != 0):
            organize_folder(res)
    else:
        print("!!!Enter folder path to organize.!!!")
        exit(0)

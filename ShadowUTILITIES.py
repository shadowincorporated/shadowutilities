import hashlib
from tkinter import *
from PIL import ImageTk, Image #Pillow
from io import BytesIO
from contextlib import *
from pathlib import Path
import glob
import os
import stat
import shutil
from subprocess import call
import requests #requests
import ctypes
import git #GitPython

ver = "0.01.2"
versionurl = "https://raw.githubusercontent.com/shadowincorporated/shadowutilities/main/ver.ignore" #You put the version link here

def staffhandbookopen():
    os.startfile("other\\staffhandbook.rtf")

def discordinvite():
    print("test")

def _pass_corr():
    pass0 = pas.get()
    password = (str(pass0))
    hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if hash == "8700e5c43f40736dc9497c40ea3acdc7626748a7f5f80d0b385d4ccaad3ca60e":
        print("Password Correct")

        root2 = Toplevel()

        root2.resizable(False, False)

        root2.iconbitmap("icons/ico.ico")

        root2.title("ShadowUTILITIES")

        canvas2 = Canvas(root2, width=600, height=700)
        canvas2.pack()

        button1 = Button(root2,text="staff handbook", command=staffhandbookopen, width=40, height=1)
        button1.place(x= 10, y=50)

        button2 = Button(root2,text="discord", command=discordinvite, width=40, height=1)
        button2.place(x= 10, y=90)

        Label2 = Label(root2, text="TICKET NOTES:")
        Label2.place(x=10, y=350)

        notes = Text(root2, height=10, width=40)
        notes.place(x=10, y=400)

        label1 = Label(root2, text="ShadowUTILITIES")
        label1.place(x=200, y=10)
    else:
        print("incorrect password")
        root.quit()

def on_rm_error(func, path, exc_info):
    #from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def unhide(dir):
    for i in os.listdir(dir):
        if i.endswith('git'):
            tmp = os.path.join(dir, i)
            # We want to unhide the .git folder before unlinking it.
            while True:
                call(['attrib', '-H', tmp])
                break
            shutil.rmtree(tmp, onerror=on_rm_error)


def _attempt_update():
    print("Attempting Update")
    root.quit()
    github_repo = git.Repo.clone_from('https://github.com/shadowincorporated/shadowutilities', 'shadowutilities-https')
    
    repo_folder = os.curdir+'/shadowutilities-https'
    target_dir = os.curdir

    unhide(repo_folder)
    file_names = os.listdir(repo_folder)
        
    for file_name in file_names:
        if (file_name.find(".ignore") == -1 and file_name.find(".git") == -1):
            shutil.move(os.path.join(repo_folder, file_name), target_dir)
    
    shutil.rmtree(repo_folder, True)

def internet_connection():
    try:
        response = requests.get(versionurl, timeout=5)
        return True
    except requests.ConnectionError:
        root.quit()
        return False    

root = Tk()
root.resizable(False, False)
root.iconbitmap("icons/ico.ico")
root.title("ShadowUTILITIES Login")

canvas = Canvas(width=500, height=500)
canvas.pack()

label1 = Label(root, text="ShadowUTILITIES Login")
label1.place(x=200, y=10)

pas = Entry(root, show='*')
pas.place(x=10, y=80)
pas.focus_set()

label2 = Label(root, text="PASSWORD:")
label2.place(x=10, y=50)

label3 = Label(root, text="NOTE: FAILED PASSWORD WILL CLOSE PROGRAM")
label3.place(x=10, y=130)

enter = Button(root, text="Enter", command=_pass_corr)
enter.place(x=160, y=75)

if internet_connection():
    page = requests.get(versionurl)

    print("Current Version: ", str.split(ver), "GitHub Repo Version:", str.split(page.text))

    if (str.split(ver) == str.split(page.text)):
        print("ShadowUTILITIES is up-to-date!")
    else:
        update = Button(root, text="Update", command=_attempt_update, fg='yellow', bg='red')
        update.place(x=210, y=75)
        ctypes.windll.user32.MessageBoxW(0, u"ShadowUTILITIES needs an update!", u"Update Available", 0)

root.mainloop()
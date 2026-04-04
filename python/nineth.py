from pathlib import Path
import os
def readfile():
    pathv= Path('')     #yea basically '' current dirctionary deta
    items=list(pathv.rglob('*')) #rg means regursive glob ,it is a fx for finding files and dir
    for i,items in enumerate(items):    #alag alag index values
      print(f"{i+1} : {items}")

def deletefile():
    try:
        readfile()
        name=input("which file you want to delete")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("file remove succesfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"A error occured as{err}")

def updatefile():
    try:
        readfile()
        name=input("which file you want to update")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file")
            print("press 2 for overwriting the data of your life")
            print("press 3 for appending some content in file")

            response=int(input("tell your response:-"))

            if response==1:
                name2=input("yell you new file name:-")
                p2=Path(name2)
                p.rename(p2)

            if response==2:
                with open(p,'w') as fs:
                    data=input("tell what u want to write this will overwrite")
                    fs.write(data)

            if response==3:
                with open(p,'a') as fs:
                    data=input("tell what u want to append")
                    fs.write(" "+data)
    except Exception as err:
        print(f"A error occured as{err}")


def readsfile():
    try:
        readfile()
        name=input("which file you want to read")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data =fs.read()
                print(data)

            print("Readed successfully")
        else:
            print("file doesnot exist")
    except Exception as err:
        print(f"A error occured as{err}")

def createfile():
    try:
        readfile()
        name=input("please tell your file name:-")
        p=Path(name)
        if not p.exists() :
            with open(p,"w") as fs:
                data=input("what you want to write in this file:-")
                fs.write(data)

            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("this file aready exist")
    except Exception as err:
        print(f"A error occured as{err}")

print("press1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating file")
print("press 4 for deletion a file")

check=int(input("please tell  your response:-"))
if check==1:
   createfile()

if check==2:
    readsfile()

if check==3:
    updatefile()

if check==4:
    deletefile()
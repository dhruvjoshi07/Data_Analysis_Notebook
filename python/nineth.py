from pathlib import Path
def readfile():
    pathv= Path('')     #yea basically '' current dirctionary deta
    items=list(pathv.rglob('*')) #rg means regursive glob ,it is a fx for finding files and dir
    for i,items in enumerate(items):    #alag alag index values
      print(f"{i+1} : {items}")

def re
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
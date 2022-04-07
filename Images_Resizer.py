from ast import Delete
from fileinput import filename
from sre_constants import JUMP
from PIL import Image
import sys
import os

directoryIn = 'input'       #directories for pictures before and after the job
directoryOut = 'output'
directoryFailed = 'failed'

class Img_prop:
    def __init__(self,height,width,maxSize):
        self.height=int(height)     #in pixles
        self.width=int(width)       #in pixles
        self.maxSize=int(maxSize)   #in KB

def main():
    checkDirs()
    print("\nEnter image limitations: ")
    imageProp = Img_prop(input("Max height: "),input("Max width: "),input("Max size (in KB): "))
    print("max size: ",imageProp.maxSize)
    print("\n")
    #iterate over the directory 'input'
    for filename in os.listdir(directoryIn):        #foreach file in directory
        f = os.path.join(directoryIn, filename)     
        if os.path.isfile(f):   #if file exists
            doFile(f,imageProp)

def doFile(picname,imageProp):
    qual = 95   #maximum quality
    print("\n>Working on [",picname.split("\\")[1],"]")  #for debbuging
    newname = changeType(picname)               #change file type
    image = Image.open(picname)                 #open oroginal photo
    image.save(newname)                         #save the new photo as a copy
    imageNew = Image.open(newname)              #open the copy
    imageNew.thumbnail((imageProp.height,imageProp.width))     #resize
    imageNew.save(newname,quality = qual)       #save
    while ((os.path.getsize(newname)/1000 > imageProp.maxSize) and qual > 10):   #change quality if needed       
        os.remove(newname)                                          #if too big then delete
        qual -= 5                                                   #decrease a bit the quality
        imageNew.save(newname,quality = qual)                       #save again 
                                    
    if(os.path.getsize(newname)/1000 > imageProp.maxSize):
        addFailed(newname,qual)     
    else:
        print("Succsessfully created: ",newname," [size:",os.path.getsize(newname)/1000,"KB , quality:",qual+5,"%]")
    

def changeType(picname):

    ret_name = list("output\\"+picname.split("\\")[1])  #add one char buffer at the begging to fit new directoy name
    length = len(ret_name)
    
    ret_name[length-3]='j'  #change file's type
    ret_name[length-2]='p'
    ret_name[length-1]='g'
    ret_name = "".join(ret_name)    #make sure saved as string

    return ret_name

def addFailed(picname,quality):
    answer = ""
    print("File: ",picname.split("\\")[1],"Failed! it's quality too low :( ")
    print("   quality:",quality+5,"% , size: ",os.path.getsize(picname)/1000,"KB\n")    
    while ( answer!="Y" and answer!="y" and answer!="N" and answer!="n" ):
        answer = input("\nStill create it in low quality? [Y \ N]:")
        if(answer == 'Y' or answer == 'y'):
            print("YES")            
        elif (answer == 'N' or answer == 'n'):
            print("NO")
            image = Image.open(picname)
            image.save("failed\\"+picname.split("\\")[1])
            os.remove(picname)          
        else:
            print("Havent typed good answer !")

def checkDirs():
    #create directories if needed
    f_dir_in = f_dir_out = f_dir_fail = False
    for dirname in os.listdir("./"):        #foreach file in directory
        f = os.path.join("",dirname) 
        if (os.path.isdir(f)):
            if f==directoryIn:
                f_dir_in=True
            elif f==directoryOut:
                f_dir_out = True
            elif f==directoryFailed:
                f_dir_fail = True
    
    if(not f_dir_in):
        os.mkdir(directoryIn)
        print("*create 'input' directory ")
    if(not f_dir_out):
        os.mkdir(directoryOut)
        print("*create 'output' directory ")
    if(not f_dir_fail):
        os.mkdir(directoryFailed)
        print("*create 'failed' directory ")

if __name__ == "__main__":
        main()

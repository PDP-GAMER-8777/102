import shutil
import os

from_Dir : r"C:\Users\\sai\\Desktop\\prathamesh whitehat .jr\\Python\\project 102"
to_Dir:""

list_of_files:os.listdir(from_Dir)
print(list_of_files)
for file_Name in list_of_file:
   name,extention= os.path.splitext(file_Name) 

   if extention =='':
     continue 
   if extention in [ ".txt, .doc, .docx, .pdf"]: 

             
    path1 = from_Dir + "/" + file_Name
    path2 = to_Dir + '/' + "Images_Files"       
    path3 = to_Dir + '/' + "Images_Files" + file_Name
    print("path1",path1)
    print("path3",path3)

    if os.path.exists(path2):
     print("Moveing" + file_Name + ".....")
     shutil.move(path1,path3)
    else:
     os.makedirs(path2)   
     print("Moveing" + file_Name + ".....")
     shutil.move(path1,path3)



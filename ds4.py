print("something in console")

#commands for jupiter and windows
#!ls=will lest down all the directories in the present working directory
#pwd() will display the present working directory
#1st way(Recommended)
# f=open("test.txt","w")
# f.write("This is my first file operation to write something in this file")

#2nd way(Not recommended)
# %%writefile test2.txt
#this is what i would like to store in my file
#to read the data in the file
# f=open("test1.txt")#by default mode is 'r'
# f.read()
# if i have opened a file in read mode and performing write operation
#Unsupported operation error will pop up
#f.seek(5):will reset the cursor while read operation at 5th position
#if you need to read from start "f.seek(0)" needs to be applied
#to know at which position the cursor is "f.tell" is used
#f.read():will read the whole data
#f.readline():will read the data line by line  
#f.readlines():will give the info in a list and every line is treated a
#as an object
#len(f.readlines())
# l[0].split() will give list of words in the first line of the 
# paragraph
#to get the list of first character of all the words availble in the paragraph
# l1=[]
# for i in l[0].split:
#     l1.append(i[0])


# %%
#r+: will open the file in both read and write mode
#%%

# l=["hi , line1","hi , line2","hi , line3","hi , line4"]
# f.writelines(l)
# f.fileno()

# To delete a File
# import os
# os.remove("test12.txt")#to delete the file
# os.getcwd()
# os.listdir()
#there is a directory , inside which there are multiple directories
#list down all the files from a parfticular directory
os.listdir("D:\\Users\\win10\\jupyter")
#os.getcwd()


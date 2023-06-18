# File1=open("testFile.txt",'w')
# #r-reading,w-writing,a-appending
# print(File1.name)
# print(File1.mode)
# File1.close()

# with open("testFile2.txt",'r') as File2:
#     file_stuff = File2.read()
#     print(file_stuff)
# print(File2.closed)
# print(file_stuff)

# with open("testFile2.txt",'r') as File2:
#     file_stuff = File2.readline()
#     print(file_stuff)
#     #file_stuff[0]: first line
#     #file_stuff[1]: second line

# with open("testFile2.txt",'r') as File2:
#     file_stuff = File2.readlines()
#     #file_stuff = File2.readlines(4)
#     #first 4 characters will be printed and then the new line.
#     print(file_stuff)   
#     #All the lines will be printed 

# #Writing a file

# with open("testFile2.txt",'w') as File3:
#     File3.write("This is line A\n")   

# Lines = ["This is LineA\n","This is lineB\n","This is lineC\n"] 
# with open("testFile2.txt",'w') as File3:  
#     for line in Lines:
#         File3.write(line) 

#To copy from one file to another
with open("testFile2.txt",'r') as readfile:
    with open("testFIle3.txt",'w') as writefile:
        for line in readfile:
            writefile.write(line)       
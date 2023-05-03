# path="my_first_file.txt"
# file1 = open(path,'r')
# print(file1.read())
# open=('my_first_file.txt',"r" )
# print(file1.readlines(),end= "---\n")

# try:
#     file1 = open('my_first_file.txt',"r")
#     print(file1.read())
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     # file1.write("Default creation was done in exception block")
#     file1.writelines(['first_line\n','second_line\n','third_line'])
    
    # print("I am location ", file1.tell())
    # print("I am resetting it at 0 " , file1.seek(0))
    # print("I am location after resetting ", file1.tell())
    # print("I am reading just after writing-->", file1.read())
    # file1.close()
    
    # program to read from one file and write to another file 
# output_file= open('my_first_file_output.txt','w+')
# for input_line in open('my_first_file.txt'):
#     output_file.write('HPCSA'+input_line)

# output_file.seek(0)    
# print(output_file.read())
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # To create empty file

# f=open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt","x")

# print("file created successfully")

# #To write data in file

# f=open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt","w")
# f.write("learn coding\n ankit | ankush")
# print("file wrote successfully")

# #To read data in file

# f=open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt","r")
# print(f.read(30))
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
#   #To copy data of one file to another file
# try:
#     with open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt") as file2:
#         with open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt","w") as file3:
#             for i in file2:
#                 file3.write(i)
                
# except:
#     print("file not avilable create first")
    
# else:
#     file2.close()
#     print("file closed")

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# #To delete a file  

# import os
# if os.path.exists ("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt") :
#     os.remove("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt")   
# else:
#     print("file not available")
# print("file deleted successfully")


# program to read from one file and write to the same file 

# input_file = open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt")
# temp_data = input_file.readlines()
# input_file.close()

# output_file= open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt",'w+')
# for input_line in temp_data:
#     output_file.write('HPCSA'+input_line)

# output_file.seek(0)    
# print(output_file.read())

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# program to write to start of each file 

# file1 = open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt",'r')

# temp= file1.readlines()
# print(temp)  
# for i in range(len(temp)):
#     temp[i] = 'hello ' + temp[i]
# print(temp)  

# file1.close()
# file1 = open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\A.txt",'w')
# file1.writelines(temp)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # program to read from one file and write to another file 

# output_file= open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt",'w+')
# for input_line in open("C:\\Users\\dhpcsa\\Desktop\\hpcsa_programs\\Python Class\B.txt"):
#     output_file.write('HPCSA'+input_line)

# output_file.seek(0)    
# print(output_file.read())

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
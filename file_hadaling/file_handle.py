# file = open("name.txt", "r")

# content = file.read()
# print(content)

# file.close()

# try:
#     line=input("Enter a line:- ")
#     # Write to file
#     with open("name.txt", "a") as file:
#         file.write(line)
    
#     # Read and display contents
#     with open("name.txt", "r") as file:
#         content = file.read()
#         print("File contents:", content)
# except IOError as e:
#     print(f"An error occurred: {e}")
    

#checking if file exit

import os

if os.path.exists("name.txt"):
    print("file exit")

else:
    print("file not exit")

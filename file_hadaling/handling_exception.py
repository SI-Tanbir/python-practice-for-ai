
# error what it meaing --- compile time error and runtime error

# compile time error --- syntax error

# runtime error --- logic error

''''



#exception  ---> runtime error

#index error

#key error

#type error value error , zero division error

'''


try:
    # with open("name.txt", "r") as file:
    #     print(file.read())

    x=asdf

except FileNotFoundError:
    print("file not found")

except ZeroDivisionError:
    print("zero division error")

#!how will you handle a errr that not defined

except Exception as e:
    print(f"some error occurred: {e}")

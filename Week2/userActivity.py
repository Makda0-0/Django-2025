try:
    with open("log.txt", "a") as file:
        file.write(" User logged in \n")
    with open("log.txt", "r") as file:
        content=file.read()
        print(content)   
except  FileNotFoundError:
    print("File not found")
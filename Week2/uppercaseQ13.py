def read_and_uppercase():
  
    try:
          with open("messages.txt", "w") as file:
           file.write("Hello World\n")
           file.write("Python is fun")
      
          with open("message.txt", "r") as file:
          
            content = file.read()
            
            
            uppercase_content = content.upper()
            
            
            print(uppercase_content)
            
    except FileNotFoundError:
        print("Error: message.txt file not found!")
        print("Please make sure the file exists in the current directory.")


read_and_uppercase()
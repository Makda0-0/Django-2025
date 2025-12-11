
user_input = input("Enter sales number: ")


try:
    sales_number = int(user_input)
    
    
    try:
      
        file = open("sales.txt", "a")
        
        file.write(str(sales_number) + "\n")
      
        file.close()
        print("Sales number saved successfully!")
        
    except FileNotFoundError:
        print("File not found - creating new file")
       
        file = open("sales.txt", "w")
        file.write(str(sales_number) + "\n")
        file.close()
        print("File created and sales number saved!")
        
except ValueError:
    print("Error: Please enter a valid number (digits only)")
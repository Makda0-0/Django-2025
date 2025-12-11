valid_sales = []  # List
total_sales = 0   

try:
    with open("sales.txt", "r") as file:
        content = file.read()
        print("File content read successfully")
    
    with open("sales.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove extra spaces/newlines
            print(f"Processing line: '{line}'")
            
            
            try:
                sales_number = int(line)
                valid_sales.append(sales_number)  # Add to list
                total_sales += sales_number       
                print(f"Added: {sales_number}")
            except ValueError:
                print(f"Skipped: '{line}' (not a valid number)")
    
    
    print("\n" + "="*40)
    print(f"Valid sales numbers: {valid_sales}")
    print(f"Total sales: {total_sales}")
    print(f"Number of valid entries: {len(valid_sales)}")
    
except FileNotFoundError:
    print("Error: sales.txt file not found!")
         
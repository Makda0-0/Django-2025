def sum_valid_numbers():
    total = 0
    line_count = 0
    
    try:

        
        with open("numbers.txt", "w") as file:
          file.write("10\n")
          file.write("20\n")
          file.write("30\n")
          file.write("abc\n")
          file.write("40\n")

          print("Created numbers.txt file")
        with open("numbers.txt", "r") as file:
            for line in file:
                line_count += 1
                line = line.strip()  # Remove extra spaces/newlines

                
                try:
                    # Try to convert line to integer
                    number = int(line)
                    total += number
                    print(f"Line {line_count}: '{line}' Added {number}")
                except ValueError:
                    # Skip invalid lines
                    print(f"Line {line_count}: '{line}'Skipped (not a number)")
                    
    except FileNotFoundError:
        print("Error: numbers.txt file not found!")
        return
    
    print(f"\nSum = {total}")


sum_valid_numbers()

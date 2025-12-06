
try:
    with open("config.txt", "r") as file:
        name = file.read().strip()
        if not name:
            name = "Guest"
except FileNotFoundError:
    with open("config.txt", "w") as file:
        file.write("Guest")
    name = "Guest"
except Exception as e:
    print(f"Error handling file: {e}")
    name = "Guest"

print(f"Welcome, {name}!")




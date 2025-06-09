# Open file and append to it.
file = open("equations.txt", "a")

# While loop to filter out any errors.
while True:
    try:
        value_1 = int(input("Type in your first value: "))
    except ValueError:
        print("You did not enter a valid number for the first value.")
        continue
    
    # Will determine what fucntion the user selected.
    calculation = input("Select whether you want to +, -, / or *: ")

    if calculation not in ["+", "-", "*", "/"]:
        print("You have not selected a valid calculation.")
        continue

    try:
        value_2 = int(input("Type in your second value: ")) 
    except ValueError:
        print("You did not enter a valid number for the second value.")
        continue 

    # if statement is used to perform the desired calculation
    if calculation == "+":
        total = value_1 + value_2

    elif calculation == "-":
        total = value_1 - value_2

    elif calculation == "*":
        total = value_1 * value_2

    elif calculation == "/":

        # State calculation error if 0 used.
        if value_2 == 0:
            total = "Error: Division by zero."
        else:
            total = value_1 / value_2

    # Print and write the result to the file
    print(total)

    # Each new answer will write on a new line.
    file.write(str(total) + "\n")

    # Exit the loop
    break

# Close the file
file.close()
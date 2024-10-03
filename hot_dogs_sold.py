# ##########################################################################

# # Program: Hot Dog Total Calculator
# # Author: Jayce Johnson
# # Date: October 1st, 2024
# # Description: Lets the user tally up hot dogs as they are sold, outputting
# #              a total number of each hot dog sold, as well as the
# #              percentage of each type of hot dog sold.

# ##########################################################################

# These are the total number of each type of hot dog sold. It's currently 0, but will increase
# as the input variable increases.
veggie_dogs_total = 0
traditional_dogs_total = 0
curry_dogs_total = 0

# Gives the user the option to hit "q" to exit our program, otherwise it will run indefinitely
exit_button = input("Welcome to hot dog counter. Press enter to start, or Q to quit.")
while exit_button != "q":

    # Prompts the user to input the amount of veggie dogs sold
    veggie_dogs_input = input("How many veggie dogs were sold? ")

    # Gives the user another option to exit using "q"
    while True:
        if veggie_dogs_input == "q":
            print("Shutting down...")
            exit()

        # Validation check to ensure the input is a positive, whole number.
        # Outputs an error message and tries for input again if not.
        elif not veggie_dogs_input.isnumeric():
            print("Error: Input must be a positive, whole number.\n")
            veggie_dogs_input = input("How many veggie dogs were sold? ")

        # Exits this nested loop when proper input is given
        else:
            break


    # Prompts the user to input the amount of traditional hot dogs sold  
    traditional_dogs_input = input("How many traditional dogs were sold? ")  

    # Gives the user another option to exit using "q"
    while True:
        if traditional_dogs_input == "q":
            print("Shutting down...")
            exit()

        # Validation check to ensure the input is a positive, whole number.
        # Outputs an error message and tries for input again if not.
        elif not traditional_dogs_input.isnumeric():
            print("Error: Input must be a positive, whole number.\n")
            traditional_dogs_input = input("How many traditional dogs were sold? ")

        # Exits this nested loop when proper input is given
        else:
            break

    # Prompts the user to input the amount of curry dogs sold
    curry_dogs_input = input("How many curry dogs were sold? ")

    # Gives the user another option to exit using "q"
    while True:
        if curry_dogs_input == "q":
            print("Shutting down...")
            exit()

        # Validation check to ensure the input is a positive, whole number.
        # Outputs an error message and tries for input again if not.
        elif not curry_dogs_input.isnumeric():
            print("Error: Input must be a positive, whole number.\n")
            curry_dogs_input = input("How many curry dogs were sold? ")

        # Exits this nested loop when proper input is given
        else:
            break

    # Adds our counter variables to the total variables we declared at the beginning of the program
    # This ensures our total does not get reset with each loop
    veggie_dogs_total += int(veggie_dogs_input)
    traditional_dogs_total += int(traditional_dogs_input)
    curry_dogs_total += int(curry_dogs_input)

    # Adds up the total number of all hot dogs sold
    hot_dogs_total = veggie_dogs_total + traditional_dogs_total + curry_dogs_total

    # Calculates percentage of veggie dogs sold
    veggie_dog_percentage = veggie_dogs_total / hot_dogs_total * 100

    # Calculates percentage of curry dogs sold
    curry_dog_percentage = curry_dogs_total / hot_dogs_total * 100

    # Calculates percentage of traditional dogs
    traditional_dog_percentage = traditional_dogs_total / hot_dogs_total * 100

    # Prints the total amount of each hot dog sold and percentage of each
    # Will loop indefinitely after this unless user inputs "q"
    # Formatting thanks to this stackoverflow thread on multi-line f strings
    # https://stackoverflow.com/questions/45965007/multiline-f-string-in-python

    print(f"""\

You have sold a total of: {veggie_dogs_total} veggie dogs ({round(veggie_dog_percentage)}%)
                          {traditional_dogs_total} traditional dogs ({round(traditional_dog_percentage)}%)
                          {curry_dogs_total} curry dogs ({round(curry_dog_percentage)}%)\n""")
          

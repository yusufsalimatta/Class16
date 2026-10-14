valid = False
while not valid: #Using nested while loop to validate user input
    try:
        n=int(input("Enter a number: "))
        #enter an even number
        while n%2!=0:

            print("Bye")
    except ValueError:
        print("Invalid")
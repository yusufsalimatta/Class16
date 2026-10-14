#using a try and except
try:
    number = int(input("Enter A Number: "))
    print("The Number Entered Is",  number )
#using value error
except ValueError as ex:
    print("Exception:", ex)
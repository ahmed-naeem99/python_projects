def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def decimal_to_hexa(decimal):
    return hex(decimal)[2:]

def hexa_to_decimal(hexa):
    return int(hexa, 16)

choice = input("Choose one of the following: \n1. decimal to binary \n2. binary to decimal \n3. decimal to octal \n4. octal to decimal \n5. decimal to hexa \n6. hexa to decimal \nEnter your choice: ")

if choice == "1":
    number = int(input("Enter the decimal number you want to convert: "))  # Convert input to int
    result = decimal_to_binary(number)
    print(f"The result is: {result}")
    
elif choice == "2":
    number = input("Enter the binary number you want to convert: ")
    result = binary_to_decimal(number)
    print(f"The result is: {result}")
    
elif choice == "3":
    number = int(input("Enter the decimal number you want to convert: "))  # Convert input to int
    result = decimal_to_octal(number)
    print(f"The result is: {result}")
    
elif choice == "4":
    number = input("Enter the octal number you want to convert: ")
    result = octal_to_decimal(number)
    print(f"The result is: {result}")
    
elif choice == "5":
    number = int(input("Enter the decimal number you want to convert: "))  # Convert input to int
    result = decimal_to_hexa(number)
    print(f"The result is: {result}")
    
elif choice == "6":
    number = input("Enter the hexadecimal number you want to convert: ")
    result = hexa_to_decimal(number)
    print(f"The result is: {result}")

else:
    print("Invalid Input! Try Again")

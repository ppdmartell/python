largest = -9999999
number = int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number > largest:
        largest = number
    number = int(input("Enter a number or type -1 to stop: "))

print("Largest number is", largest)

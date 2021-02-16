# Lab 3
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

#Task1
print("---TASK 1: Determine Fare---")
age = int(input("What is your age?: "))
studentQ = input("Are you a student (Y/N)?: ").strip().upper()
price1 = 1.50
price2 = 0.50
price3 = 1.00
if (age <= 12) and (studentQ == "Y" or studentQ == "N"):
  print(f"Fare Type 'CHILD' - {price2}")
elif (age > 12 and studentQ == "Y") and age < 65:
  print(f"Fare Type 'STUDENT' - {price3}")
elif (age >= 65) and (studentQ == "Y" or studentQ == "N"):
  print(f"Fare Type 'SENIOR' - {price2}")
else:
  print(f"Fare Type 'Adult' - ${price1}")

print()

#Task2
print("---Task 2: Print String Characters and Reverse---")
string = input("Input a string: ")
for x in range(0, len(string)):
  print(f"Str[{x}] = '{string[x]}'")
print(f"Reversed: '{string[::-1]}'")

print()

#Task3
print("---Task 3: The Maximum ----\nKeep entering positive numbers.\nTo quit, input enter a negative number.")
a = int(input("Enter a number: "))
x = 0
while a > 0:
    if a > x:
        x = a
    a = int(input("Enter a number: "))
print(f"The largest number is {x}")

print()

#Task4
print("---Task 4: String triangle ---")
triangle = input("Type in a string: ")
for x in range(1,len(triangle)+1):
  print(triangle[:x])
for x in range(len(triangle)-1,0,-1):
    print(triangle[:x])
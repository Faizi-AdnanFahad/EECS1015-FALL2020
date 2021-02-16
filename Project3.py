# Lab 2
# Author: Adnan Fahad Faizi
# Email: adnan500@my.yorku.ca
# Student ID: 217905928

#Task 1
print("----")
print("Task 1: Type in an exponential in the following form x^y, where x and y are single digits from 0-9")
exponent_input = (input("Type exponent here:").strip())
x = int(exponent_input[0])
y = int(exponent_input[2])
exponent_calculation = x**y
power = "^"
print(f"{str(exponent_input[0])}{power}{str(exponent_input[2])} is {str(exponent_calculation)}")
print()
print("----")
print()

#Task 2
print("Task 2: First half upper, second half lower")
long_sentence = input("Type a sentence: ").strip()
middle_character = long_sentence[len(long_sentence) // 2]
slicing_till_the_middle_character = len(long_sentence) // 2
print(f"The string is {len(long_sentence)} characters long. '{middle_character}' is the middle character'")
upper_sentence = long_sentence[0:slicing_till_the_middle_character].upper()
lower_sentence = long_sentence[slicing_till_the_middle_character:].lower()
print(f"Modified sentence: {upper_sentence} | {lower_sentence}.")
print()
print("----")
print()

#Task3
print("Task 3: Remove commas and periods.  Convert spaces to * and characters to lowercase.")
sentence3 = input("Type a sentence: ").strip()
newSentence = sentence3.replace(",", "")
update_sentence = newSentence.replace(" ", "*").lower()
print(f"Modified sentence: {update_sentence}")
print()
print("----")
print()

#Task4
print("Task 4: Substring highlight")
sentence4 = input("Type a sentence: ").strip()
sub_string = input("Type substring: ")
indexOfSubString1 = sentence4.index(sub_string)
LenOfSub = len(sub_string)
add = indexOfSubString1 + LenOfSub
print(f"{sentence4[0:indexOfSubString1]}*{sub_string.upper()}*{sentence4[add:]}")

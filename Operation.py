#Write a program to print the “CODINGAL” word in a reverse direction.

#input a word
text = (input("Enter a string: "))

#Reverse string
# using step value as -1 to itrerate in reverse
revText = text[::-1]
text = revText

print("Reverse of given string is: ")
print(text)

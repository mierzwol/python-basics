print("This is a line of text!")

print("This is first line of text!\nThis is second line!")

# \ Prints out the " that normally would indicate the end of string
print("This is some \" text")

phrase = "String in a variable"
print(phrase)

print("\n" + phrase + " and concatenated string")

print(phrase.capitalize())
print(phrase.upper())
x=phrase.upper()
print(phrase.isupper())
print(x)
print(x.isupper())

print(len(phrase))
print(phrase[2])
print(phrase.index("rig"))
print(phrase.index("i"))
print(phrase.replace("variable","variable_replaced"))
print(phrase.lower().upper())


import string
import keyword

input_string = input("Enter name: ")

if " " in input_string:
    print(False)
elif input_string[0].isdigit():
    print(False)
elif any(char in string.punctuation and char != "_" or char.isupper() for char in input_string):
    print(False)
elif input_string in keyword.kwlist:
    print(False)
elif input_string == "__":
    print(False)
elif input_string.startswith("__")and input_string.count("_")>2:
    print(False)
elif input_string.count("_")>1 and not input_string.startswith("__"):
    print(False)
else:
    print(True)

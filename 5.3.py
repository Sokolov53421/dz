import string



input_string = input("Enter Text: ")

clean_text=input_string.translate(str.maketrans('', '',string.punctuation)).split()
caps_text=[word.capitalize() for word in clean_text]

hashteg="#" + ''.join(caps_text)
hashteg= hashteg[:140]

print(hashteg)
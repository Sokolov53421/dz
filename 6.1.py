input_string = input("Enter a-c:")
start, end = input_string.split("-")

start_code = ord(start)
end_code = ord(end)

result = (''.join(chr(i) for i in range(start_code, end_code + 1)))
print(result)

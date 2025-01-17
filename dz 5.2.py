while True:
    num1 = float(input("first number"))
    num2 = float(input("second number"))
    action = input("please enter following characters '+,-,/,*")

    if action in "+":
        result = num1 + num2
    elif action in "-":
        result = num1 - num2
    elif action in "*":
        result = num1 * num2
    elif action == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error")
            result = None

    print(result)

    restart = input("To continue, type 'yes'.").lower()
    if restart != "yes" :
        break

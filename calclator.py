

def operations(num1, num2, operator):
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "//":
        return num1 // num2
    else:
        return num1 ** num2


def calculator():
    while True:
        num1 = input("input first number: ")
        if num1.lower() == "quit":
            print("calculator closed")
            break
        try: 

            num1 = float(num1)

            opt = input("input and operator: ")

            if opt.lower() == "sqrt":
                pass

            elif opt not in ["+", "-", "*", "/", "%", "//", "^"]:
                print("invalid operator. list of operator:\""+", "-", "*", "/", "%", "//", "^"\"")
                continue
            

            num2 = input("input second number: ")
            
            if num2.lower() == "quit":
                print("calculator closed")
                break

            num2 = float(num2)

            result = operations(num1, num2, opt)
            print(f"{num1} {opt} {num2} = {result}")

        except ValueError:
            print("not a number, input a valid number")
            continue

calculator()
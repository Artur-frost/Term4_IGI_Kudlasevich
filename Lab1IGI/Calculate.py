def function(number_1, number_2, op):
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)

        if op == "add":
            print(f"{number_1} + {number_2} = {number_1 + number_2}")
            return False
        elif op == "sub":
            print(f"{number_1} - {number_2} = {number_1 - number_2}")
            return False
        elif op == "mul":
            print(f"{number_1} * {number_2} = {number_1 * number_2}")
            return False
        elif op == "div":
            if number_2 == 0:
                print("Divide by zero")
                return True
            print(f"{number_1} / {number_2} = {number_1 / number_2}")
            return False
        else:
            print("Incorrect operation")
            return True
    except ValueError:
        return


first_number = input("Enter the first number \t")
second_number = input("Enter the second umber \t")
action = input("Enter an action \t")
print(function(first_number, second_number, action))

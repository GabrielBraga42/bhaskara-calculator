def input_abc():
    a = int(input("Input a integer for 'a': "))
    b = int(input("Input a integer for 'b': "))
    c = int(input("Input a integer for 'c': "))
    return (a, b, c)


def manual_check_y_n():
    goodInput = 0
    while goodInput == 0:
        test = (input("(Yes/No): "))
        if (test.upper()) == "YES" or (test.upper()) == "NO":
            goodInput = 1
    if (test.upper()) == "YES":
        return True
    elif (test.upper()) == "NO":
        return False


def abc_to_manual_check(a, b, c):
    formula = "(" + str(a) + "x)²"
    if b < 0:
        formula += str(b) + "x"
    else:
        formula += "+" + str(b) + "x"

    if c < 0:
        formula += str(c)
    else:
        formula += "+" + str(c)
    print()
    print("Is this correct?: " + str(formula) + " = 0")
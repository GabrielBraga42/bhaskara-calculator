def input_abc():
    aOK, bOK, cOK = False, False, False
    while not aOK:
        try:
            a = float(input("Input a valid number for 'a': "))
            aOK = True
        except:
            pass
    while not bOK:
        try:
            b = float(input("Input a valid number for 'b': "))
            bOK = True
        except:
            pass
    while not cOK:
        try:
            c = float(input("Input a valid number for 'c': "))
            cOK = True
        except:
            pass
    return a, b, c


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
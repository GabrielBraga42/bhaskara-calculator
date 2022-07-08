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
import functions as ft
print("Welcome to the bhaskara calculator!")
correct1 = False
while not correct1:
    correct2 = False
    while not correct2:
        a, b, c = ft.input_abc()
        ft.abc_to_manual_check(a, b, c)
        if ft.manual_check_y_n():
            correct2 = True
        else:
            correct2 = False
            print()
            print("Then, please re-input the values: ")
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print()
        print("Error! Delta cannot be a negative number. (Δ = " + str(delta) + ")")
        print("Do you wish to re-input the values?: ")
        if ft.manual_check_y_n():
            correct2 = False
            print()
            print("Then, please re-input the values: ")
        else:
            correct1 = True
            print()
            print("This program is not ready for this kind of math yet :)")
            print("Exiting.")
    else:
        correct1 = True
print()
print("With the following formula for bhaskara: ")
if b < 0:
    formula2 = ("X = " + "(" + str(b) + " ± √" + str(delta) + ") / " + "2")
else:
    formula2 = ("X = " + "(-" + str(b) + " ± √" + str(delta) + ") / " + "2")
if a < 0:
    formula2 += " * (" + str(a) + ")"
else:
    formula2 += " * " + str(a)
print(formula2)
print()
print("We get the possible solutions: ")
s1 = (b + (delta ** (1 / 2))) / (2 * a)
s2 = (b - (delta ** (1 / 2))) / (2 * a)
print("For + : " + str(s1))
print("For - : " + str(s2))
if s1 < s2:
    print(("S = {" + str(s1) + ", " + str(s2) + "}"))
else:
    print(("S = {" + str(s2) + ", " + str(s1) + "}"))
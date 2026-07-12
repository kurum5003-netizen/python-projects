def addition(z,x):
    return z+x
def subtraction(z,x):
    return z-x
def multiplication(z,x):
    return z*x
def division(z,x):
    return z/x

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

def calculate():
    accunlate=True
    num1=int(input("What's the first number?: "))

    while accunlate:
        for key in operations:
            print(key)
        operation_symbol=input("Pick a operation: ")
        num2=float(input("What's the second number?: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2}={answer}")
        chocie=input(f"Type 'y' to continue calculating with {answer }or type 'n' new calculating: ")

        if chocie=="y":
            num1=answer
        else:
            accunlate=False
            print("\n" * 20)
            calculate()
calculate()

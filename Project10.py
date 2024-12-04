def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

dictionary={"+":add,
            "-":sub,
            "*":multiply,
            "/":divide}

def calculator():
    should_continue=True
    number1 = float(input("Enter the first number:"))
    while should_continue:
        for symbol in dictionary:
            print(symbol)
        operation = input("Enter the operation:")
        number2 = float(input("Enter the second number:"))
        answer=dictionary[operation](number1,number2)
        print(answer)

        result=input(f"Type 'y' if you want to continue with {answer},type 'n' if you want to provide different value:")
        if result=="y":
            number1=answer
        else:
            should_continue=False
            print("\n"*20)
calculator()



def damateba(x, y):
    return x + y

def gamokleba(x, y):
    return x - y

def gamravleba(x, y):
    return x * y

def gayofa(x, y):
    if y == 0:
        return "0ze gayofa ar sheidzleba!"
    return x / y

def calculator():
    print("airchie operacia:")
    print("1. + damateba")
    print("2. - gamokleba")
    print("3. * gamravleba")
    print("4. / gayofa")

    choice = input("airchie (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {damateba(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {gamokleba(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {gamravleba(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {gayofa(num1, num2)}")
    else:
        print("error")


calculator()
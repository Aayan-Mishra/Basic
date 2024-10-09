a = input("What is your 'A' value?: ")
b = input("What is your 'B' value?: ")
sign = input("What operation?: ")

if sign == "times":
    result = int(a) * int(b)
    print(f"{a} times {b} equals {result}")
elif sign == "divide":
    try:
        result = int(a) / int(b)
        print(f"{a} divided by {b} equals {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
elif sign == 'add':
    result = int(a) + int(b)
    print(f"{a} plus {b} equals {result}")
elif sign == 'subtract':
    result = int(a) - int(b)
    print(f"{a} minus {b} equals {result}")
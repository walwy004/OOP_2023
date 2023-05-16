try:
    number = int(input("Number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except:
    print("Not a number")

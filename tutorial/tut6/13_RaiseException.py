def noReturn():
    print("Exception to be raised.")
    raise Exception("Raised Exception.")
    print("This line is never executed")
    return "Not returned!"


try:
    noReturn()
except:
    print("Exception was caught.")

print("Executed after the exception")

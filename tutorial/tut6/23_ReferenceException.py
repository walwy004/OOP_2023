try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("Exception:", e)
    print("Arguments:", e.args)
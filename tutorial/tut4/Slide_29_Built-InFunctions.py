obj = 0

if hasattr(obj, 'method_name') and \
    callable(obj.method_name):
    print("Method is available.")
    obj.method_name()
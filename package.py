num = 1

def increment(*arg):
    global num
    num += arg[0] if len(arg) > 0 else 1
def decorator(func):
    def wrapper():
        print("decorator active")
        return func().split()
    return wrapper
@decorator
def function():
    print("in function")
    return "hi here"
print(function())


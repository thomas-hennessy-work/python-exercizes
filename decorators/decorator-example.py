def upper_decorator(func):
    def function_wrapper(string_1):
        return string_1.upper()
    return function_wrapper

@upper_decorator
def hello(string_2):
    return string_2

print(hello("This is a test"))
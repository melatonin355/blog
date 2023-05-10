# Python Decorators


A Python decorator is a design pattern that allows you to modify or extend the behavior of a function or method without changing its code. Decorators are used as higher-order functions that take a function as input and return a new function that usually extends the input function's behavior. 

Here's a cheat sheet for decorators:

1. Basic syntax:
```python
@decorator
def function_to_decorate():
    # Function implementation
```

2. Defining a simple decorator:
```python
def my_decorator(func):
    def wrapper():
        print("Something happens before the function is called.")
        func()
        print("Something happens after the function is called.")
    return wrapper
```

3. Using the decorator:
```python
@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Output: "Something happens before the function is called." "Hello!" "Something happens after the function is called."
```

Now, let's dive into some different ways to use decorators:

1. Timing a function:
```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()  # Output: "slow_function took 2.0002 seconds to execute."
```

2. Logging function calls:
```python
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(3, 4)  # Output: "Calling function add with arguments: (3, 4) and keyword arguments: {}" "Function add returned: 7"
```

3. Restricting access to a function (e.g., authentication):
```python
def auth_decorator(allowed_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if allowed_role == "admin":
                return func(*args, **kwargs)
            else:
                print(f"Access denied for role: {allowed_role}")
        return wrapper
    return decorator

@admin_only = auth_decorator("admin")

@admin_only
def restricted_function():
    print("This function can only be accessed by admins.")

restricted_function()  # Output: "This function can only be accessed by admins."
```

These examples should give you a good understanding of Python decorators and how to use them in various situations. Decorators can be a powerful tool to help you write more modular and maintainable code.
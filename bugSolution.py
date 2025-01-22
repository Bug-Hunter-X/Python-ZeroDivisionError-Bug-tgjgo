def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or raise a more specific exception, or return a default value

result = function(10, 0) # Returns 0
result2 = function(10,2) # Returns 5.0
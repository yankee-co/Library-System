def factorial(x):
    """Calculates factorial"""
    if type(x) == int and x >= 0:
        result = 1
        for i in range(2, x+1):
            result *= i
        return result
    return 'Wrong data given to function'

def multiply(a, b):
    # Handle negative numbers
    if b == 0:
        return 0
    if b < 0:
        return -multiply(a, -b)
    result = 0
    for _ in range(b):
        result += a
    return result
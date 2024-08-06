def recrusive_power(n, m):
    if m == 0:
        return 1
    return n * recrusive_power(n, m - 1)


print(recrusive_power(2, 10))

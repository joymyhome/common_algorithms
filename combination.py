def comb(n, m):
    """
    calculate c(n, m)
    """
    res = 1
    for i in range(m):
        res *= n-i
        res /= i+1
    return res


def extraLongFactorials(n):
    return n * extraLongFactorials(n-1) if n > 2 else n*2

if __name__ == "__main__":
    print(extraLongFactorials(5))
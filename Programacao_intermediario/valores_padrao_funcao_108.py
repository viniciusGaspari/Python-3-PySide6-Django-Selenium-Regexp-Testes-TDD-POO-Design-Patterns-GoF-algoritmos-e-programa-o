def soma(x, y, z = None):
    if z is not None:
        print((x + y) ** z)
    else:
        print(x + y)

soma(5, 5)
def avg(*args):
    total = sum(args)
    return total / len(args)


print(avg(2, 5, 5))
def sum(*args):
    print(args)
    print(type(args))  # tuple

    sum = 0
    for i in args:
        sum += i
    return sum

result1 = sum(10,20)
result2 = sum(10,20,30)
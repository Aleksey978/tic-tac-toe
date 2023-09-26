def count(a=None):
    if a is None:
        a = [1, 2, 3]
        sting = "".join(a)
        print(sting)
    while True:
        yield a


count()
print("Изменено")
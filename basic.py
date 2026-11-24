def myFunction():
    yield 3
    yield 4
    yield 5

x = myFunction()

for _ in x:
    print(_)
# building a system that takes a set of temperature values as an array
# and then uses yield to return each reading individually 

temperatures = [36.2, 22.1, 232.0, 21.5, 0.1]

def giveReadings(x):
    for readings in x:
        print(readings)

def yields(y):
    for reading in y:
        yield reading

x = yields(temperatures)

giveReadings(x)
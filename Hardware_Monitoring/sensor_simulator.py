from numpy import random

class data_gen():

    def genTemp():
        temp_data = random.randint(150, size=(1000))
        return temp_data

    def genVolt():
        cpuvol_data = [random.uniform(0, 1) for n in range(1000)]
        return cpuvol_data

    def genFanSpd():
        fanspd_data = random.randint(800, size=(1000))
        return fanspd_data


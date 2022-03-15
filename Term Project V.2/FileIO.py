import numpy as np 

class Reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def readFromFile(self):
        weather_data = np.genfromtxt(self.file_name, delimiter = ',', dtype = float, skip_header = 1)
        return weather_data
        
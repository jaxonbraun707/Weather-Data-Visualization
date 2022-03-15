
class TemperatureData: 
    def __init__(self, data):
        self.data = data

    def getMinTemps(self):
        temps = self.data[:, 3].flatten()
        return temps

    def getMaxTemps(self):
        temps = self.data[:, 2].flatten()
        return temps

    def getSnowfalls(self):
        snowfalls = self.data[:, 4].flatten()
        return snowfalls



        


        
        




            


        
                





                

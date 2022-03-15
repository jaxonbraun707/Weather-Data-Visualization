from TemperatureData import * 
from Date import * 
import numpy as np


class WeatherAnalyzer:
    def __init__(self, data):
        self.data = data

    def getMinTemp(self):
        print(np.min(self.data.getMinTemps()))
        return

    def getMaxTemp(self):
        print(np.max(self.data.getMaxTemps()))
        return

    def getMinTempAnnually(self, dates):
        minTemps = np.array(self.data.getMinTemps())
        years = (dates.getYears())
        minTemps = np.array_split(minTemps, 30)
        minTempsAnnually = [[0 for x in range(2)]for y in range(30)]
        for i in range(30):
            minTemp = np.min(minTemps[i])
            minTempsAnnually[i][0] = years[i]
            minTempsAnnually[i][1] = minTemp
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in minTempsAnnually]))
        return minTempsAnnually
    
    def getMaxTempAnnually(self, dates):
        maxTemps = np.array(self.data.getMaxTemps())
        years = (dates.getYears())
        maxTemps = np.array_split(maxTemps, 30)
        maxTempsAnnually = [[0 for x in range(2)]for y in range(30)]
        for i in range(30):
            maxTemp = np.max(maxTemps[i])
            maxTempsAnnually[i][0] = years[i]
            maxTempsAnnually[i][1] = maxTemp
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in maxTempsAnnually]))
        return maxTempsAnnually

    def getAveSnowfallAnnually(self, dates):
        snowfalls = np.array(self.data.getSnowfalls())
        years = (dates.getYears())
        snowfalls = np.array_split(snowfalls, 30)
        AveSnowfallsAnnually = [[0 for x in range(2)]for y in range(30)]
        for i in range(30):
            snowfall = round(np.average(snowfalls[i]), 2)
            AveSnowfallsAnnually[i][0] = years[i]
            AveSnowfallsAnnually[i][1] = snowfall
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in AveSnowfallsAnnually]))
        return AveSnowfallsAnnually
    
    def getAveTempAnnually(self, dates):
        years = dates.getYears()
        minTemps = np.array(self.data.getMinTemps())
        maxTemps = np.array(self.data.getMaxTemps())
        aveTemps = []
        for i in range(359):
            Sum = minTemps[i] + maxTemps[i]
            ave = Sum / 2
            aveTemps.append(ave)
        AveTempsAnnually = [[0 for x in range(2)]for y in range(30)]
        aveTemps = np.array_split(aveTemps, 30)
        for i in range(30):
            aveTemp = round(np.average(aveTemps[i]), 2)
            AveTempsAnnually[i][0] = years[i]
            AveTempsAnnually[i][1] = aveTemp
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in AveTempsAnnually]))
        return AveTempsAnnually






        
        

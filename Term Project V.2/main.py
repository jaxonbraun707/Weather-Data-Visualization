import numpy as np  
import matplotlib.pyplot as pyplot

from FileIO import *
from Date import *
from Chart import *
from TemperatureData import *
from WeatherAnalyzer import *


def main():
    file_name = "CalgaryWeather.csv"
    reader = Reader(file_name)
    data = reader.readFromFile()
    dates = Date(data)
    chart = Chart()
    temperature_data = TemperatureData(data)
    weather_analyzer = WeatherAnalyzer(temperature_data)
    user_input = True

    while user_input:
        print("""
        1 - Get Minimum Temperature of 1990-2019
        2 - Get Maximum Temperature of 1990-2019
        3 - Get Minimum Temperature of 1990-2019 Annually
        4 - Get Maximum Temperature of 1990-2019 Annually
        5 - Get Average Snowfall of 1990-2019 Annually
        6 - Get Average Temperature of 1990-2019 Annually
        7 - LineChart Minimum Temperature of 1990-2019 Annually
        8 - LineChart Maximum Temperature of 1990-2019 Annually
        9 - BarChart Average Snowfall of 1990-2019 Annually
        10 - BarChart Average Temperature of 1990-2019 Annually
        11 - Exit
        """)
        user_input = input("Please enter the number of the data you want to view: ")
        if user_input == "1":
            print("\n Minimum Temperature Between 1990-2019:")
            weather_analyzer.getMinTemp()
        elif user_input == "2":
            print("\n Maximum Temperature Between 1990-2019:")
            weather_analyzer.getMaxTemp()
        elif user_input == "3":
            print("\n Minimum Temperature Between 1990-2019 Annually:")
            weather_analyzer.getMinTempAnnually(dates)
        elif user_input == "4":
            print("\n Maximum Temperature Between 1990-2019 Annually:")
            weather_analyzer.getMaxTempAnnually(dates)
        elif user_input == "5":
            print("\n Average Snowfall Between 1990-2019 Annually:")
            weather_analyzer.getAveSnowfallAnnually(dates)
        elif user_input == "6":
            print("\n Average Temperature Between 1990-2019 Annually:")
            weather_analyzer.getAveTempAnnually(dates)
        elif user_input == "7":
            print("\n LineChart Minimum Temperature Between 1990-2019 Annually: ")
            minTemps = []
            years = dates.getYears()
            minTempsAnnually = weather_analyzer.getMinTempAnnually(dates)
            for i in range(30):
                minTemps.append(minTempsAnnually[i][1])
            chart.drawLineChart(years, minTemps, "Minimum Temperature Between 1990-2019", "Year", "Temperature")
        elif user_input == "8":
            print("\n LineChart Maximum Temperature Between 1990-2019 Annually: ")
            maxTemps = []
            years = dates.getYears()
            maxTempsAnnually = weather_analyzer.getMaxTempAnnually(dates)
            for i in range(30):
                maxTemps.append(maxTempsAnnually[i][1])
            chart.drawLineChart(years, maxTemps, "Maximum Temperature Between 1990-2019", "Year", "Temperature")
        elif user_input == "9":
            print("\n LineChart Average Snowfall Between 1990-2019 Annually: ")
            aveSnowfalls = []
            years = dates.getYears()
            aveSnowfallsAnnually = weather_analyzer.getAveSnowfallAnnually(dates)
            for i in range(30):
                aveSnowfalls.append(aveSnowfallsAnnually[i][1])
            chart.drawBarChart(years, aveSnowfalls, "Average Snowfall Between 1990-2019", "Year", "Snowfall")
        elif user_input == "10":
            print("\n LineChart Average Temperature Between 1990-2019 Annually: ")
            aveTemps = []
            years = dates.getYears()
            aveTempsAnnually = weather_analyzer.getAveTempAnnually(dates)
            for i in range(30):
                aveTemps.append(aveTempsAnnually[i][1])
            chart.drawBarChart(years, aveTemps, "Average Temperature Between 1990-2019", "Year", "Temperature")
        elif user_input == "11":
            print("\n Bye!")
            user_input = None
        else:
            print("\n Invalid Input, Please Try Again")
    

if __name__ == "__main__":
    main()

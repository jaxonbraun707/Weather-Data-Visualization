class Date:  
    def __init__(self, data):
        self.data = data

    def getYears(self):
        years = self.data[:, 0].flatten()
        years_mod = list(set(years))
        years_mod1 = [int(i) for i in years_mod]
        return years_mod1

    def getMonths(self):
        months = self.data[:, 1].flatten()
        return months

import matplotlib.pyplot as pyplot 

class Chart():
    def drawLineChart(self, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.plot(x, y, marker = 'o')
        pyplot.show()
        return
    
    def drawBarChart(self, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.bar(x, y)
        pyplot.show()
        return

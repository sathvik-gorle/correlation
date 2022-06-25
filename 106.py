import csv
import plotly.express as px
import numpy as np

def getdatasource(data_path):
    Ice_cream_Sales=[]
    Cold_drink_sales=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Ice_cream_Sales.append(float(row['Temperature']))
            Cold_drink_sales.append(float(row['Ice-cream Sales']))
    return{'x':Ice_cream_Sales,'y':Cold_drink_sales}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('correlation is : ',correlation[0,1])

def setup():
    data_path='ice.csv'
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()

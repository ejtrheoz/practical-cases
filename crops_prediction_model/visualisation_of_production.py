import matplotlib
import seaborn
import pandas

matplotlib.rcParams['figure.figsize'] = [10, 7]

data = pandas.read_csv('crops_usa.csv')

production_2019 = data[data['Year'] == 2019]['Production']
states_2019 = data[data['Year'] == 2019]['State']


seaborn.barplot(x=production_2019, y=states_2019)

import matplotlib
import seaborn
import pandas

matplotlib.rcParams['figure.figsize'] = [15, 7] # указываем размер графика

data = pandas.read_csv('app_stats.csv')
conversions = data['payments'] / data['installs']

seaborn.barplot(x=data['week_number'], y=conversions)

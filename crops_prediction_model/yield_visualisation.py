
import pandas
import matplotlib
import seaborn


matplotlib.rcParams['figure.figsize'] = [15, 7]


data = pandas.read_csv('crops_usa.csv')

acres_usa = data.groupby('Year')['Acres'].sum()
production_usa = data.groupby('Year')['Production'].sum()

yield_usa = production_usa / acres_usa


years_unique = acres_usa.index.values


seaborn.barplot(x=years_unique, y=yield_usa)

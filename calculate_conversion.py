import pandas

data = pandas.read_csv('/datasets/app_stats.csv')

conversion = data['payments'] / data['installs']
print(conversion.tail(8) * 600)

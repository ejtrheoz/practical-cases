import pandas

pandas.set_option('display.float_format', lambda x: '%.2f' % x)

data = pandas.read_csv('crops_usa.csv')

acres_usa = data.groupby('Year')['Acres'].sum()
production_usa = data.groupby('Year')['Production'].sum()

yield_usa = production_usa / acres_usa

predict_acres = acres_usa * yield_usa.shift(1)
print(predict_acres)

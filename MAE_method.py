
import pandas

pandas.set_option('display.float_format', lambda x: '%.2f' % x)


data = pandas.read_csv('crops_usa.csv')

acres_usa = data.groupby('Year')['Acres'].sum()
production_usa = data.groupby('Year')['Production'].sum()

yield_usa = production_usa / acres_usa

predict_acres = acres_usa * yield_usa.shift(1)

error_acres = production_usa - predict_acres
error_acres = error_acres.dropna()

predict_yield = acres_usa.shift(1) * yield_usa

error_yield = production_usa - predict_yield
error_yield = error_yield.dropna()

error_abs_acres = abs(error_acres)

result_acres = error_abs_acres.sum() / error_abs_acres.count()
print(result_acres)

error_abs_yield = abs(error_yield)

result_yield = error_abs_yield.sum()/error_abs_yield.count()
print(result_yield)

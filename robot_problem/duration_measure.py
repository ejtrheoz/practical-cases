import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

duration_sum = data.groupby(['segment', 'interval'])['duration'].sum()    
duration_count = data.groupby(['segment', 'interval'])['duration'].count()

mean_duration = duration_sum / duration_count
print(mean_duration)

seaborn.heatmap(mean_duration.unstack('interval'), xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

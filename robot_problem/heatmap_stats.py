import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

# для каждой пары сегмент-интервал считаем сумму оценок
scores_sum = data.groupby(['segment', 'interval'])['score'].sum()    
# для каждой пары сегмент-интервал считаем количество записей
scores_count = data.groupby(['segment', 'interval'])['score'].count()

mean_scores = scores_sum / scores_count

# строим тепловую карту для средних значений
# столбец mean_scores получился вложенным из-за группировки по двум столбцам,
# поэтому его нужно «развернуть» методом unstack()
seaborn.heatmap(mean_scores.unstack('interval'),
                xticklabels=intervals,
                yticklabels=segments_new,
                annot=True,
                cmap='RdYlGn')

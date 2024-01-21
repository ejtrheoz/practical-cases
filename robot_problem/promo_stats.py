import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

# для каждой пары сегмент-интервал посчитайте сумму выданных промокодов
# так как в столбце promo есть только значения 1 и 0, сумма даст количество промокодов
promo_sum = data.groupby(['segment', 'interval'])['promo'].sum()
# для каждой пары сегмент-интервал найдите количество записей
promo_count = data.groupby(['segment', 'interval'])['promo'].count()

mean_promo = promo_sum / promo_count
print(mean_promo)

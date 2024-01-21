import pandas
import seaborn

data = pandas.read_csv('app_stats.csv')

campaign_weeks = [7, 9, 13, 15, 17, 19, 29, 31, 33, 45]

diff_installs = data['installs'].diff()
installs_from_ads = diff_installs[campaign_weeks]

diff_payments = data['payments'].diff()
payments_from_ads = diff_payments[campaign_weeks]

conversions_from_ads = payments_from_ads / installs_from_ads
ads_install_average_profit = conversions_from_ads * 600

seaborn.barplot(x=campaign_weeks, y=ads_install_average_profit)

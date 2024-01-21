import matplotlib.pyplot as plt
import pandas as pd
import seaborn

plt.rcParams['figure.figsize'] = (4, 8)

data = pd.read_csv('polomki.csv', index_col='Shop')
data['Week 14'] = data['Week 14']*100

seaborn.heatmap(data)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

seaborn_digimon = pd.read_csv('data/digimon/DigiDB_digimonlist.csv')
xticks = ['Lv50 SP', 'Lv50 Atk', 'Lv50 Def', 'Lv50 Int', 'Lv50 Spd']

sns.set_style('darkgrid')

plot = sns.boxplot(data=[seaborn_digimon[xtick] for xtick in xticks])
plot.set_xticklabels(xticks)

plt.show()

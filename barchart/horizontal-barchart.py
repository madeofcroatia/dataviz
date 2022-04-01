import matplotlib.pyplot as plt
import pandas as pd

digimon = pd.read_csv('data/digimon/DigiDB_digimonlist.csv')
digimon.head().plot.barh(x='Digimon', y=['Lv50 Atk', 'Lv50 Spd'], label=['Level 50 Attack', 'Level 50 Speed'])

plt.show()

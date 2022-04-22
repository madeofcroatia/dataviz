import plotnine as p9
import pandas as pd
import matplotlib.pyplot as plt

digimon = pd.read_csv('../data/digimon/DigiDB_digimonlist.csv')

print((p9.ggplot(data=digimon, mapping=p9.aes(x='Lv 50 HP', fill='count')) +
       p9.geom_histogram() + p9.scale_fill_gradient(low='magenta', high='red'))
)


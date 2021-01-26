import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


rt = [0.76, 0.81, 0.82, 0.88, 0.9, 0.94, 0.95, 0.97, 0.98, 0.98,
      0.99,1.02,1.03,1.04,1.05,1.05,1.08,1.12,1.12,1.27,1.38]
regioni = ['Campania', 'Veneto', 'LOMBARDIA', 'FVG', 'Trento', 'Lazio', 'Sardegna', 'E.R', 
           'Marche', 'Toscana', 'Liguria', 'Calabiria', 'Bolzano', 'Piemonte', 'Abruzzo', 'Umbria', 'Puglia', 
           'Basilicata', "Valle d'Aosta", 'Sicilia', 'Molise']

df = pd.DataFrame(data = rt, index = regioni, columns = ['RT'])
df = df.sort_values(by='RT', ascending=False)

 
# - CATEGORICAL PLOTS
fig = plt.figure(figsize=(12,6), dpi = 100)
g = sns.barplot(x='RT', y = df.index, data=df, palette = 'viridis')
g.set_xscale("log")
g.set_xlabel('Rt: Contagious Indices per Italian region, Protezione Civile 20 January 2021')
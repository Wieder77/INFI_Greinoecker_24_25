import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# Einlesen des Datensatzes
df1 = pd.read_excel('data/Zeitreihe-Winter-2024011810.xlsx')
# 1.2
base = ['Bezirk','Gemnr','Gemeinde']
years = df1.columns[3:].astype(str)
base.extend('x' + years)
df1.columns = base
# hole mir alle werte aus dem dokumt die größer als 0 sind
df1 = df1[df1.x2000 > 0]

# 1.3
print("1.3 :")
print(f"Describe Command:\n{df1.x2000.describe()}\n")

# 2.1
print("2.1 :")
naechtigungen = df1.values[0, 3:]
print(f"Nächtigungen Innsbruck: \n{naechtigungen}\n")

plt.title("Wintertourismus Nächtigungen Innsbruck")
plt.xlabel("Jahr")
plt.ylabel("Nächtigungen")
plt.plot(years, naechtigungen, "g.")
plt.show()

# 2.2
print("2.2 :")
df_il = df1[df1["Bezirk"] == "IL"]

naechtigungen = df_il.loc[:, df_il.columns[3:]].sum(axis=0).values
print(f"Nächtigungen Hall in Tirol: \n{naechtigungen}\n")

plt.title("Wintertourismus Nächtigungen Hall in Tirol")
plt.xlabel("Jahr")
plt.ylabel("Nächtigungen")
plt.plot(years, naechtigungen, "g.")
plt.show()

# 3.1
print("3.1:")
df1['min'] = df1.iloc[:, 3:].min(axis=1)
print(f"Minimalen Nächtigungen in den Städten: \n{df1['min']}\n")
df1['max'] = df1.iloc[:, 3:].max(axis=1)
print(f"Maximalen Nächtigungen in den Städten: \n{df1['max']}\n")
df1['mean'] = df1.iloc[:, 3:].mean(axis=1)
print(f"Durchschnitlliche Nächtigungen in den Städten: \n{df1['mean']}\n")
df1['range'] = df1['max'] - df1['min']
print(f"Spannweite Nächtigungen in den Städten: \n{df1['range']}\n")

# 3.2
print("3.2:")
naechtigungen_sum = df1.loc[:, df_il.columns[3:]].sum(axis=0)
print(f"Summe aller Nächtigungen Jährlich: \n{naechtigungen_sum}\n")
naechtigungen_total = naechtigungen_sum.values.sum(axis=0)
print(f"Summe aller Nächtigungen: \n{naechtigungen_total}\n")
naechtigungen_sum.plot(kind='bar', title="Jährliche Nächtigungen")
plt.xlabel("Jahre")
plt.ylabel("Nächtigungen")
plt.show()


# 4.1
print("4.1:")
df1['range_std'] = (df1['range'] / df1['max']) * 100
#a
df1.boxplot(column='range_std', by='Bezirk')
plt.show()
#b
pos = 0
labels = df1['Bezirk'].unique()
for b in labels:
    bez = df1[df1['Bezirk'] == b]
    plt.boxplot(bez['range_std'], positions=[pos])
    pos += 1
plt.xticks(range(len(labels)), labels)
plt.show()
#c
sns.boxplot(x=df1['Bezirk'], y=df1['range_std'], data=df1, palette="terrain")
plt.show()


# 4.2
print("4.2:")
naechtigungen = df1.loc[0, ("x" + years.values)].values
# Barplot erstellen

sns.barplot(x=years, y=naechtigungen, palette="terrain")
plt.xticks(rotation=70)
plt.title("Wintertourismus Nächtigungen Innsbruck")
plt.show()


# 5
print("5:")
df2 = pd.read_excel('data/bev_meld.xlsx')
base = ['Bezirk', 'Gemnr', 'Gemeinde']
gemeinde = df2.Gemeinde.values
years = df2.columns[3:].astype(str)
base.extend('x' + years)
df2.columns = base
both = pd.merge(df1, df2, how='inner', on='Gemnr')

# a
both['statartiesierter_vergleich'] = both['x2018_x'] / both['x2018_y']
print("5a:")
print(f"Verhältnis von Nächtigungen zur Einwohnerzahl für das Jahr 2018:\n{both['statartiesierter_vergleich']}\n")
# b
sns.barplot(x=both['Bezirk_x'], y=both['statartiesierter_vergleich'], palette="terrain")
plt.xticks(rotation=70)
plt.title("Statistischer Vergleich")
plt.show()
#c
both_high = both.sort_values(by='statartiesierter_vergleich', ascending=False).head(10)
both_low = both.sort_values(by='statartiesierter_vergleich', ascending=True).head(10)
print("5c:")
print(f"Top 10 Gemeinden mit dem höchsten Tourismus-Einwohner-Verhältnis: \n{both_high}\n")
print(f"Top 10 Gemeinden mit dem niedrigsten Tourismus-Einwohner-Verhältnis:\n{both_low}\n")
#d
gemeinden = both['Gemeinde_x'].values
verhaeltnis_hall = both[both['Gemeinde_x'].str.strip() == 'Hall in Tirol']['statartiesierter_vergleich']
print("5d:")
print(f"Tourismus-Einwohner-Verhältnis für Hall in Tirol:\n{verhaeltnis_hall.values}\n")
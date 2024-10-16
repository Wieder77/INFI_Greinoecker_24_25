import numpy as np
from matplotlib import pyplot as plt

#source: https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data
# date,cloud_cover,sunshine,global_radiation,max_temp,mean_temp,min_temp,precipitation,pressure,snow_depth
d = np.genfromtxt('data/london_weather.csv', delimiter=",", skip_header=1 )

dt = d[:,0] #Datum mit folgendem Aufbau: 19790103 (3.Jänner 1979)
# Aufteilen in Tag, Monat, Jahr
day = (dt % 100).astype('i')
month = (dt % 10000 / 100).astype('i')
year = (dt % 100000000 / 10000).astype('i')

# Check ob es funktioniert hat
print("Jahr:", np.unique(year, return_counts=True))
print("Monat", np.unique(month, return_counts=True))
print("Tag:", np.unique(day, return_counts=True))
print("Jahr MIN MAX" , np.min(year), np.max(year))

sun = d[:,2] # Sonnenstunden
print(sun)


# 1.1 Darstellung der Temperaturunterschiede
mean_temp = d[:,5]
temp1979 = mean_temp[year == 1979]
temp1989 = mean_temp[year == 1989]
temp1999 = mean_temp[year == 1999]
temp2000 = mean_temp[year == 2000]
plt.boxplot([temp1979, temp1989, temp1999, temp2000])
plt.title("Durchschnittliche Temperatur ueber 4 unterschiedliche Jahre:")
plt.ylabel("Temperatur °C")
plt.xlabel("Jahr")
plt.xticks([1, 2, 3, 4], ["1979", "1989", "1999", "2000"])
plt.grid(axis='y')
plt.show()
"""
    Man merkt das die TAge in 1979 kälter waren als wie die in den Jahren drauf. Unteranderem lässt sich erkennen, dass
    der Mittelwert der Jahre im gleichen Bereich liegt.
"""
# 1.2 Zeitlicher Verlauf
days2000 = month[year == 2000]
print(days2000)
plt.title("Zeitlicher Verlauf der Temperatur 2000:")
plt.xlabel("Tage")
plt.ylabel("Temperatur °C")
plt.plot(temp2000, "r-")
plt.show()
"""
    Man sieht in dieser Darstellung schön die einzelnen Jahreszeiten, da es im Winter z.B. viel kälter wie im Sommer.
    Außerdem erkennt man Extreme Tage an denen es entweder sehr heiß oder sehr kalt war, da diese stark rausstechen.
    Durch die Monate Jänner und Dezember welche von einander in der Darstellung am weitesten etfernt sieht das Liniendiagramm,
        wie eine Kurve aus.
"""

# 1.3 Herausfinden von Wetterextremen
temp2000_extrem_low = temp2000[temp2000 < np.quantile(temp2000, 0.25)]
temp2000_extrem_high = temp2000[temp2000 > np.quantile(temp2000, 0.75)]
temp1979_extrem_low = temp1979[temp1979 < np.quantile(temp1979, 0.25)]
temp1979_extrem_high = temp1979[temp1979 > np.quantile(temp1979, 0.75)]

plt.boxplot([temp2000_extrem_low, temp1979_extrem_low, temp2000_extrem_high, temp1979_extrem_high])
plt.title("Die kältesten sowie heißesten Tage vom Jahr 2000 und 1979:")
plt.ylabel("Temperatur °C")
plt.xlabel("Jahr")
plt.xticks([1, 2, 3, 4], ["2000 kältesten", "1979 kältesten", "2000 heißesten", "1979 heißesten"])
plt.grid(axis='y')
plt.show()
"""
    Man kann erkennen das die kältesten Tage in 1979 kälter waren, wie die kältesten Tage in 2020.
    Ausserdem kann man leicht sehen das es durchschnittlich heisser Tage in 2020 gibt als 1979. 
    Unteranderem passiert es öffter das es extreme Aussnahmen gibt Hitze und Kälte technisch in 2020.
    Das Klima ist also in 2020 eher wärmer wie in 1979 es kann aber extreme Ausschläge geben in Richtung Kälte und
    Hitze.
"""
#1.4 Mittelwert der einzlnen Jahre
for jahr in range(2010, 2020 + 1):
    temp = mean_temp[year == jahr]
    print(temp)
    temp_avg = np.average(temp)
    plt.bar(str(jahr),temp_avg, color='blue')
plt.title("Mittelwerte der letzten 10 Jahre:")
plt.ylabel("Temperatur °C")
plt.xlabel("Jahr")
plt.show()
"""
 Der Mittelwert in hat sich in den letzen 10 jahren nicht stark verändert er ist immer bei um die 12 Grad.
"""

#1.5 eigenes Diagramm und daten
max_temp = d[:, 4]
plt.hist(max_temp, bins=40, color='blue')
plt.title("Verteilung der maximalen Temperaturen")
plt.xlabel("Temperatur °C")
plt.ylabel("Anzahl der Tage")
plt.grid(axis='y')
plt.show()
"""
Man kann erkennen, dass die meisten Tage um die 12 grad heiß waren und nur wenige bis fast keine über die 30 Grad rüber gingen.
"""
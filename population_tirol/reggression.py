import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def show_population(df,years):
    population_avg = []
    for i in years.array:
        population_avg.append(sum(df['x' + i].values))
    print("Aufgabe 2.1: ")
    print(f"Summe der Einwohner in Tirol über die Jahre verteilt:\n{population_avg}\n")
    plt.xlabel('Jahre')
    plt.ylabel('Bevölkerung')
    plt.title('Bevölkerungsentwicklung')
    plt.plot(years.array, population_avg)
    plt.show()

def predict_population(sum_population):
    df_reg = pd.DataFrame({"years": np.arange(1992, 2021), "sum_population": sum_population})
    model = sm.OLS.from_formula('sum_population ~ years', data=df_reg).fit()
    df_pred = pd.DataFrame({"years": np.arange(1992, 2040)})
    predictions = model.predict(df_pred)
    print("Aufgabe 2.2: ")
    print(f"Prognose der Bevölkerungsentwicklung in Tirol:\n{predictions}\n")
    plt.plot(df_reg.years.values, df_reg.sum_population)
    plt.plot(df_pred.years.values, predictions)
    plt.xlabel('Jahre')
    plt.ylabel('Bevölkerung')
    plt.title('Bevölkerungsprognose')
    plt.xlim([1980, 2040])
    plt.show()


def predict_gemeinde(gmeinde_population):
    df_reg = pd.DataFrame({"years": np.arange(1992, 2021), "sum_population": gmeinde_population})
    model = sm.OLS.from_formula('sum_population ~ years', data=df_reg).fit()
    df_pred = pd.DataFrame({"years": np.arange(1992, 2040)})
    predictions = model.predict(df_pred)
    print("Aufgabe 3: ")
    print(f"Bevölkerungsentwicklung in Hall in Tirol:\n{df_reg.sum_population}\n")
    print(f"Prognose der Bevölkerungsentwicklung in Hall in Tirol:\n{predictions}\n")
    plt.plot(df_reg.years.values, df_reg.sum_population)
    plt.plot(df_pred.years.values, predictions)
    plt.xlabel('Jahre')
    plt.ylabel('Bevölkerung Hall in Tirol')
    plt.title('Bevölkerungsprognose Hall in Tirol')
    plt.xlim([1980, 2040])
    plt.show()

def comperaison_population(population_il, population_re):
    df_reg_il = pd.DataFrame({"years": np.arange(1992, 2021), "sum_population": population_il})
    df_reg_re = pd.DataFrame({"years": np.arange(1992, 2021), "sum_population": population_re})

    model_il = sm.OLS.from_formula('sum_population ~ years', data=df_reg_il).fit()
    model_re = sm.OLS.from_formula('sum_population ~ years', data=df_reg_re).fit()

    df_pred = pd.DataFrame({"years": np.arange(1992, 2040)})
    predictions_il = model_il.predict(df_pred)
    predictions_re = model_re.predict(df_pred)
    print("Aufgabe 4: ")
    print(f"Bevölkerungsentwicklung in IL:\n{df_reg_il.sum_population}\n")
    print(f"Prognose der Bevölkerungsentwicklung in IL:\n{predictions_il}\n")
    print(f"Bevölkerungsentwicklung in RE:\n{df_reg_re.sum_population}\n")
    print(f"Prognose der Bevölkerungsentwicklung in RE:\n{predictions_re}\n")
    plt.plot(df_reg_il.years.values, df_reg_il.sum_population, label="IL (tatsächliche Werte)", marker='o')
    plt.plot(df_reg_re.years.values, df_reg_re.sum_population, label="RE (tatsächliche Werte)", marker='o')
    plt.plot(df_pred.years.values, predictions_il, label="IL (Prognose)", linestyle="--")
    plt.plot(df_pred.years.values, predictions_re, label="RE (Prognose)", linestyle="--")
    plt.xlabel('Jahre')
    plt.ylabel('Bevölkerung')
    plt.title('Bevölkerungsvergleich IL und RE')
    plt.legend()
    plt.xlim([1980, 2040])
    plt.show()


def main():
    # 2. Erste Auswertung
    # Einlesen des Datensatzes
    df = pd.read_excel('data/bev_meld.xlsx')
    base = ['Bezirk', 'Gemnr', 'Gemeinde']
    years = df.columns[3:].astype(str)
    base.extend('x' + years)
    df.columns = base
    # Aufgabe 2.1
    show_population(df, years)
    sum_population = []
    for i in years.array:
        sum_population.append(sum(df['x' + i].values))
    # Aufgabe 2.2
    predict_population(sum_population)
    population_gemeinde =[]
    for i in years.array:
        population_gemeinde.append(sum(df.loc[df['Gemeinde'] == 'Hall in Tirol']['x' + i].values))
    # Aufgabe 3
    predict_gemeinde(population_gemeinde)
    # Aufgabe 4
    population_il = []
    for i in years.array:
        population_il.append(sum(df.loc[df['Bezirk'] == 'IL']['x' + i].values))
    population_re = []
    for i in years.array:
        population_re.append(sum(df.loc[df['Bezirk'] == 'RE']['x' + i].values))
    comperaison_population(population_il, population_re)

if __name__ == "__main__":
    main()
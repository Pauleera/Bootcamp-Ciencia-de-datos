import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('petroleum_argentina_500.csv')

print("***** ESPECIES ******")
print(df.head(5))

print(df.info())
print(df.describe())

df['date'] = pd.to_datetime(df['date'])
print("Hola")
print(df.info())

pozo_vaca_muerta = df[df['field'] == 'Vaca Muerta'].sort_values("field")
pozo_loma_campana = df[df['field'] == 'Loma Campana'].sort_values("field")
pozo_cerro_dragon = df[df['field'] == 'Cerro Dragón'].sort_values("field")
pozo_el_trapial = df[df['field'] == 'El Trapial'].sort_values("field")


# Histograma + KDE
plt.figure(figsize=(8, 5))
sns.histplot(df['oil_bbl'], kde=True, color='green')
plt.title('Distribución de Producción de Petróleo (oil_bbl)')
plt.show()
#plt.savefig('fig/histograma_oil.png')
plt.close()


freq = df['field'].value_counts()
print(freq)
df['alta_agua'] = np.where(df["water_cut_pct"] >= 40, True, False)

tabla_contingencia = pd.crosstab(df['field'], df['alta_agua'])

print(tabla_contingencia)


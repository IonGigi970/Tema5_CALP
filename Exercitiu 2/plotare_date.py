import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# print(df.to_string())

x_val = df.head(6)
y_val = df[['Durata','Puls']].tail(5)
y_val_ox = df['Durata'].tail(5)
y_val_oy = df['Puls'].tail(5)


print(x_val)
print(y_val)

plt.figure(1)
plt.plot(df)
plt.title('Toate valorile din CSV')
plt.legend(df.columns)

plt.figure(2)
plt.plot(x_val['Durata'],  'v--g', label='Durata')
plt.plot(x_val['Puls'],    '^:y',  label='Puls')
plt.plot(x_val['MaxPuls'], '<-r',  label='MaxPuls')
plt.plot(x_val['Calorii'], '>-.k', label='Calorii')
plt.title('Primele 6 valori pentru toate coloanele')
plt.xlabel('Inregistrare')
plt.ylabel('Valoare')
plt.legend(x_val.columns)

plt.figure(3)
plt.plot(y_val_ox,y_val_oy,'x:b')
plt.title('Durata vs Puls')
plt.xlabel('Durata [s]')
plt.ylabel('Puls [bpm]')

plt.show()


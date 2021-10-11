# Ksyta Mateusz

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Zadanie 3

# Deklaracja funkcji
def function(x):
    return x ** 2 + 5


# Deklaracja argumentów
x1 = np.linspace(-1, 1)
x2 = np.linspace(-6, 6)
x3 = np.linspace(0, 5)

# Wyrysowanie pierwszego wykresu przy użyciu funkcji
plt.plot(x1, function(x1), label="Line 1")
plt.legend()
plt.title('First plot')
plt.ylabel('Y label')
plt.xlabel('X label')
plt.show()

# Wyrysowanie drugiego wykresu przy użyciu funkcji
plt.plot(x2, function(x2), label="Line 2")
plt.legend()
plt.title('Second plot')
plt.ylabel('Y label')
plt.xlabel('X label')
plt.show()

# Wyrysowanie trzeciego wykresu przy użyciu funkcji
plt.plot(x3, function(x3), label="Line 3")
plt.legend()
plt.title('Third plot')
plt.ylabel('Y label')
plt.xlabel('X label')
plt.show()

# Zadanie 4

# Definiowanie Dataframe

df = pd.DataFrame({'name': ['Mateusz', 'Mateusz', 'Kuba', 'Kasia',
                   'Łucja'], 'surname': ['Ksyta', 'Nowak', 'Ksyta', 'Kowalczyk', 'Kruk'], 'age': [14, 15, 16, 17, 18],
                   'sex': ['M', 'M', 'M', 'F', 'F']})

# Wyświetlanie informacji
df.info()

# Opis danych
print(df.describe())

# Trzy pierwsze rekordy
print(df.head(3))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

archivo_excel = './Macro/PIB/PIB-MES.xlsx'  # Reemplaza 'ruta/al/archivo.xlsx' con la ubicación de tu archivo Excel
data = pd.read_excel(archivo_excel, engine='openpyxl')

anio = ["2021",2022]
# Asumamos que tu archivo Excel tiene columnas llamadas 'Año', 'Mes' y 'PIB'
fecha = data['Fecha']
pib = data['PIB']

# Crear una paleta de colores suficientemente grande para tus datos
n_colores = len(set(fecha))
print(n_colores)
colores = plt.cm.rainbow(np.linspace(0, 1, n_colores))

plt.figure(figsize=(10, 8))  # Establecer el tamaño de la figura

for fecha, valor, color in zip(fecha, pib, colores):
    rangos = f'{fecha}'
    print(valor)
    plt.plot(rangos, valor, marker='o', linestyle='-', color=color, alpha=0.5)

plt.xlabel('Fecha')
plt.ylabel('PIB')
plt.title('PIB por Año y Mes')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor legibilidad
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()



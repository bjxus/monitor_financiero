import pandas as pd
import matplotlib.pyplot as plt


# Leer los tres archivos de Excel, asumiendo que se llaman 'hoja1.xlsx', 'hoja2.xlsx' y 'hoja3.xlsx'

archivo1 = './Macro/inflacion.xlsx'
archivo2 = "./Macro/desempleo.xlsx"

# Leer los datos de cierre (Close) de las tres hojas

df1 = pd.read_excel(archivo1)
df2 = pd.read_excel(archivo2)
print(df1.head())



# Crear una figura para el gráfico


valores = df1[["Año","Inflacion"]]
valores2 = df2[["Año","Desempleo"]]

print(valores)
print(valores2)

anioInflacion = df1[["Año"]]
anioDesempleo = df2[["Año"]]

Inflacion = df1[["Inflacion"]]
Desempleo = df2[["Desempleo"]]

# Graficar los datos de cierre de la primera hoja

# PIB_MENSUAL = valores1.plot(x="Mes" , y="PIB")
PORCENTAJE_INFLACION = plt.plot(anioInflacion,Inflacion, label=" % Inflación",color="red", marker='o', linestyle='-')

PORCENTAJE_DESEMPLEO = plt.plot(anioDesempleo,Desempleo, label=" % Desempleo",color="orange", marker='o', linestyle='-')

# Personalizar el gráfico
plt.xlabel('Año')
plt.ylabel('Porcentaje')
plt.title('Indices de inflación y desempleo')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()






plt.show()



# Graficar los datos de cierre de la segunda hoja

 # Agregar leyendas para distinguir las hojas

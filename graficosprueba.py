import pandas as pd
import matplotlib.pyplot as plt


# Leer los tres archivos de Excel, asumiendo que se llaman 'hoja1.xlsx', 'hoja2.xlsx' y 'hoja3.xlsx'

archivo1 = './Macro/PIB/PIB-ANIO.xlsx'
archivo2 = './Macro/Deuda.xlsx'

# Leer los datos de cierre (Close) de las tres hojas

df1 = pd.read_excel(archivo1)
df2 = pd.read_excel(archivo2)
print(df1.head())



# Crear una figura para el gráfico


valores = df1[["Fecha","PIB"]]
valores1 = df2[["Año","Deuda"]]


print(valores)
print(valores1)

anio = df1[["Fecha"]]
PIB = df1[["PIB"]]

anioDeuda = df2[["Año"]]
deuda = df2[["Deuda"]]

# Graficar los datos de cierre de la primera hoja


PIB_ANUAL = plt.plot(anio,PIB, label="PIB ANUAL",color="green", marker='o', linestyle='-') 

# PIB_MENSUAL = valores1.plot(x="Mes" , y="PIB")
PIB_MENSUAL = plt.plot(anioDeuda,deuda, label="Deuda",color="red", marker='o', linestyle='-')


# Personalizar el gráfico
plt.xlabel('Año')
plt.ylabel('PIB en millones de pesos')
plt.title('Indices de PIB y deuda')
plt.legend()


plt.show()



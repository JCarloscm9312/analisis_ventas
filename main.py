import pandas as pd

# Carga de los datos
datos = pd.read_csv("ventas.csv", sep = ";", encoding="latin-1")
# Eliminar valores nulos y convertir la columna cantidad en valores enteros
datos.dropna(inplace=True)
# Filtrar solo productos

# Realizar grafico de linea que nos muestre las ventas por año de los productos

print(datos.head())

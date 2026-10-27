import pandas as pd
df=pd.read_excel("ventas.xlsx",sheet_name="Hoja1")
print(df.head())
print("Dimensiones: ", df.shape)
print(df.info())
print(df.describe())

print(" === resumen general de datos === ")
print("el total de registro en excel es de:", len(df))
print("el total de los precios unitarios es de: ", df["Precio unitario"].sum())
print("el precio unitario mas caro es: ", df["Precio unitario"].max())
print("el precio unitario mas barato es: ", df["Precio unitario"].min())
print("el promedio de los precios unitarios es: ", df["Precio unitario"].mean())
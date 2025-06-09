import pandas as pd
datos = pd.read_csv('ATP_DATA.csv', encoding='latin1')
print(datos.head())
print(datos.iloc[0:200])
print(datos.iloc[[0,3,6,24],])
print(datos.iloc[[0,3,6,24],[0,4,3]])
print(datos.iloc[:,[0,4,3]])


import pandas as pd
import numpy as np
datos = pd.read_csv('ATP_DATA.csv', encoding='latin1')
print(datos.head())
print(datos.info())
nuevo=pd.DataFrame(datos)
print(nuevo)

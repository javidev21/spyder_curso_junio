#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 13:37:12 2025

@author: javier
"""

import pandas as pd
import numpy as np
datos={'Nombre':['Leonardo','Darik','Alex','Alex'], 'Calificaciones':[
    '60','70','70', '80'], 'Deportes':['Natación','Basquet', 'Fútbol', 'Fútbol'],
    'Materias':['Química','Matemática', 'Historia', 'vida']
       }
df= pd.DataFrame(datos)
print(df)
print('\n'*4)
print(df)
print('\n')

datos2={'Nombre':['Darik','Alex','Alex', 'N/A', 'Alex','Alex'], 
        'Calificaciones':['60','70','100', np.nan, '200', '300'], 
        'Deportes':['Natación','N/A', 'Fútbol', 'Fútbol','Fútbol', 'Fútbol'],
        'Materias':['Química','Matemática', 'N/A', 'vida','N/A', 'vida']}
df2= pd.DataFrame(datos2)
print(df2)
print('\n'*4)
print(df2.info())
print('\n'*4)
print(df2.describe())
print('\n'*4)
nuevo = pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan,"0")

nuevo['Calificaciones']= nuevo.Calificaciones.astype(int)
print(nuevo.describe())
print('\n'*4)
print(nuevo.info())
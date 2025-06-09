#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 20:04:40 2025

@author: javier
"""
import pandas as pd
datos= pd.read_csv('ATP_DATA.csv', encoding='latin1')
print(datos.head())
datos.set_index('Location', inplace=True)
print(datos.loc[datos['Court'] =='Outdoor',['Surface']])
print(datos.loc[datos['Court'] =='Outdoor',['Surface','Winner']])
print(datos.loc[datos['Series'].str.endswith('Slam')&(datos['Surface']=="Clay")& (datos['Winner']=="Federer R.")&(datos['Round']=="The Final")])
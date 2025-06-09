#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 20:26:38 2025

@author: javier
"""
import pandas as pd
datos= pd.read_csv('ATP_DATA.csv', encoding='latin1')
df= pd.DataFrame(datos)
df.to_csv('exported_data.csv', index=False, encoding='utf-8')
datos.set_index('Location', inplace=True)
df= datos.loc['Barcelona']
df.to_csv('exported_barcelona.csv', index=False, encoding='utf-8')

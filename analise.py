# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient()
db = client.wdi_indicators
indicators = db.indicators

gdp_paises = indicators.find(
	{"indicator_code" : "NY.GDP.MKTP.KD.ZG", 
		"country_code" : {
		"$in" : ["CAN", "FRA", "GBR", "ITA", "JPN", "USA", "BRA", "IND", "CHN", "ZAF"]
		}
	}
)

gdp_paises_series = {}

gdp_paises_series["CAN"] = []
gdp_paises_series["FRA"] = []
gdp_paises_series["GBR"] = []
gdp_paises_series["ITA"] = []
gdp_paises_series["JPN"] = []
gdp_paises_series["USA"] = []
gdp_paises_series["BRA"] = []
gdp_paises_series["IND"] = []
gdp_paises_series["CHN"] = []
gdp_paises_series["ZAF"] = []


for pais in gdp_paises:
    for ano in pais["indicator_values"]:
        if (ano != ""):
            gdp_paises_series[pais["country_code"]].append(ano)
    print(pais["country_code"])
    print(len(gdp_paises_series[pais["country_code"]]))
    
df_gdp = pd.DataFrame({ "Canadá" : np.array(gdp_paises_series["CAN"], dtype='float32'), 
                       "França" : np.array(gdp_paises_series["FRA"], dtype='float32'),
                       "GBR" : np.array(gdp_paises_series["GBR"], dtype='float32'),
                       "Itália" : np.array(gdp_paises_series["ITA"], dtype='float32'),
                       "Japão" : np.array(gdp_paises_series["JPN"], dtype='float32'),
                       "EUA" : np.array(gdp_paises_series["USA"], dtype='float32'),
                       "Brasil" : np.array(gdp_paises_series["BRA"], dtype='float32'),
                       "Índia" : np.array(gdp_paises_series["IND"], dtype='float32'),
                       "China" : np.array(gdp_paises_series["CHN"], dtype='float32'),
                       "África do Sul" : np.array(gdp_paises_series["ZAF"], dtype='float32'),
                       })

print(df_gdp.describe())
corr = df_gdp.corr()
fig, ax = plt.subplots(figsize=(9, 9))
ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns);
plt.yticks(range(len(corr.columns)), corr.columns);

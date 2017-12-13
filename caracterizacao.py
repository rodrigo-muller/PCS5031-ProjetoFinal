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
		"$in" : ["CAN", "FRA", "GBR", "DEU", "ITA", "JPN", "USA", "BRA", "RUS", "IND", "CHN", "ZAF"]
		}
	}
)
data_co2_emission = indicators.find({"indicator_code" : "EN.ATM.CO2E.PC", "country_info" : {"$exists" : "true", "$ne" : None }, "country_info.currency_unit" : {"$ne" : ""}})

data_gdp = indicators.find({"indicator_code" : "NY.GDP.MKTP.KD.ZG", "country_info" : {"$exists" : "true", "$ne" : None }, "country_info.currency_unit" : {"$ne" : ""}})

co2_emission_series = []
gdp_series = []

for pais in data_co2_emission:
    for ano in pais["indicator_values"]:
        if (ano != ""):
            co2_emission_series.append(ano)

for pais in data_gdp:
    for ano in pais["indicator_values"]:
        if (ano != ""):
            gdp_series.append(ano)
    
df_co2 = pd.DataFrame({ 'Emissão de CO2 (tonelada métrica per capita)' : np.array(co2_emission_series, dtype='float32')})

df_gdp = pd.DataFrame({ 'Crescimento anual do Produto Interno Bruto (%)' : np.array(gdp_series, dtype='float32')})

#df_co2_emission = pd.DataFrame(list(data_co2_emission["indicator_values"]))

#print(list(df_co2_emission.values))

#df = pd.DataFrame(list(gdp_paises))
print(df_co2.describe())
print(df_gdp.describe())

plt.figure(); df_co2.boxplot(return_type='axes'); plt.legend(loc='best')
plt.figure(); df_gdp.boxplot(return_type='axes'); plt.legend(loc='best')



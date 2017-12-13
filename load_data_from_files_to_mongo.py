# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

import csv

from indicator import Indicator

from pymongo import MongoClient

directory = '/Users/romul/Google Drive/Estudo/Mestrado/disciplinas/PCS5031/projeto/PCS5031-ProjetoFinal/data/'
countries_file = 'WDICountry.csv'
countries_series_file = 'WDICountry-Series.csv'
data_file = 'WDIData.csv'
foot_note_file = 'WDIFootNote.csv'
series_file = 'WDISeries.csv'
series_time_file = 'WDISeries-Time.csv'

client = MongoClient()
db = client.wdi_indicators
indicators = db.indicators

indicators_array = []
#Open the data file and insert data from others files in each row
with open(directory + data_file, encoding='utf8') as csv_data_file:
    data_reader = csv.reader(csv_data_file, delimiter=',')
    row_count = 1
    #Read the main file -- with data values
    for data_row in data_reader:
        if row_count > 1:
            indicator = Indicator()
            indicator.insert_indicator_values(data_row)
            indicators_array.append(indicator)
        row_count = row_count + 1

country_information_map = {}
#Read the file with information about the country and insert the data to indicator instance
with open(directory + countries_file, encoding='utf8') as csv_countries_file:
    countries_reader = csv.reader(csv_countries_file, delimiter=',')
    row_count = 1
    for countries_row in countries_reader:
        if row_count > 1:
            country_information_map[countries_row[0]] = countries_row
        row_count = row_count + 1

countries_series_map = {}
#Read the file with information about the series
with open(directory + countries_series_file, encoding='utf8') as csv_countries_series_file:
    countries_series_reader = csv.reader(csv_countries_series_file, delimiter=',')
    row_count = 1
    for countries_series_row in countries_series_reader:                
        if row_count > 1:
            countries_series_map[countries_series_row[0]+countries_series_row[1]] = countries_series_row
        row_count = row_count + 1

foot_note_map = {}
#Read the file with information about the foot notes of indicators.
with open(directory + foot_note_file, encoding='utf8') as csv_foot_note_file:
    foot_note_reader = csv.reader(csv_foot_note_file, delimiter=',')
    row_count = 1
    for foot_note_row in foot_note_reader:
        if row_count > 1:
            if foot_note_map.get(foot_note_row[0]+foot_note_row[1]) == None:
                foot_note_map[foot_note_row[0]+foot_note_row[1]] = []
            foot_note_map[foot_note_row[0]+foot_note_row[1]].append(row_count)
        row_count = row_count + 1

series_map = {}
#Read the file with information about the series (indicator)
with open(directory + series_file, encoding = 'utf8') as csv_series_file:
    series_reader = csv.reader(csv_series_file, delimiter=',')
    row_count = 1
    for series_row in series_reader:
        if row_count > 1:
            series_map[series_row[0]] = series_row
        row_count = row_count + 1

series_time_map = {}
#Read the file with descriptions of series by year
with open(directory + series_time_file, encoding = 'utf8') as csv_series_time_file:
    series_time_reader = csv.reader(csv_series_time_file, delimiter = ',')
    row_count = 1
    for series_time_row in series_time_reader:
        if row_count > 1:
            if series_time_map.get(series_time_row[0]) == None:
                series_time_map[series_time_row[0]] = []
            series_time_map[series_time_row[0]].append(series_time_row)
        row_count = row_count + 1

indicators_dict = []
row_count = 1
for indicator in indicators_array:
    if row_count % 1000 == 0:
        print('Indicator ' + str(row_count))
        
    if country_information_map.get(indicator.country_code) != None:
        indicator.insert_country_info(country_information_map.get(indicator.country_code))
        
    if countries_series_map.get(indicator.country_code+indicator.indicator_code) != None:
        indicator.insert_indicator_description(countries_series_map.get(indicator.country_code+indicator.indicator_code))
        
    if foot_note_map.get(indicator.country_code+indicator.indicator_code) != None:
        for foot_note in foot_note_map.get(indicator.country_code+indicator.indicator_code):
            indicator.insert_foot_note(foot_note_row)
            
    if series_map.get(indicator.indicator_code) != None:
        indicator.insert_indicator_info(series_map.get(indicator.indicator_code))
        
    if series_time_map.get(indicator.indicator_code) != None:
        for series_time_row in series_time_map.get(indicator.indicator_code):
            indicator.insert_indicator_time_info(series_time_row)

    indicators_dict.append(indicator.to_dict())
    row_count = row_count + 1

print('Inserting into MongoDB')
indicators.insert_many(indicators_dict)
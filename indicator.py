# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

from country_info import CountryInfo
from foot_note import FootNote
from indicator_info import IndicatorInfo

class Indicator:
    
    def __init__(self):
        self.country_name = None
        self.country_code = None
        self.indicator_name = None
        self.indicator_code = None
        self.indicator_values = None
        self.country_info = None
        self.indicator_description = None
        self.foot_note = []
    
    def insert_indicator_values(self, indicator_data):
        """
        Indicator data is an array containing in the first positions
        the country name, coutry code, indicator name and indicator code.
        The next positions are the values of the particular indicator from
        1960 to 2017.
        """
        self.country_name = indicator_data[0]
        self.country_code = indicator_data[1]
        self.indicator_name = indicator_data[2]
        self.indicator_code = indicator_data[3]
        self.indicator_values = indicator_data[4:]
        
    def insert_country_info(self, country_info):
        """
        Country info is an array of 30 elements containing data about the Country
        """
        self.country_info = CountryInfo(country_info)
        
    def insert_indicator_description(self, indicator_description):
        """
        Indicator description is an array containing in the first position the
        country code, in the second position the series code (indicator) 
        and in last position the description of series. 
        """
        self.indicator_description = indicator_description[2]
        
    def insert_foot_note(self, foot_note):
        """
        Foot note is an array containing int hte first position the country code,
        in the second position the indicator code, in the third position the
        year of foot note and in the last position the description of foot note.
        """
        self.foot_note.append(FootNote(foot_note[2], foot_note[3]))
        
    def insert_indicator_info(self, indicator_info):
        """
        Indicator info in an array containing the information about the indicator.
        """
        self.indicator_info = IndicatorInfo(indicator_info)
        
    def insert_indicator_time_info(self, indicator_time_info):
        """
        Indicator time info in an array containing the information about the indicator
        in the first position in a year in second position. The last position contains
        the description.
        """
        self.indicator_info.insert_time_info(indicator_time_info[1], indicator_time_info[2])
        
    def to_dict(self):
        foot_notes = []
        for i in self.foot_note:
            foot_notes.append(i.to_dict())
        indicator_as_dict = self.__dict__
        indicator_as_dict['country_info'] = self.country_info.to_dict()
        indicator_as_dict['foot_note'] = foot_notes
        indicator_as_dict['indicator_info'] = self.indicator_info.to_dict()
        return indicator_as_dict
        
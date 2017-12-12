# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

from series_time_info import SeriesTimeInfo

class IndicatorInfo:
    
    def __init__(self, indicator_info):
        """
        Indicator info in an array containing the information about the indicator.
        """
        self.series_code = indicator_info[0]
        self.topic = indicator_info[1]
        self.indicator_name = indicator_info[2]
        self.short_definition = indicator_info[3]
        self.long_definition = indicator_info[4]
        self.unit_of_measure = indicator_info[5]
        self.periodicity = indicator_info[6]
        self.base_period = indicator_info[7]
        self.other_notes = indicator_info[8]
        self.aggregation_method = indicator_info[9]
        self.limitations_and_exceptions = indicator_info[10]
        self.notes_from_original_source = indicator_info[11]
        self.general_comments = indicator_info[12]
        self.source = indicator_info[13]
        self.statistical_concept_and_methodology = indicator_info[14]
        self.development_relevance = indicator_info[15]
        self.related_source_links = indicator_info[16]
        self.other_web_links = indicator_info[17]
        self.related_indicators = indicator_info[18]
        self.licence_type = indicator_info[19]
        self.time_info = []
        
    def insert_time_info(self, year, description):
        new_info = SeriesTimeInfo(year, description)
        self.time_info.append(new_info)
        
    def to_dict(self):
        time_infos = []
        for i in self.time_info:
            time_infos.append(i.to_dict())
        indicator_info_as_dict = self.__dict__
        indicator_info_as_dict['time_info'] = time_infos
        return indicator_info_as_dict
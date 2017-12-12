# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

class SeriesTimeInfo:
    
    def __init__(self, year, description):
        self.year = year
        self.description = description
        
    def to_dict(self):
        return self.__dict__
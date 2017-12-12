# -*- coding: utf-8 -*-
"""
Projeto disciplina PCS5031 - Introdução à Ciência dos Dados
@author: Rodrigo Müller de Carvalho
@author: Eduardo Dias Filho
"""

class CountryInfo:
    
    def __init__(self, country_data):
        """
        country_data is an array containing the info about a country.
        """
        self.country_code = country_data[0]
        self.short_name = country_data[1]
        self.table_name = country_data[2]
        self.long_name = country_data[3]
        self.two_alpha_code = country_data[4]
        self.currency_unit = country_data[5]
        self.special_notes = country_data[6]
        self.region = country_data[7]
        self.income_group = country_data[8]
        self.wb_2_code = country_data[9]
        self.national_accounts_base_year = country_data[10]
        self.national_accounts_reference_year = country_data[11]
        self.sna_price_valuation = country_data[12]
        self.lending_category = country_data[13]
        self.other_groups = country_data[14]
        self.system_of_national_accounts = country_data[15]
        self.alternative_conversion_factor = country_data[16]
        self.ppp_survey_year = country_data[17]
        self.balance_of_payments_manual_in_use = country_data[18]
        self.external_debt_reporting_status = country_data[19]
        self.system_of_trade = country_data[20]
        self.government_accounting_concept = country_data[21]
        self.imf_data_dissemination = country_data[22]
        self.latest_population_census = country_data[23]
        self.latest_household_survey = country_data[24]
        self.source_of_most_recent_income_and_expenditure_data = country_data[25]
        self.vital_registration_complete = country_data[26]
        self.latest_agricultural_census = country_data[27]
        self.latest_industrial_data = country_data[28]
        self.latest_trade_data = country_data[29]
        self.latest_water_withdrawal_data = country_data[30]
        
    def to_dict(self):
        return self.__dict__
import pandas as pd
import pylab as plt
import numpy as np
import scipy as sc
import scipy.stats
import matplotlib.pyplot as plt

df = pd.read_csv('./kickstarter_data_full.csv', sep=',')
column_of_interest = ''
columns_for_edit = 'goal', 'pledged'
total_rows = df.count
uniqueVals = []

#Currency Definitions

#the "rates" indicate the number by which each currency must be multiplied
#as of 2018 in order to be represented in a US dollar amount

us_dollar = 'USD'
us_rate = 1.0
#AUD = 0.75 USD
australian_dollar = 'AUD'
australian_rate = 0.75
#CAD = 0.78 USD
canadian_dollar = 'CAD'
canadian_rate = 0.78
#CHF = USD
swiss_franc = 'CHF'
swiss_rate = 1.0
#DKK = 0.16 USD
danish_krone = 'DKK'
danish_rate = 0.16
#EUR = 1.20 USD
euro = 'EUR'
euro_rate = 1.20
#GBP = 1.35 USD
british_pound = 'GBP'
british_rate = 1.35
#HKD = 0.13 USD
hong_kong_dollar = 'HKD'
hong_kong_rate = 0.13
#MXN = 0.052 USD
mexican_peso = 'MXN'
mexican_rate = 0.052
#NOK = 0.12 USD
norwegian_krone = 'NOK'
norwegian_rate = 0.12
#NZD = 0.70 USD
new_zealand_dollar = 'NZD'
new_zealand_rate = 0.70
#SEK = 0.11 USD
swedish_krona = 'SEK'
swedish_rate = 0.11
#SGD = 0.75 USD
singapore_dollar = 'SGD'
singapore_rate = 0.75


#find_unique_currencies prints ['$' 'Fr ' 'kr' '£' '€']
def find_unique_currency_symbols():
    column_of_interest = 'currency_symbol'
    my_list = df[column_of_interest]
    uniqueVals = np.unique(my_list) #['$' 'Fr ' 'kr' '£' '€']
    print(uniqueVals)

#We will use currencies rather than symbols because it prints more
#currency types, which suggests the currency symbols are not entirely thorough/
#accurate. This method prints the the below:
#['AUD' 'CAD' 'CHF' 'DKK' 'EUR' 'GBP' 'HKD' 'MXN' 'NOK' 'NZD' 'SEK' 'SGD''USD']

def find_unique_currencies():
    column_of_interest = 'currency'
    my_list = df[column_of_interest]
    uniqueVals = np.unique(my_list)
    print(uniqueVals)


def convert_to_dollars():
     currency_list = df['currency']
     goal_list = df['goal']
     pledged_list = df['pledged']
     i = 1
     while i < len(currency_list):
        if currency_list.at[i] == us_dollar:
          goal_list.at[i] = pd.to_numeric(goal_list.at[i])
          pledged_list.at[i] = pd.to_numeric(pledged_list.at[i])
          i+=1
        elif currency_list[i] == australian_dollar:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i]) * australian_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * australian_rate
            i+=1
        elif currency_list.at[i] == canadian_dollar:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i]) * canadian_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * canadian_rate
            i+=1
        elif currency_list.at[i] == swiss_franc:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i]) * swiss_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * swiss_rate
            i+=1
        elif currency_list.at[i] == danish_krone:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i]) * danish_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * danish_rate
            i+=1
        elif currency_list.at[i] == euro:
            goal_list.at[i] = pd.to_numeric(goal_list[i])* euro_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * euro_rate
            i+=1
        elif currency_list.at[i] == british_pound:
            goal_list.at[i] = pd.to_numeric(goal_list[i])* british_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * british_rate
            i+=1
        elif currency_list.at[i] == hong_kong_dollar:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* hong_kong_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * hong_kong_rate
            i+=1
        elif currency_list.at[i] == mexican_peso:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* mexican_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * mexican_rate
            i+=1
        elif currency_list.at[i] == norwegian_krone:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* norwegian_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * norwegian_rate
            i+=1
        elif currency_list.at[i] == new_zealand_dollar:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* new_zealand_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * new_zealand_rate
            i+=1
        elif currency_list.at[i] == singapore_dollar:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* singapore_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * singapore_rate
            i+=1
        elif currency_list.at[i] == swedish_krona:
            goal_list.at[i] = pd.to_numeric(goal_list.at[i])* swedish_rate
            pledged_list.at[i] = pd.to_numeric(pledged_list.at[i]) * swedish_rate
            i+=1

     df['goal_list_dollars'] = goal_list.values
     df['pledged_list-dollars'] = pledged_list.values

convert_to_dollars()

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
#currency types, which suggests the currency symbols are not entirely
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
    pledged_list = ['pledged']
    i = 1
    while i < len(currency_list):
       if currency_list[i] == us_dollar:
           pd.to_numeric(goal_list[i])
          # pd.to_numeric(pledged_list[i])
           i+=1
       elif currency_list[i] == australian_dollar:
           pd.to_numeric(goal_list[i]) * australian_rate
           i+=1
       elif currency_list[i] == canadian_dollar:
           pd.to_numeric(goal_list[i]) * canadian_rate
            # pd.to_numeric(pledged_list[i])
           i+=1
       elif currency_list[i] == swiss_franc:
           pd.to_numeric(goal_list[i]) * swiss_rate
          # pd.to_numeric(pledged_list[i])
           i+=1
       elif currency_list[i] == danish_krone:
           pd.to_numeric(goal_list[i]) * danish_rate
               # pd.to_numeric(pledged_list[i])
           i+=1
       elif currency_list[i] == euro:
            pd.to_numeric(goal_list[i])* euro_rate
            #    pd.to_numeric(pledged_list[i])*(1.20)
            i+=1
       elif currency_list[i] == british_pound:
            pd.to_numeric(goal_list[i])* british_rate
           # pd.to_numeric(pledged_list[i])*(1.35)
            i+=1
       elif currency_list[i] == hong_kong_dollar:
           pd.to_numeric(goal_list[i])* hong_kong_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1
       elif currency_list[i] == mexican_peso:
           pd.to_numeric(goal_list[i])* mexican_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1
       elif currency_list[i] == norwegian_krone:
           pd.to_numeric(goal_list[i])* norwegian_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1
       elif currency_list[i] == new_zealand_dollar:
           pd.to_numeric(goal_list[i])* new_zealand_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1
       elif currency_list[i] == singapore_dollar:
           pd.to_numeric(goal_list[i])* singapore_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1
       elif currency_list[i] == swedish_krona:
           pd.to_numeric(goal_list[i])* swedish_rate
          # pd.to_numeric(pledged_list[i]) *(0.11)
           i+=1


    print(goal_list)
    #print(pledged_list)

convert_to_dollars()

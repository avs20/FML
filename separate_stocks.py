import os 

import sys 

import pandas as pd

data = pd.read_csv('all_dataset_2018.csv')

# data.shape

# data.head()

# data.STOCK.unique()
os.mkdir("2018_individual_files")
os.chdir("2018_individual_files")
for stock in data.STOCK.unique():
    single_stock_df = data.query("STOCK == @stock")
    single_stock_df.to_csv('{}_2018.csv'.format(stock), index=False)
    

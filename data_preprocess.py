import pandas as pd
import os

# Data preprocessing - Merge all csv file
for inputfile in os.listdir(r'./data'):
    data = pd.read_csv('data/'+inputfile)
    data.to_csv('data/data.csv', mode='a', index=False, header=None)

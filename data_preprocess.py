import pandas as pd
import glob

listing = glob.glob(r'./data/rawdata/*.csv')
# Data preprocessing - Merge all csv file
rawdata = pd.DataFrame()

for inputfile in listing:
    data = pd.read_csv(inputfile)
    rawdata = pd.concat([rawdata, data])

rawdata.to_csv('data/data.csv', mode='a', index=False)


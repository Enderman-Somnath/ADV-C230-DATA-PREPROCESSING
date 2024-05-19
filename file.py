import pandas as pd
dataset = pd.read_csv(r'country_vaccination.csv')
print("Shape of  given dataset:",dataset.shape)
print("Count of column:",len(dataset.columns))
print("Name of parameter used:",dataset.columns)
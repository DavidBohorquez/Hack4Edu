import pandas as pd
import sweetviz as sv


url = 'https://raw.githubusercontent.com/DavidBohorquez/Hack4Edu/main/Dropout_Academic%20Success%20-%20Sheet1.csv'
df = pd.read_csv(url)
#df = pd.read_csv(url)

df.head()

#EDA using Autoviz
sweet_report = sv.analyze(df)

#Saving results to HTML file
sweet_report.show_notebook()
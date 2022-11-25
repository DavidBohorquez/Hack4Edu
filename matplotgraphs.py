import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_URL = ('https://raw.githubusercontent.com/DavidBohorquez/Hack4Edu/main/Dropout_Academic%20Success%20-%20Sheet1.csv')
data = pd.read_csv(DATA_URL)

lables = ["yes", "no"]
scholarship_holder_data = data['Scholarship holder']

scholarship_grp = scholarship_holder_data.groupby(scholarship_holder_data).size()
df_scholarship = pd.DataFrame(scholarship_grp) 
print(df_scholarship, type(df_scholarship))

plt.pie(df_scholarship)
plt.show()
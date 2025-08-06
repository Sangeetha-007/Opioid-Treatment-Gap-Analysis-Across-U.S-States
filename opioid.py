import pandas as pd
import numpy as np
import openpyxl
import plotly.express as px


df = pd.read_excel('/Users/sangeetha/Downloads/SUDORS-Fatal-Overdose-Data.xlsx', sheet_name='Data')
#print(df[df['Jurisdiction'] == 'Overall'])

#Filtering out Overall data
df_filtered = df[df['Jurisdiction'] != 'Overall']

print(df_filtered)

print(pd.Series(list(df.columns)))


columns_to_drop = df_filtered.columns[190:275]  # 275 because the end index is exclusive

# Drop those columns
df_filtered = df_filtered.drop(columns=columns_to_drop)


columns_to_drop=df_filtered.columns[30:42]
df_filtered=df_filtered.drop(columns=columns_to_drop)
print(df_filtered)

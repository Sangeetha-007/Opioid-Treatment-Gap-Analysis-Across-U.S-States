import pandas as pd
import numpy as np
import openpyxl


df = pd.read_excel('/Users/sangeetha/Downloads/SUDORS-Fatal-Overdose-Data.xlsx', sheet_name='Data')
#print(df[df['Jurisdiction'] == 'Overall'])

#Filtering out Overall data
df_filtered = df[df['Jurisdiction'] != 'Overall']

print(df_filtered)
import pandas as pd
import numpy as np
import openpyxl
import plotly.express as px
import us
import os
import plotly.io as pio
pio.renderers.default = 'browser'


df = pd.read_excel('/Users/sangeetha/Downloads/SUDORS-Fatal-Overdose-Data.xlsx', sheet_name='Data')
#print(df[df['Jurisdiction'] == 'Overall'])

print(df.isnull())
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


# Convert full state names to abbreviations
df_filtered['Jurisdiction'] = df_filtered['Jurisdiction'].apply(lambda x: us.states.lookup(x).abbr if us.states.lookup(x) else x)

df_2023 = df_filtered[df_filtered['year'] == 2023]


fig = px.choropleth(df_2023,
                        locations='Jurisdiction',
                        locationmode="USA-states",
                        scope="usa",
                        color='opioids_rate',  # Column with the data to color the states
                        color_continuous_scale="Viridis_r", # Choose a color scale
                        title="Opioid Rate Per State in 2023")
fig.show() 
os.makedirs("Visualization", exist_ok=True)
fig.write_html("Visualization/opioid_map_2023.html")


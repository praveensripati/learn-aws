# import the pandas library
import pandas as pd

# import the altair library
import altair as alt

# load the data 'tsc00001.csv' into the pandas data frame
data = pd.read_csv('tsc00001.csv')

# load the data 'tsc00001.csv' into the pandas data frame
data = pd.read_csv('tsc00001.csv')

# drop the 'unit' column
data = data.drop(columns=['unit'])

# select the rows where 'geo' is 'IT'
data = data[data['geo'] == 'IT']

# drop the 'geo' column
data = data.drop(columns=['geo'])

# use melt() as follows:
# - use 'sectperf' as the id_vars
# - use 'date' as var_name
# - use 'value' as value_name
data = data.melt(id_vars=['sectperf'], var_name='date', value_name='value')

# convert the 'date' column to integers
data['date'] = data['date'].str.replace('M', '').astype(int)

# convert the 'value' column to float
data['value'] = data['value'].str.replace(',', '.').astype(float)

# draw a line chart in Python Altair as follows:
# - use 'data' as the data source
# - use 'date' for the x axis
# - use the 'value' column for the y axis
# - use the 'sectperf' for color
# done creating the chart
chart = alt.Chart(data).mark_line().encode(
    x='date:Q',
    y='value:Q',
    color='sectperf:N'
)

# save the chart to 'chart.html'
chart.save('chart.html')

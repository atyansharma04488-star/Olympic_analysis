import pandas as pd
import helper

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

# Test individual functions
print(helper.fetch_medal_tally(df, 'Overall', 'India'))
print(helper.country_year_list(df))
print(helper.data_over_time(df, 'region'))
print(helper.most_successful(df, 'Basketball'))

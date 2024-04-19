"""
Web Scrapping 1 (Read only 1 CSV file from a website)

Loops can be added to iterate and download all the CSV files from the website
Target website = "https://www.football-data.co.uk/data.php"

#Steps
1. Reading 1 CSV file from website
2. Showing dataframe
3. Rename columns
4. Show dataframe

"""

import pandas as pd


# Assign the dataframe to a variable
df_EPL_2023 = pd.read_csv(f'https://www.football-data.co.uk/mmz4281/2324/SP1.csv')

print(df_EPL_2023.columns)

### Change the column names as per preference
    #'Use dictionary literals or decorator to change the column names'
df_EPL_2023.rename(columns={
    'FTAG': 'Full Time Away Goals',
    'FTHG': 'Full Time Home Goals',
    'FTR': 'Full Time Result',
    'HTHG': 'Half Time Home Goals',
    'HTAG': 'Half Time Away Goals',
    'HTR': 'Half Time Result',
    'Referee': 'Name of the referee for the match',
    'HS': 'Home Shots',
    'AS': 'Away Shots',
    'HST': 'Home Shots on Target',
    'AST': 'Away Shots on Target',
    'HF': 'Home Fouls',
    'AF': 'Away Fouls',
    'HC': 'Home Corners',
    'AC': 'Away Corners',
    'HY': 'Home Yellow Cards',
    'AY': 'Away Yellow Cards',
    'HR': 'Home Red Cards',
    'AR': 'Away Red Cards'
}, inplace=True)

print(df_EPL_2023.columns)


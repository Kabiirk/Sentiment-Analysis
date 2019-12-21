import pandas as pd
import datetime
import re

#loading the dataframes
echo = pd.read_csv(r'C:\Users\kabii\Desktop\amazon_review\reviews_echo.csv')
echo_dot = pd.read_csv(r'C:\Users\kabii\Desktop\amazon_review\reviews_echodot.csv')

#data cleaning and formatting


#declarations
i = 0
n1 = len(echo['Reviews'])
n2 = len(echo_dot['Reviews'])


#coverting date collumn to datetime
echo['Date'] =  pd.to_datetime(echo['Date'], format='%d %B %Y')
echo_dot['Date'] =  pd.to_datetime(echo_dot['Date'], format='%d-%b-%y')


#removing special charcters like 'Â' etc.
for i in range(n1):
    re.sub("Â|â|€|™|&amp;|ðŸ|»|ðŸ˜|$|â€™", "", echo['Reviews'][i])
    
for i in range(n2):
    re.sub("Â|â|€|™|&amp;|ðŸ|»|ðŸ˜|$|â€™", "", echo_dot['Reviews'][i])

print(echo.dtypes)
print(echo_dot.dtypes)


#export data to a new file
echo_sanitized = echo.to_csv(r'C:\Users\kabii\Desktop\echo_sanitized.csv')
echo_dot_sanitized = echo_dot.to_csv(r'C:\Users\kabii\Desktop\echo_dot_sanitized.csv')
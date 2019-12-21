import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()

def sentiment_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

#test the function
'''
sentence = 'This is a placeholder sentence.'
dicy = sentiment_scores(sentence)
print(list(dicy.values()))
'''

#load csv into dataframes
echo_sanitized = pd.read_csv(r'C:\Users\kabii\Desktop\echo_sanitized.csv')
echo_dot_sanitized = pd.read_csv(r'C:\Users\kabii\Desktop\echo_dot_sanitized.csv')

#declarations
i = 0
n1 = len(echo_sanitized)
n2 = len(echo_dot_sanitized)

#df for echo
neg1 = []
neu1 = []
pos1 = []
com1 = [] 

#df for echo dot
neg2 = []
neu2 = []
pos2 = []
com2 = []

#generate scores and dataframe for echo
for i in range(n1):
    dicy1 = sentiment_scores(echo_sanitized['Reviews'][i])
    neg1.append(list(dicy1.values())[0])
    pos1.append(list(dicy1.values())[1])
    neu1.append(list(dicy1.values())[2])
    com1.append(list(dicy1.values())[3])
df1 = pd.DataFrame(list(zip(neg1, neu1, pos1, com1)) , columns =['Negative', 'Neutral', 'Positive', 'Compound'])

#generate scores and dataframe for echo dot
for i in range(n2):
    dicy2 = sentiment_scores(echo_dot_sanitized['Reviews'][i])
    neg2.append(list(dicy2.values())[0])
    pos2.append(list(dicy2.values())[1])
    neu2.append(list(dicy2.values())[2])
    com2.append(list(dicy2.values())[3])
df2 = pd.DataFrame(list(zip(neg2, neu2, pos2, com2)) , columns =['Negative', 'Neutral', 'Positive', 'Compound'])

#Putting the final values down in a csv file
echo_sanitized_sentiment_scores = df1.to_csv(r'C:\Users\kabii\Desktop\echo_sanitized_sentiment_scores.csv')
echo_dot_sanitized_sentiment_scores = df2.to_csv(r'C:\Users\kabii\Desktop\echo_dot_sanitized_sentiment_scores.csv')
import pandas as pd

#reading the necesarry files into dataframes
#echo
echo_sanitized = pd.read_csv(r'C:\Users\kabii\Desktop\echo_sanitized.csv')
echo_sanitized_sentiment_scores = pd.read_csv(r'C:\Users\kabii\Desktop\echo_sanitized_sentiment_scores.csv')
echo_emotion = pd.read_csv(r'C:\Users\kabii\Desktop\echo_emotion_dataframe.csv')

#echo dot
echo_dot_sanitized = pd.read_csv(r'C:\Users\kabii\Desktop\echo_dot_sanitized.csv')
echo_dot_sanitized_sentiment_scores = pd.read_csv(r'C:\Users\kabii\Desktop\echo_dot_sanitized_sentiment_scores.csv')
echo_dot_emotion = pd.read_csv(r'C:\Users\kabii\Desktop\echo_dot_emotion_dataframe.csv')

#final echo dataframe with new index
df1 = echo_sanitized.drop(columns="Unnamed: 0")
df2 = echo_sanitized_sentiment_scores.drop(columns="Unnamed: 0")
df3 = echo_emotion.drop(columns="Unnamed: 0")
echo_sanitized_sentiment_emotion_final = pd.concat([df1, df2, df3], axis=1)


#final echo dot dataframe with new index
df4 = echo_dot_sanitized.drop(columns="Unnamed: 0")
df5 = echo_dot_sanitized_sentiment_scores.drop(columns="Unnamed: 0")
df6 = echo_dot_emotion.drop(columns="Unnamed: 0")
echo_dot_sanitized_sentiment_emotion_final = pd.concat([df4, df5, df6], axis=1)


#printing final dataframes
print(echo_sanitized_sentiment_emotion_final)
print(echo_dot_sanitized_sentiment_emotion_final)

#creating final file with all the sentiment polarity scores
#echo_sentiment_dataframe = echo_sanitized_sentiment_final.to_csv(r'C:\Users\kabii\Desktop\echo_sentiment_dataframe.csv')
#echo_dot_sentiment_dataframe = echo_dot_sanitized_sentiment_final.to_csv(r'C:\Users\kabii\Desktop\echo_dot_sentiment_dataframe.csv')


#creating final file with all the sentiment and emotion polarity scores
echo_Final_analysis = echo_sanitized_sentiment_emotion_final.to_csv(r'C:\Users\kabii\Desktop\echo(FINAL SCORES).csv')
echo_dot_Final_analysis = echo_dot_sanitized_sentiment_emotion_final.to_csv(r'C:\Users\kabii\Desktop\echo_dot(FINAL SCORES).csv')

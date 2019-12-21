library('syuzhet')
echo <- read.csv(file = 'C:/Users/kabii/Desktop/echo_sentiment_dataframe.csv', stringsAsFactors = FALSE)
echo_dot <- read.csv(file = 'C:/Users/kabii/Desktop/echo_dot_sentiment_dataframe.csv', stringsAsFactors = FALSE)

emotion_echo  = get_nrc_sentiment(echo['Reviews'][[1]])
emotion_echo_dot  = get_nrc_sentiment(echo_dot['Reviews'][[1]])

write.csv(emotion_echo, file = 'C:/Users/kabii/Desktop/echo_emotion_dataframe.csv')
write.csv(emotion_echo_dot, file = 'C:/Users/kabii/Desktop/echo_dot_emotion_dataframe.csv')
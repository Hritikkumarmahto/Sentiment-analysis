import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Prepare the data
nltk.download('vader_lexicon')

#Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

while True:
    #Get user input
    text = input("Enter a sentence for sentiment analysis (or 'quit' to exit): ")

    # Check if the user wants to quit
    if text.lower() == 'quit':
        break

    #Perform sentiment analysis
    scores = sid.polarity_scores(text)

    #Interpret the sentiment scores
    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    #Print the sentiment
    print("Sentiment:", sentiment)
    print()

print("Thank you for using the sentiment analysis tool!")

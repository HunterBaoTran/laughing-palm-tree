import os
from serpapi import GoogleSearch
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('SERPAPI_KEY')

# Ensure the required nltk data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the GoogleSearch client
client = GoogleSearch({
    "q": "IQ Viet My reviews",
    "engine": "google",
    "hl": 'en',
    "gl": "us",
    "api_key": api_key,
    "num": 100
})

# Fetch search results
results = client.get_dict()
snippets = [result['snippet'] for result in results['organic_results']]

#Below Commented out Code is for Sentiment Analysis for another project I am working on
#snippets = [result['snippet'] for result in results['organic_results'] if 'Ukraine' in result['snippet'] or 'Russia' in result['snippet']]

# Preprocess the text data
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

clean_snippets = [preprocess(snippet) for snippet in snippets]

# Perform sentiment analysis using VADER
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

sentiments = [analyze_sentiment(snippet) for snippet in clean_snippets]
sentiment_labels = ['Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral' for score in sentiments]

# Visualize the sentiment results
df = pd.DataFrame({
    'Snippet': snippets,
    'Sentiment': sentiment_labels
})

sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Sentiment Analysis of IQ Viet My Tutoring Centers')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
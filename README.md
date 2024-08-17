# Sentiment Analysis of IQ Viet My Tutoring Center

## Overview

This project performs a sentiment analysis on Google search results related to the tutoring center IQ Viet My. The goal is to analyze public sentiment (Positive, Neutral, or Negative) about the center based on search result snippets, providing insights into how the center is perceived online.

![Sentiment Analysis of IQ Viet My Tutoring Centers](https://github.com/user-attachments/assets/99398748-9651-43a2-8778-d6a98661faff)


## Project Structure

- **main.py**: The main Python script that fetches Google search results using SerpAPI, preprocesses the text data, performs sentiment analysis using VADER, and visualizes the results.
- **.env**: A file that stores environment variables, including the SerpAPI key (not included in version control).
- **requirements.txt**: A list of dependencies required to run the project.
- **README.md**: Documentation for the project.

## How It Works

1. **Google Search Results**: The script uses the SerpAPI to fetch Google search results for the query `"IQ Viet My tutoring center reviews"`.
2. **Text Preprocessing**: The raw text snippets from the search results are cleaned and processed to remove stopwords, punctuation, and to lemmatize the words.
3. **Sentiment Analysis**: Each snippet undergoes sentiment analysis using the VADER SentimentIntensityAnalyzer, which classifies the sentiment as Positive, Negative, or Neutral.
4. **Visualization**: The results are visualized in a bar chart that shows the distribution of sentiments.

## Requirements

- Python 3.6+
- Required Python packages:
  - serpapi
  - vaderSentiment
  - pandas
  - matplotlib
  - nltk
  - python-dotenv

You can install the required packages using:
```bash
pip install -r requirements.txt

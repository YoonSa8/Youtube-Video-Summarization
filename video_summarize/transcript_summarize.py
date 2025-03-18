from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from transformers import pipeline
from textblob import TextBlob
import re
import nltk
import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# text summarization function


def summarize_text(text, max_length=100000):
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(
        text[:2000], max_length=max_length, min_length=50, do_sample=False)  # Limit the input text length
    return summary[0]['summary_text']

# extract keywords


def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Tokenization and Lemmatization
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower())
             for word in words if word.isalnum()]

    # Filter out stopwords and short words
    keywords = [
        word for word in words if word not in stop_words and len(word) > 1]

    # Use Counter to get word frequencies
    word_freq_dict = {word: keywords.count(word) for word in set(keywords)}

    # Sort words by frequency in descending order
    top_keywords = sorted(
        word_freq_dict, key=word_freq_dict.get, reverse=True)[:5]
    return top_keywords


def topic_modeling(text):
    vectorizer = CountVectorizer(
        max_df=0.95, min_df=0.05, stop_words='english')
    tf = vectorizer.fit_transform([text])
    lda_model = LatentDirichletAllocation(
        n_components=5, max_iter=5, learning_method='online', random_state=42)
    lda_model.fit(tf)
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda_model.components_):
        # Top 5 words for each topic
        topics.append([feature_names[i] for i in topic.argsort()[:-6:-1]])
    return topics

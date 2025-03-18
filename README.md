In this Repo I'll create some projects related to web scrapping 

1- YouTube Channel Analytics

Overview

The YouTube Channel Analytics project is a data-driven web application that scrapes data from YouTube to analyze the highest-viewed and most-subscribed YouTube channels. The project provides insights into trends, engagement metrics, and content strategies used by top creators.

Features

Web Scraping: Extracts data on top YouTubers using the YouTube API.

Data Analysis: Analyzes subscriber count, total views, video counts, and engagement metrics.

Trend Identification: Identifies patterns in content strategies among high-performing channels.

Visualization: Generates charts and graphs to present the findings in an interactive way.

2- YouTube Video Summarizer
Overview 
The YouTube Video Summarizer is a Streamlit-based web application that extracts transcripts from YouTube videos and generates concise summaries. Additionally, the app performs keyword extraction, topic modeling, and sentiment analysis to provide deeper insights into the video's content.

Features

Transcript Extraction: Fetches the transcript of a YouTube video using youtube_transcript_api.

Summarization: Uses HuggingFace's Transformer models to generate a concise summary of the transcript.

Keyword Extraction: Identifies the most relevant keywords from the transcript using NLP techniques.

Topic Modeling: Applies Latent Dirichlet Allocation (LDA) to extract key topics.

Sentiment Analysis: Uses TextBlob to analyze the sentiment (polarity and subjectivity) of the transcript.

3-  CV-Job Matching System using scrapped Linkedin jobs

📌 Project Overview

This project evaluates how well a candidate’s CV matches a given job description. It uses TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity to compute similarity scores between job descriptions and CVs.

📂 Project Structure

📁 CV-Job Matching
│── 📂 data
│   ├── extracted_cvs.csv  (Extracted text from CVs)
│   ├── processed_job_descriptions.csv  (Cleaned job descriptions)
│   ├── cv_job_similarity_scores.csv  (Similarity scores between CVs & jobs)
│   ├── top_matched_cvs.csv  (Best CV match for each job)
│── 📂 scripts
│   ├── extract_cvs.py  (Extract text from DOCX CVs)
│   ├── extract_jobs.py  (Preprocess job descriptions)
│   ├── compute_similarity.py  (TF-IDF similarity calculation)
│   ├── rank_matches.py  (Rank best CVs for each job)
│── README.md  (Project Documentation)


---

🛠️ How It Works

1️⃣ Extract CV Text and scrape LinkedIn posted jobs

Reads multiple DOCX CV files.

Extracts raw text from each CV.

Stores the extracted text in a structured CSV file.

Scrape linkedIn jobs and Clean job descriptions

2️⃣ Process Job Descriptions

Loads job descriptions from a CSV file.

Cleans and prepares job text.


3️⃣ Compute Similarity Scores

Uses TF-IDF vectorization to convert CVs and job descriptions into numerical vectors.

Computes Cosine Similarity to measure how closely each CV matches each job.

Outputs a similarity matrix where higher scores indicate a better match.


4️⃣ Rank the Best Matches

Sorts CVs for each job by similarity score.

Extracts the top-matching CV for each job.

Saves ranked results in a CSV file.



---

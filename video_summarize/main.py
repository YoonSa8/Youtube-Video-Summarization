import streamlit as st
from extract_video import extract_video_id, get_transcript
from transcript_summarize import extract_keywords, topic_modeling, summarize_text
from textblob import TextBlob
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound
# Main Streamlit app


def main():
    st.title("YouTube Video Summarizer")

    # User input for YouTube video URL
    video_url = st.text_input("Enter YouTube Video URL:", "")

    # User customization options
    max_summary_length = st.slider("Max Summary Length:", 1000, 20000, 50000)

    if st.button("Summarize"):
        try:
            # Extract video ID from URL
            video_id = extract_video_id(video_url)
            if not video_id:
                st.error("Invalid YouTube URL. Please enter a valid URL.")
                return

            # Get transcript of the video
            transcript = get_transcript(video_id)
            if not transcript:
                st.error("Transcript not available for this video.")
                return

            video_text = ' '.join([line['text'] for line in transcript])

            # Summarize the transcript
            summary = summarize_text(video_text, max_length=max_summary_length)

            # Extract keywords from the transcript
            keywords = extract_keywords(video_text)

            # Perform topic modeling
            topics = topic_modeling(video_text)

            # Perform sentiment analysis
            sentiment = TextBlob(video_text).sentiment

            # Display summarized text, keywords, topics, and sentiment
            st.subheader("Video Summary:")
            st.write(summary)

            st.subheader("Keywords:")
            st.write(keywords)

            st.subheader("Topics:")
            for idx, topic in enumerate(topics):
                st.write(f"Topic {idx+1}: {', '.join(topic)}")

            st.subheader("Sentiment Analysis:")
            st.write(f"Polarity: {sentiment.polarity}")
            st.write(f"Subjectivity: {sentiment.subjectivity}")

        except TranscriptsDisabled:
            st.error("Transcripts are disabled for this video.")
        except NoTranscriptFound:
            st.error("No transcript found for this video.")
        except Exception as e:
            st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

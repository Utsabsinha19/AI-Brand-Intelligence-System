from backend.ingestion.load_data import load_dataset

from backend.nlp.preprocessing import clean_text
from backend.nlp.sentiment import analyze_sentiment
from backend.nlp.topic_model import generate_topics
from backend.nlp.keywords import extract_keywords
from backend.nlp.complaint_detection import detect_complaint
from backend.nlp.insights import generate_insight

def run_pipeline(file_path):

    df = load_dataset(file_path)

    df['cleaned_text'] = df['text'].apply(clean_text)

    df['sentiment'] = df['cleaned_text'].apply(analyze_sentiment)

    df['complaint'] = df['cleaned_text'].apply(detect_complaint)

    topics = generate_topics(df['cleaned_text'])

    keywords = extract_keywords(df['cleaned_text'])

    negative_percent = (
        len(df[df['sentiment'] == "Negative"])
        / len(df)
    ) * 100

    complaint_percent = (
        len(df[df['complaint'] == "Complaint"])
        / len(df)
    ) * 100

    insight = generate_insight(
        negative_percent,
        complaint_percent
    )

    return {
        "dataframe": df,
        "topics": topics,
        "keywords": keywords,
        "insight": insight,
        "negative_percent": negative_percent,
        "complaint_percent": complaint_percent
    }
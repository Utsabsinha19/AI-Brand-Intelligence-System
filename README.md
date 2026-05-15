# AI Consumer Intelligence & Sentiment Analytics Platform

An AI-powered analytics platform that transforms raw consumer feedback into actionable business intelligence using Natural Language Processing (NLP), sentiment analysis, topic modelling, and complaint detection.

This system helps brands, startups, and product teams understand how customers feel about products, services, and experiences by automatically analyzing reviews, social-style posts, and feedback datasets.

---

# Project Overview

Modern businesses receive thousands of customer opinions every day through:

- product reviews
- customer feedback
- surveys
- complaint logs
- social media discussions
- community forums

Manually analyzing this data is difficult, time-consuming, and inefficient.

This project solves that problem by building an intelligent NLP-driven analytics engine capable of automatically extracting:

- customer sentiment
- recurring complaints
- trending discussion topics
- keyword insights
- business recommendations

The platform converts unstructured text into structured business intelligence through a clean interactive dashboard.

---

# Key Features

## Sentiment Analysis
Detects whether customer feedback is:

- Positive
- Negative
- Neutral

Using:
- VADER Sentiment Analysis
- TextBlob NLP

---

## Complaint Detection
Automatically identifies complaints and critical customer issues such as:

- delayed delivery
- refund problems
- poor customer support
- damaged products
- service failures

This enables early issue detection before escalation.

---

## Topic Modelling (LDA)
Uses Latent Dirichlet Allocation (LDA) to discover hidden discussion themes within customer conversations.

Example detected topics:
- battery issues
- delivery experience
- pricing
- product quality
- customer support

---

## Keyword Extraction
Extracts high-frequency and high-impact keywords using TF-IDF vectorization to identify emerging customer trends.

---

## AI Business Insights
Generates automated business-level recommendations based on analyzed consumer sentiment and complaint patterns.

Example:
> “Consumers are increasingly frustrated with delivery delays and customer support response times.”

---

## Interactive Dashboard
Built with Streamlit and Plotly for real-time visualization of:

- sentiment distribution
- detected topics
- complaint percentage
- keyword trends
- processed datasets
- AI-generated insights

---

# Tech Stack

## Programming
- Python

## NLP & Machine Learning
- NLTK
- VADER
- TextBlob
- Scikit-learn
- Gensim

## Data Processing
- Pandas
- NumPy

## Visualization
- Plotly
- Streamlit
- Matplotlib

---

# System Architecture

```text
User Input / Dataset Upload
            ↓
      Text Preprocessing
            ↓
      NLP Intelligence Layer
   ├── Sentiment Analysis
   ├── Complaint Detection
   ├── Topic Modelling
   ├── Keyword Extraction
            ↓
     AI Insight Generation
            ↓
      Analytics Dashboard

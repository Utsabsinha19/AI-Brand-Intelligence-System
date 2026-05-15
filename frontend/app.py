import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import datetime

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from backend.main_pipeline import run_pipeline

def generate_pdf_report(results):
    pdf = FPDF()
    pdf.add_page()
    
    # Title and Timestamp
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "AI Brand Intelligence Report", ln=True, align='C')
    pdf.set_font("Arial", '', 10)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Generated on: {now}", ln=True, align='C')
    pdf.ln(10)
    
    # AI Insight
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "AI Business Insight:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, results['insight'])
    pdf.ln(5)
    
    # Metrics
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Key Metrics:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"- Complaint Percentage: {results['complaint_percent']:.2f}%", ln=True)
    pdf.cell(0, 10, f"- Negative Sentiment: {results['negative_percent']:.2f}%", ln=True)
    pdf.cell(0, 10, f"- Total Records Analyzed: {len(results['dataframe'])}", ln=True)
    pdf.ln(5)
    
    # Keywords
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Top Keywords:", ln=True)
    pdf.set_font("Arial", '', 12)
    keywords_str = ", ".join(results['keywords'])
    pdf.multi_cell(0, 10, keywords_str)
    
    # Save to temp file and read bytes
    pdf.output("temp_report.pdf")
    with open("temp_report.pdf", "rb") as f:
        pdf_bytes = f.read()
    return pdf_bytes

if 'results' not in st.session_state:
    st.session_state['results'] = None

st.set_page_config(
    page_title="AI Brand Intelligence",
    layout="wide"
)

st.title("AI Consumer Intelligence Dashboard")

st.markdown("""
### About This Project
The AI Brand Intelligence System processes consumer feedback, reviews, and comments to provide actionable business insights. 
Leveraging Natural Language Processing (NLP), this tool automatically helps you:
- 📊 **Analyze Sentiment:** Understand the overall mood of your customers.
- 🚨 **Detect Complaints:** Quickly flag critical customer service issues.
- 🔑 **Extract Keywords & Topics:** Discover the main subjects your customers are discussing.
- 💡 **Generate AI Insights:** Get automatic, high-level business recommendations based on the data.
""")

st.subheader("Input Consumer Data")

option = st.radio(
    "Choose Input Method",
    ["Upload CSV", "Paste Text"]
)

# =========================
# CSV Upload
# =========================

if option == "Upload CSV":

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file:

        if st.button("Analyze CSV"):
            with open("temp.csv", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.session_state['results'] = run_pipeline("temp.csv")

# =========================
# Manual Text Input
# =========================

elif option == "Paste Text":

    st.info(
        "Enter one customer review/comment per line."
    )

    user_text = st.text_area(
        "",
        height=300,
        placeholder="Type or paste customer feedback here..."
    )

    if st.button("Analyze Text"):

        if user_text.strip() != "":

            lines = user_text.split("\n")

            posts = [
                line.strip()
                for line in lines
                if line.strip() != ""
            ]

            import pandas as pd

            df = pd.DataFrame({
                "text": posts
            })

            df.to_csv("temp_manual.csv", index=False)

            st.session_state['results'] = run_pipeline("temp_manual.csv")

if st.session_state['results'] is not None:

    results = st.session_state['results']
    df = results['dataframe']

    st.subheader("Processed Data")

    st.dataframe(df)

    # =========================
    # Sentiment Chart
    # =========================

    st.subheader("Sentiment Distribution")

    sentiment_counts = df['sentiment'].value_counts()

    fig = px.pie(
        values=sentiment_counts.values,
        names=sentiment_counts.index,
        title="Sentiment Analysis"
    )

    st.plotly_chart(fig)

    # =========================
    # Topics
    # =========================

    st.subheader("Detected Topics")

    for topic in results['topics']:
        st.write(topic)

    # =========================
    # Keywords
    # =========================

    st.subheader("Top Keywords")

    st.write(results['keywords'])

    keywords_text = "\n".join(results['keywords'])
    st.download_button(
        label="Download Keywords as TXT",
        data=keywords_text,
        file_name="extracted_keywords.txt",
        mime="text/plain"
    )

    # =========================
    # AI Insight
    # =========================

    st.subheader("AI Business Insight")

    st.success(results['insight'])

    # =========================
    # Metrics
    # =========================

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Complaint %",
            f"{results['complaint_percent']:.2f}%"
        )

    with col2:
        st.metric(
            "Negative Sentiment %",
            f"{results['negative_percent']:.2f}%"
        )

    # =========================
    # Export & Actions
    # =========================

    st.markdown("---")
    st.subheader("Export & Actions")
    
    col_x, col_y, col_z = st.columns(3)
    
    with col_x:
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Processed CSV",
            data=csv_data,
            file_name="processed_insights.csv",
            mime="text/csv"
        )
        
    with col_y:
        pdf_report = generate_pdf_report(results)
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_report,
            file_name="brand_intelligence_report.pdf",
            mime="application/pdf"
        )
        
    with col_z:
        if st.button("🗑️ Clear Data"):
            st.session_state['results'] = None
            st.rerun()
# AI Sales Call Assistant For Enhanced conversational Strategies

## Overview
The Voice-Powered Sales Call Assistant is an AI-driven tool designed to enhance sales call interactions by providing real-time transcription, sentiment analysis, product recommendations, and objection handling. It leverages state-of-the-art machine learning and natural language processing techniques to assist sales representatives in improving their performance and customer engagement.

---

## Features

1. **Real-Time Speech Transcription**:
   - Utilizes the Vosk model for accurate and efficient speech-to-text conversion.
   - Enables hands-free transcription of live conversations.

2. **Sentiment Analysis**:
   - Analyzes customer sentiment in real-time using a Hugging Face model (`tabularisai/multilingual-sentiment-analysis`).
   - Categorizes sentiment into five levels: VERY NEGATIVE, NEGATIVE, NEUTRAL, POSITIVE, VERY POSITIVE.

3. **Objection Handling**:
   - Detects and responds to customer objections using an objection-response database.
   - Embedding-based search powered by Sentence Transformers and FAISS for intelligent objection handling.

4. **Product Recommendations**:
   - Suggests relevant products based on live conversation context.
   - Embedding-based recommendation system trained on product descriptions and titles.

5. **Google Sheets Integration**:
   - Stores transcription, sentiment analysis, and summary data in Google Sheets for easy access and reporting.

---

## Technology Stack

1. **Speech Recognition**:
   - **Vosk**: Real-time, offline speech-to-text conversion.
   - **PyAudio**: Captures live audio input.

2. **Natural Language Processing (NLP)**:
   - **Hugging Face Transformers**: For sentiment analysis.
   - **Sentence Transformers**: Embedding generation for recommendations and objection handling.

3. **Search and Retrieval**:
   - **FAISS**: Efficient vector similarity search for objections and recommendations.

4. **Data Storage**:
   - **Google Sheets API**: For storing and accessing transcription and analysis results.

5. **Data Formats**:
   - CSV files for product and objection data.

---

## System Architecture

1. **Voice Input**:
   - Captured using PyAudio and transcribed using the Vosk model.

2. **Preprocessing**:
   - Transcribed text is analyzed for sentiment using Hugging Face's sentiment analysis pipeline.

3. **Objection Handling**:
   - Objections detected in the conversation are matched to responses using FAISS and Sentence Transformers.

4. **Product Recommendations**:
   - User queries are matched to product data embeddings for relevant recommendations.

5. **Data Integration**:
   - Final outputs, including transcriptions, sentiment scores, and summaries, are stored in Google Sheets.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root and define the following:
     ```env
     huggingface_api_key=your_huggingface_api_key
     vosk_model_path=path_to_vosk_model
     google_sheet_id=your_google_sheet_id
     ```

4. **Download Models**:
   - **Vosk Model**: Download `vosk-model-en-in-0.5` from [Vosk Models](https://alphacephei.com/vosk/models).
   - **Sentence Transformers**: Preloaded in the code (`all-MiniLM-L6-v2`).

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

6. **Prepare Data**:
   - Place the following CSV files in the project directory:
     - `Sales_Calls_Transcriptions_Sheet2.csv`: Product data (columns: `product_title`, `product_description`).
     - `Sales_Calls_Transcriptions_Sheet3.csv`: Objection data (columns: `Customer Objection`, `Salesperson Response`).

---

## Usage

1. **Start Transcription**:
   - Run the application and say "start listening" to begin transcription.
   - Speak naturally, and the system will process your input in chunks.

2. **Objection Handling**:
   - The system detects objections in real-time and provides relevant responses.

3. **Product Recommendations**:
   - Suggestions are generated based on the conversation context.

4. **View Results**:
   - Transcriptions, sentiment analysis, and recommendations are displayed in the console.
   - Data is stored in Google Sheets for further analysis.

---

## Future Enhancements

1. Expand product and objection datasets for broader applicability.
2. Integrate with CRM systems for seamless sales tracking.
3. Add multilingual support for non-English sales calls.
4. Develop a web-based dashboard for real-time monitoring and analytics.
5. Enable advanced filtering and search in Google Sheets for better reporting.

---


## Acknowledgments
- **Vosk** for speech-to-text capabilities.
- **Hugging Face** for NLP models and pipelines.
- **FAISS** for vector search and retrieval.
- **Google Sheets API** for data storage and integration.


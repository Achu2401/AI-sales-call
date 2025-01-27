#AI Sales Call Assistant
This project implements a real-time product recommendation system using Streamlit, integrating voice input processed by the Vosk model, and embedding generation through the LLaMA model. The system uses FAISS for vectorization and RAG (Retrieval-Augmented Generation) for dynamic product recommendations based on real-time user queries.


#Features

##Voice Input: Uses the Vosk speech recognition model to accept voice commands from users.
##Product Recommendations: Recommends products based on user queries and stored product data.
##Real-Time Responses: Utilizes FAISS and LLaMA for fast, accurate vector-based product recommendations.
##Modular Design: The code is structured for maintainability and easy refactoring.


#Technologies Used

##Streamlit: For creating the interactive web app.
##Vosk: For speech-to-text conversion.
##LLaMA 3.2: Used for embedding generation in product recommendations.
##FAISS: For vectorization of product data.
##RAG: To integrate product data dynamically for enhanced recommendation accuracy.
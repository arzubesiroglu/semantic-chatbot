# rag_semantic_app.py

import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# ---------- 1. Setup: Load Dataset and Embed ----------
@st.cache_resource
def load_data_and_index():
    df = pd.read_excel("Mentoring_data.xlsx")
    questions = df["Questions"].tolist()

    model_embed = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    embeddings = model_embed.encode(questions)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return df, questions, index, model_embed

# ---------- 2. Streamlit UI ----------
st.set_page_config(page_title="Semantic Chatbot", layout="wide")
st.title("💬 Bootcamp Yardımcı Chatbot")
st.markdown("Veri analizi ve veri bilimi hakkında en alakalı cevabı getirir. LLM yoktur, doğrudan bilgi döndürür.")

query = st.text_input("📌 Sorunuzu girin:", placeholder="Örnek: Veri bilimi nedir?")

if query:
    with st.spinner("En iyi eşleşme aranıyor..."):
        df, questions, index, embedder = load_data_and_index()

        query_vec = embedder.encode([query])
        _, indices = index.search(np.array(query_vec), 1)

        matched_index = indices[0][0]
        matched_q = questions[matched_index]
        matched_a = df["Answer"].iloc[matched_index]

        st.markdown("---")
        st.subheader("🧠 En Yakın Soru")
        st.write(matched_q)

        st.subheader("📘 Cevap")
        st.write(matched_a)


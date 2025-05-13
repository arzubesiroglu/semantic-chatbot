# Semantic Chatbot

https://semantic-chatbot.streamlit.app/

Bu proje, bootcamp platformlarında kullanıcıların veri bilimi, veri analizi ve yapay zeka konularında en çok merak ettiği sorulara anlamlı ve hızlı yanıt vermek için geliştirilmiştir.


## 🧰 Kullanılan Teknolojiler

| Bileşen                | Açıklama                                      |
| ---------------------- | --------------------------------------------- |
| `Streamlit`            | Uygulamanın web arayüzü için                  |
| `Pandas`               | Excel tabanlı veriyi okuma ve işleme          |
| `SentenceTransformers` | Cümleleri vektörleştirme (Semantic Embedding) |
| `FAISS`                | Anlamsal benzerlik arama motoru               |
| `GitHub`               | Uygulama kod ve veri barındırma               |
| `Streamlit Cloud`      | Ücretsiz ve interaktif deploy ortamı          |

## 🔍 Özellikler

- ❌ LLM kullanmaz — tamamen maliyetsizdir
- ✅ FAISS ile semantik eşleşme yapar
- ✅ Sentence-BERT tabanlı embedding modeli kullanır
- ✅ Excel dosyasından gelen verileri tarar
- ✅ Streamlit Cloud ile web üzerinden erişilebilir

## 🚀 Kullanım

### 1. Gerekli dosyalar

- `rag_semantic_app.py`: Streamlit uygulaması
- `Mentoring_data.xlsx`: Soru-Cevap veri seti
- `requirements.txt`: Kurulması gereken kütüphaneler

### 2. Çalıştırmak için

```bash
pip install -r requirements.txt
streamlit run rag_semantic_app.py

Excel Verisi ➝ Sentence-BERT ➝ FAISS ➝ En yakın soru ➝ Cevap




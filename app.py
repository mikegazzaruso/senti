import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
import numpy as np
from utils import analyze_sentiment, detect_language, transcribe_audio
import os
import wave
import tempfile

# Configurazione della pagina
st.set_page_config(
    page_title="Analisi del Sentimento Multilingua",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Applicazione del tema scuro
st.markdown("""
    <style>
        .stTextInput > label {
            font-size: 20px;
        }
        .stTextArea > label {
            font-size: 20px;
        }
        .sentiment-result {
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .positive {
            background-color: rgba(0, 255, 0, 0.1);
        }
        .negative {
            background-color: rgba(255, 0, 0, 0.1);
        }
        .neutral {
            background-color: rgba(128, 128, 128, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Titolo dell'app
st.title("🌈 SENTI")
st.markdown("**SENTI**: Sentiment Evaluation and Natural Text Interpretation")
st.markdown("---")

# Selezione della funzionalità
option = st.radio("Scegli un'opzione:", ("Analizza Testo", "Analizza Audio"))

if option == "Analizza Testo":
    # Area di input per testo
    text_input = st.text_area(
        "Inserisci il testo da analizzare (supporta più lingue)",
        height=150,
        placeholder="Scrivi qui il tuo testo..."
    )

    # Pulsante di analisi per testo
    if st.button("Analizza Sentimento", type="primary"):
        if text_input.strip():
            detected_lang = detect_language(text_input)
            sentiment, polarity, subjectivity = analyze_sentiment(text_input)
            
            sentiment_class = "positive" if sentiment in ["Positivo", "Positive"] else "negative" if sentiment in ["Negativo", "Negative"] else "neutral"
            
            st.markdown(f"""
                <div class="sentiment-result {sentiment_class}">
                    <h3>Risultati dell'Analisi</h3>
                    <p><strong>Lingua rilevata:</strong> {detected_lang.upper()}</p>
                    <p><strong>Sentimento:</strong> {sentiment}</p>
                    <p><strong>Polarità:</strong> {polarity:.2f}</p>
                    <p><strong>Soggettività:</strong> {subjectivity:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("📖 Spiegazione dei risultati"):
                st.markdown("""
                    - **Lingua rilevata**: La lingua del testo inserito
                    - **Polarità**: varia da -1 (molto negativo) a +1 (molto positivo)
                    - **Soggettività**: varia da 0 (oggettivo) a 1 (soggettivo)
                """)
        else:
            st.error("Per favore, inserisci del testo da analizzare.")

elif option == "Analizza Audio":
    # Sezione per l'analisi del file audio
    st.markdown("---")
    st.header("📥 Analisi del Sentimento da File Audio")

    # Aggiungi .m4a ai formati supportati
    audio_file = st.file_uploader("Carica un file audio (formati supportati: WAV, MP3, M4A)", type=["wav", "mp3", "m4a"])

    if audio_file is not None:
        # Salva il file audio temporaneamente
        with open("temp_audio", "wb") as f:
            f.write(audio_file.getbuffer())
        
        # Trascrivi l'audio
        transcribed_text = transcribe_audio("temp_audio")
        st.write("Testo trascritto dall'audio:")
        st.write(transcribed_text)
        
        # Analizza il sentimento del testo trascritto
        if transcribed_text:
            detected_lang = detect_language(transcribed_text)
            sentiment, polarity, subjectivity = analyze_sentiment(transcribed_text)
            
            sentiment_class = "positive" if sentiment in ["Positivo", "Positive"] else "negative" if sentiment in ["Negativo", "Negative"] else "neutral"
            
            st.markdown(f"""
                <div class="sentiment-result {sentiment_class}">
                    <h3>Risultati dell'Analisi</h3>
                    <p><strong>Lingua rilevata:</strong> {detected_lang.upper()}</p>
                    <p><strong>Sentimento:</strong> {sentiment}</p>
                    <p><strong>Polarità:</strong> {polarity:.2f}</p>
                    <p><strong>Soggettività:</strong> {subjectivity:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("📖 Spiegazione dei risultati"):
                st.markdown("""
                    - **Lingua rilevata**: La lingua del testo trascritto
                    - **Polarità**: varia da -1 (molto negativo) a +1 (molto positivo)
                    - **Soggettività**: varia da 0 (oggettivo) a 1 (soggettivo)
                """)

# Footer
st.markdown("---")
st.markdown("(C) 2024 Mike Gazzaruso")
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import nltk
from langdetect import detect, DetectorFactory
from typing import Tuple
import speech_recognition as sr
from pydub import AudioSegment

# Imposta il seme per la riproducibilità
DetectorFactory.seed = 0

# Download necessario per NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def detect_language(text: str) -> str:
    """
    Rileva la lingua del testo.
    """
    try:
        return detect(text)
    except Exception as e:
        print(f"Errore nel rilevamento della lingua: {e}")
        return 'en'  # Default a inglese se la detection fallisce

def translate_to_english(text: str, source_lang: str) -> str:
    """
    Traduce il testo in inglese se necessario.
    """
    if source_lang != 'en':
        try:
            translator = GoogleTranslator(source=source_lang, target='en')
            return translator.translate(text)
        except Exception as e:
            print(f"Errore nella traduzione: {e}")
            return text  # Restituisci il testo originale in caso di errore
    return text

def analyze_sentiment(text: str) -> Tuple[str, float, float]:
    """
    Analizza il sentimento del testo in qualsiasi lingua.
    Prima traduce in inglese se necessario, poi usa VADER per l'analisi.
    
    Args:
        text (str): Il testo da analizzare
        
    Returns:
        tuple: (sentiment_label, polarity, subjectivity)
    """
    # Rileva la lingua
    source_lang = detect_language(text)
    
    # Traduci in inglese se necessario
    text_for_analysis = translate_to_english(text, source_lang)
    
    # Usa VADER per l'analisi
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text_for_analysis)
    
    polarity = scores['compound']
    subjectivity = (scores['pos'] + scores['neg']) / 2
    
    # Determina il sentimento
    if polarity >= 0.05:
        sentiment = "Positivo" if source_lang == 'it' else "Positive"
    elif polarity <= -0.05:
        sentiment = "Negativo" if source_lang == 'it' else "Negative"
    else:
        sentiment = "Neutro" if source_lang == 'it' else "Neutral"
    
    return sentiment, polarity, subjectivity

def transcribe_audio(file_path: str) -> str:
    """
    Trascrive un file audio in testo.
    
    Args:
        file_path (str): Il percorso del file audio da trascrivere.
        
    Returns:
        str: Il testo trascritto.
    """
    recognizer = sr.Recognizer()
    
    # Carica il file audio
    audio = AudioSegment.from_file(file_path)  # Supporta WAV, MP3, M4A
    
    # Salva il file audio in formato WAV temporaneamente
    wav_file_path = "temp_audio.wav"
    audio.export(wav_file_path, format="wav")
    
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)  # Leggi il file audio
        try:
            # Riconoscimento vocale
            text = recognizer.recognize_google(audio_data, language='it-IT')  # Cambia la lingua se necessario
            return text
        except sr.UnknownValueError:
            return "Non sono riuscito a capire l'audio."
        except sr.RequestError as e:
            return f"Errore nel servizio di riconoscimento vocale: {e}"
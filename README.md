# SENTI - Sentiment Evaluation and Natural Text Interpretation

🌈 **SENTI** is a multilingual sentiment analysis tool that allows users to analyze text and audio files for sentiment evaluation. This application has been created entirely with the assistance of AI, using Cursor AI.

## License

This project is protected under the GNU General Public License v3.0 (GPL-3.0). You can freely use, modify, and distribute this software, provided that all copies include this license.

## App Flow

1. **Choose Functionality**: Users can select between analyzing text or audio.
2. **Text Analysis**:
   - Users can input text in various languages.
   - Upon clicking "Analyze Sentiment," the app detects the language, analyzes the sentiment, and displays the results, including sentiment classification, polarity, and subjectivity.
3. **Audio Analysis**:
   - Users can upload audio files in WAV, MP3, or M4A formats.
   - The app transcribes the audio to text and then analyzes the sentiment of the transcribed text, displaying the results similarly to text analysis.
4. **Results Display**: The app provides a clear and user-friendly display of the analysis results, including explanations of the sentiment metrics.

## Technologies Used

- **Language**: Python
- **Framework**: Streamlit
- **Libraries**:
  - `textblob`: For language detection and sentiment analysis.
  - `vaderSentiment`: For sentiment analysis of English text.
  - `deep-translator`: For translating text to English.
  - `langdetect`: For detecting the language of the input text.
  - `SpeechRecognition`: For transcribing audio files to text.
  - `pydub`: For handling audio file formats and conversions.
  - `streamlit-webrtc`: For handling audio streaming and recording.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Acknowledgments

This tool has been developed with the help of AI technologies, specifically using Cursor AI, which has significantly streamlined the development process.

For any questions or contributions, feel free to reach out!
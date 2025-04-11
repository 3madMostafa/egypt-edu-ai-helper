from gtts import gTTS
from io import BytesIO
from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return "ar" if lang.startswith("ar") else "en"
    except Exception:
        return "ar"  # default fallback

def get_tts_audio(text):
    detected_lang = detect_language(text)
    try:
        tts = gTTS(text, lang=detected_lang)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        return None

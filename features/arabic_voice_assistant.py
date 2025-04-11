import streamlit as st
from file_utils import process_uploaded_file
from llm_utils import call_llm
from audio_utils import get_tts_audio, detect_language

def arabic_voice_assistant(language):
    st.subheader("🗣️ المساعد الصوتي")
    input_method = st.radio("اختر طريقة الإدخال", ("رفع ملف نصي", "كتابة النص يدويًا"))
    content = ""
    if input_method == "رفع ملف نصي":
        uploaded_file = st.file_uploader("ارفع ملف (PDF, TXT, صورة)", type=["pdf", "txt", "jpg", "jpeg", "png"])
        if uploaded_file is not None:
            content = process_uploaded_file(uploaded_file)
    else:
        content = st.text_area("اكتب النص هنا", height=300)
    if content.strip():
        detected_lang = detect_language(content)
        lang_name = "العربية" if detected_lang == "ar" else "الإنجليزية"
        st.success(f"✅ تم التعرف على اللغة: {lang_name}")
        # Use Gemini to enhance the text before converting to speech
        if detected_lang == "ar":
            enhancement_prompt = f"قم بإعادة صياغة وتحسين النص التالي ليكون أكثر وضوحاً وفهماً:\n\n{content}"
        else:
            enhancement_prompt = f"Please rephrase and improve the following text to make it clearer and more understandable:\n\n{content}"
        enhanced_text = call_llm(enhancement_prompt)
        st.markdown("### النص المحسن")
        st.write(enhanced_text)
        audio = get_tts_audio(enhanced_text)
        st.audio(audio, format="audio/mp3")
    else:
        st.info("يرجى إدخال نص أو رفع ملف.")

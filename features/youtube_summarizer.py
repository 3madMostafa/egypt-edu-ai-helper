import streamlit as st
from llm_utils import call_llm
from audio_utils import detect_language
from youtube_utils import extract_youtube_transcript

def youtube_summarizer(language):
    st.subheader("🎥 مولّد ملخص الفيديو من YouTube")
    video_url = st.text_input("أدخل رابط فيديو YouTube")
    if st.button("تلخيص الفيديو"):
        if video_url:
            transcript = extract_youtube_transcript(video_url)
            detected_lang = detect_language(transcript)
            language_str = "العربية" if detected_lang == "ar" else "الإنجليزية"
            prompt = (f"النص التالي هو تفريغ فيديو تعليمي. قم بتوليد ملخص شامل له باللغة {language_str}، دون عرض النص الأصلي:\n\n" 
                      + transcript)
            summary = call_llm(prompt)
            st.markdown("### الملخص")
            st.write(summary)
        else:
            st.warning("الرجاء إدخال رابط الفيديو.")

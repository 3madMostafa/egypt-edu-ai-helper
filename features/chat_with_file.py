import streamlit as st
from file_utils import process_uploaded_file
from llm_utils import call_llm
from audio_utils import detect_language

def chat_with_file(language):
    st.subheader("📄 دردشة مع الملف")
    uploaded_file = st.file_uploader("ارفع ملف (PDF, TXT, صورة)", type=["pdf", "txt", "jpg", "jpeg", "png"])
    if uploaded_file is not None:
        content = process_uploaded_file(uploaded_file)
        if content.strip() == "":
            st.error("لم يتم استخراج أي نص من الملف.")
            return
        detected_lang = detect_language(content)
        language_str = "العربية" if detected_lang == "ar" else "الإنجليزية"
        summary_prompt = f"الوثيقة التالية تحتوي على معلومات، لخص النص بشكل موجز باللغة {language_str}:\n\n{content}"
        summary = call_llm(summary_prompt)
        st.markdown("### الملخص")
        st.write(summary)
        question = st.text_input("اطرح سؤالك عن الملف")
        if st.button("إرسال السؤال"):
            if question:
                prompt = f"الوثيقة:\n{content}\n\nالسؤال: {question}\nالرجاء تقديم إجابة باللغة {language_str}."
                answer = call_llm(prompt)
                st.markdown("### الإجابة")
                st.write(answer)
            else:
                st.warning("الرجاء إدخال سؤال.")

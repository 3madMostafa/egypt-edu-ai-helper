import streamlit as st
import re
from llm_utils import call_llm
from audio_utils import detect_language

def flashcard_generator(language):
    st.subheader("🗂️ مولّد البطاقات التعليمية")
    input_method = st.radio("اختر طريقة الإدخال", ("رفع ملف", "نسخ ولصق النص"), key="flashcard_input")
    content = ""
    if input_method == "رفع ملف":
        uploaded_file = st.file_uploader("ارفع ملف (PDF, TXT, صورة)", type=["pdf", "txt", "jpg", "jpeg", "png"], key="flashcard_file")
        if uploaded_file is not None:
            from file_utils import process_uploaded_file  # local import
            content = process_uploaded_file(uploaded_file)
    else:
        content = st.text_area("أدخل النص", height=300, key="flashcard_text")
    
    if content:
        detected_lang = detect_language(content)
        language_str = "العربية" if detected_lang == "ar" else "الإنجليزية"
        prompt = (f"من النص التالي، أنشئ مجموعة من البطاقات التعليمية على هيئة سؤال-جواب. "
                  f"يجب أن يكون كل سؤال وإجابته باللغة {language_str} وبصيغة موجزة:\n\n{content}\n\n"
                  "يرجى إخراج البطاقات في الشكل التالي:\n"
                  "البطاقة 1:\n"
                  "السؤال: ...\n"
                  "الإجابة: ...\n\n"
                  "البطاقة 2: ...")
        flashcards = call_llm(prompt)
        st.markdown("### البطاقات التعليمية")
        cards = re.split(r"(?:^|\n)(?=البطاقة\s*\d+[:：])", flashcards)
        for i, card in enumerate(cards):
            card = card.strip()
            if card:
                with st.expander(f"📘 بطاقة {i + 1}"):
                    lines = card.split("\n")
                    for line in lines:
                        line = line.strip()
                        if line.startswith("السؤال"):
                            st.markdown(f"**🟠 {line}**")
                        elif line.startswith("الإجابة"):
                            st.markdown(f"✅ {line}")
                        else:
                            st.write(line)

import streamlit as st
import re
from file_utils import process_uploaded_file
from llm_utils import call_llm
from audio_utils import detect_language

def quiz_generator(language):
    st.subheader("🧠 مولّد الاختبارات")
    input_method = st.radio("اختر طريقة الإدخال", ("رفع ملف", "نسخ ولصق النص"))
    content = ""
    if input_method == "رفع ملف":
        uploaded_file = st.file_uploader("ارفع ملف (PDF, TXT, صورة)", type=["pdf", "txt", "jpg", "jpeg", "png"], key="quiz_file")
        if uploaded_file is not None:
            content = process_uploaded_file(uploaded_file)
    else:
        content = st.text_area("أدخل النص", height=300)
    
    if content:
        st.markdown("### معاينة المحتوى")
        st.write(content[:500] + "..." if len(content) > 500 else content)
        if st.button("توليد الاختبار"):
            detected_lang = detect_language(content)
            language_str = "العربية" if detected_lang == "ar" else "الإنجليزية"
            prompt = (f"أنشئ اختباراً متعدد الخيارات (MCQs) باللغة {language_str} قائم على المحتوى التالي. "
                      "يجب أن يحتوي كل سؤال على أربع إجابات مع تحديد الإجابة الصحيحة أسفل كل سؤال.\n\n" + content)
            quiz_text = call_llm(prompt)
            st.markdown("### نتيجة الاختبار")
            quiz_blocks = quiz_text.strip().split("\n\n")
            for block in quiz_blocks:
                lines = block.strip().split("\n")
                if not lines:
                    continue
                st.markdown("---")
                for line in lines:
                    if line.startswith("السؤال") or line.startswith("س:") or "؟" in line:
                        st.markdown(f"**🟠 {line.strip()}**")
                    elif "الإجابة" in line:
                        st.markdown(f"✅ **{line.strip()}**")
                    elif re.match(r"^[أ-د]\)", line.strip()):
                        st.markdown(f"- {line.strip()}")
                    else:
                        st.write(line.strip())

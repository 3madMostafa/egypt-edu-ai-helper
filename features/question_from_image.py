import streamlit as st
import pytesseract
from PIL import Image
from llm_utils import call_llm
from audio_utils import detect_language

def question_from_image(language):
    st.subheader("🖼️ اسأل عن محتوى صورة")
    image_file = st.file_uploader("ارفع صورة (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="الصورة المرفوعة", use_column_width=True)
        extracted_text = pytesseract.image_to_string(image, lang="ara+eng")
        if extracted_text.strip():
            st.markdown("### النص المستخرج (تحضير للإجابة فقط)")
            st.write(extracted_text)
            user_question = st.text_input("❓ اسأل أي سؤال عن محتوى الصورة")
            if st.button("إرسال السؤال"):
                detected_lang = detect_language(extracted_text)
                language_str = "العربية" if detected_lang == "ar" else "الإنجليزية"
                prompt = (f"الصورة تحتوي على النص التالي:\n\n{extracted_text}\n\n"
                          f"السؤال: {user_question}\nالرجاء الإجابة باللغة {language_str}.")
                answer = call_llm(prompt)
                st.markdown("### الإجابة")
                st.write(answer)
        else:
            st.warning("⚠️ لم يتم استخراج نص من الصورة.")

import streamlit as st
from llm_utils import call_llm, augment_prompt_with_chroma

def general_chat(language):
    st.subheader("💡 دردشة عامة (مدعومة بالمنهج)")
    user_query = st.text_input("اكتب سؤالك هنا")
    if st.button("إرسال"):
        if user_query:
            school_keywords = ["مدرسة", "ثانوي", "امتحان", "تعليم", "منهج", "صف"]
            if any(word in user_query for word in school_keywords):
                prompt = augment_prompt_with_chroma(user_query)
            else:
                prompt = user_query
            answer = call_llm(prompt)
            st.markdown("### الإجابة")
            st.write(answer)
        else:
            st.warning("الرجاء كتابة سؤال.")

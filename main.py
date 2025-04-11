import streamlit as st
from features.chat_with_file import chat_with_file
from features.quiz_generator import quiz_generator
from features.youtube_summarizer import youtube_summarizer
from features.general_chat import general_chat
from features.flashcard_generator import flashcard_generator
from features.arabic_voice_assistant import arabic_voice_assistant
from features.question_from_image import question_from_image

def main():
    st.title("المساعد التعليمي لطلبة الثانوية العامة المصرية (الثانوية العامة)")
    
    features = {
        "📄 دردشة مع الملف": chat_with_file,
        "🧠 مولّد الاختبارات": quiz_generator,
        "🎥 تلخيص فيديو YouTube": youtube_summarizer,
        "💡 دردشة عامة (مدعومة بالمنهج)": general_chat,
        "🗂️ مولّد البطاقات التعليمية": flashcard_generator,
        "🗣️ المساعد الصوتي": arabic_voice_assistant,
        "🖼️ سؤال من صورة": question_from_image
    }
    
    feature_choice = st.sidebar.radio("اختر الخاصية", list(features.keys()))
    language = st.sidebar.radio("اختر لغة الواجهة", ("Arabic", "English"))
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        "هذا التطبيق مصمم لمساعدة طلاب الثانوية العامة بالمحتوى التعليمي. "
        "يستخدم واجهة Gemini 1.5 Pro مع دعم ChromaDB للبيانات المنهجية."
    )
    
    selected_feature = features[feature_choice]
    selected_feature(language)

if __name__ == "__main__":
    main()

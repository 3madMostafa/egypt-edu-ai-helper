
# Egyptian High School Educational Assistant (Streamlit App)

This is a Streamlit-based educational assistant designed to help Egyptian high school students interact with learning content using AI-powered tools.

## 🔧 Features

1. **Chat with File**  
   Upload a file (PDF, TXT, or Image), and the assistant will extract its content, summarize it, and allow you to ask questions about it.

2. **Quiz Generator**  
   Generate multiple-choice questions (MCQs) based on the content you upload or write.

3. **YouTube Video Summarizer**  
   Paste a YouTube link (Arabic videos only), and the app will summarize the transcript using AI.  
   _Note: The video must have an Arabic transcript available._

4. **Curriculum-Aware General Chat**  
   Ask any general educational question and get a smart answer. If it's related to the curriculum, the assistant uses context stored in ChromaDB.

5. **Flashcard Generator**  
   Upload content and get short question-answer flashcards to study from.

6. **Voice Assistant**  
   Upload a file or enter a text — the assistant will rewrite it clearly (with Gemini AI) and read it aloud using TTS.

7. **Ask About Image**  
   Upload an image containing text and ask questions about its content.  
   _Note: In the online demo version, image file upload might be limited due to Streamlit’s file handling._

---

## 🧠 Powered by:

- **Gemini 1.5 Pro** (via Google Generative AI)
- **Streamlit** for UI
- **ChromaDB** for curriculum context
- **PyTesseract** for OCR
- **gTTS** for text-to-speech
- **LangDetect** for automatic language detection

---

## 📁 Project Structure (Recommended)

```
project/
│
├── main.py                 # Streamlit entry point
├── requirements.txt
├── README.md
│
├── features/               # Feature-based modules
│   ├── chat_with_file.py
│   ├── quiz_generator.py
│   ├── youtube_summarizer.py
│   ├── flashcard_generator.py
│   ├── general_chat.py
│   ├── voice_assistant.py
│   └── image_question.py
│
├── llm_utils.py            # Gemini setup + call_llm()
├── file_utils.py           # OCR, PDF/Image/Text processing
├── audio_utils.py          # gTTS helpers
└── youtube_utils.py        # YouTube transcript extraction
```

---

## ⚠️ Notes

- In the **Streamlit Community Cloud**, image file handling might not fully work due to limitations with PDF-to-image conversion or OCR processing.  
- YouTube summarization requires that the video has **Arabic subtitles or transcript**.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/educational-assistant.git
cd educational-assistant
pip install -r requirements.txt
streamlit run main.py
```

---

## 🙋‍♂️ Author

Built by Emad Mostafa to help students learn better using the power of AI.

import os
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions

# -------------------------------------------------------------------
# Gemini API setup
# -------------------------------------------------------------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyDtwKF1t3fcooCHNauZoMk35h5jAHHLKbs"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# -------------------------------------------------------------------
# ChromaDB setup for curriculum context retrieval
# -------------------------------------------------------------------
chromadb_client = chromadb.Client()
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection_names = [col.name for col in chromadb_client.list_collections()]
if "curriculum" in collection_names:
    collection = chromadb_client.get_collection("curriculum")
else:
    collection = chromadb_client.create_collection(name="curriculum", embedding_function=embedding_function)

def augment_prompt_with_chroma(prompt):
    results = collection.query(query_texts=[prompt], n_results=3)
    context = ""
    if results and results.get("documents") and results["documents"][0]:
        context = " ".join(results["documents"][0])
    augmented = prompt + "\n\nRelevant Context:\n" + context
    return augmented

def call_llm(prompt):
    augmented_prompt = augment_prompt_with_chroma(prompt)
    response = model.generate_content(augmented_prompt)
    return response.candidates[0].content.parts[0].text

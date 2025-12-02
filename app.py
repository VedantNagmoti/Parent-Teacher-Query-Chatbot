import streamlit as st
import google.generativeai as genai
import rag_engine as rag
import time
from streamlit_mic_recorder import speech_to_text
from gtts import gTTS
from io import BytesIO
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables. Please set it before running the application.")
else:
    pass

# ==========================================
# 1. CONFIGURATION & SETUP
# ==========================================
st.set_page_config(
    page_title="EduBot - School Assistant",
    page_icon="🎓",
    layout="centered"
)

genai.configure(api_key=API_KEY)

# Initialize Model
model = genai.GenerativeModel('gemini-2.0-flash')

# Updated System Prompt
SYSTEM_INSTRUCTIONS = """
You are "EduBot," a warm, empathetic, and professional school counselor assistant. 
Your goal is to help parents track their child's progress and understand school policies.

CORE BEHAVIORS:
1. **Multilingual:** ALWAYS reply in the same language the user is speaking.
2. **Be Warm:** If a student scored low, add a constructive remark.
3. **Strict Context:** Answer strictly using the provided Context.
"""

# ==========================================
# 2. SESSION STATE
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! I am EduBot. How can I help you today?"}
    ]

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# ==========================================
# 3. HELPER FUNCTIONS
# ==========================================
def extract_potential_student_names(query):
    known_students = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", 
                      "Ayaan", "Krishna", "Ishaan", "Diya", "Saanvi", "Ananya", "Aadhya", 
                      "Pari", "Kiara", "Myra", "Riya", "Anvi", "Fatima"]
    found_names = [name for name in known_students if name.lower() in query.lower()]
    return found_names[0] if found_names else None

def text_to_audio(text):
    """
    Converts text to audio bytes using Google TTS (Indian Accent).
    """
    sound_file = BytesIO()
    # 'en' with tld='co.in' gives a nice Indian English accent
    # You can change lang='hi' if you want pure Hindi
    tts = gTTS(text, lang='en', tld='co.in')
    tts.write_to_fp(sound_file)
    return sound_file

# ==========================================
# 4. UI LAYOUT
# ==========================================
st.title("🎓 EduBot: Parent Assistant")

# --- 🎤 VOICE INPUT ---
st.markdown("### 🎙️ Voice Input")
voice_text = speech_to_text(
    language='en-IN', 
    start_prompt="Click to Speak",
    stop_prompt="Stop Recording", 
    just_once=True,
    key='STT'
)

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # If there is saved audio for this message, play it
        if "audio" in message:
            st.audio(message["audio"], format="audio/mp3")

# ==========================================
# 5. CHAT LOGIC
# ==========================================
chat_input_text = st.chat_input("Ask about grades, syllabus, or fees...")

# Priority Logic
prompt = None
if voice_text:
    prompt = voice_text
elif chat_input_text:
    prompt = chat_input_text

if prompt:
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. RAG Retrieval
    context_pieces = []
    
    with st.spinner("Searching school records..."):
        # A. General Search
        general_info = rag.search_general_knowledge(prompt)
        if general_info:
            context_pieces.append(f"📚 SCHOOL KNOWLEDGE BASE:\n{general_info}")

        # B. Student Search (FIXED LOGIC)
        potential_name = extract_potential_student_names(prompt)
        if potential_name:
            student_record = rag.get_student_info(potential_name) # Pass Name Only
            
            if student_record and "SYSTEM_MESSAGE" in student_record:
                context_pieces.append(f"⚠️ SYSTEM ALERT: {student_record}")
            elif student_record:
                context_pieces.append(f"👤 STUDENT RECORD:\n{student_record}")

    # 3. Construct Final Prompt
    full_context = "\n\n".join(context_pieces)
    
    final_prompt = f"""
    {SYSTEM_INSTRUCTIONS}

    CONTEXT FOUND IN DATABASE:
    {full_context}

    USER QUERY:
    {prompt}
    """

    # 4. Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            response = st.session_state.chat_session.send_message(final_prompt)
            
            # Text Animation
            for chunk in response.text.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
            # --- 🔊 NEW: GENERATE AUDIO ---
            # We generate audio for the final response
            audio_data = text_to_audio(full_response)
            st.audio(audio_data, format="audio/mp3")
            
            # Save to history so it persists
            st.session_state.messages.append({
                "role": "assistant", 
                "content": full_response,
                "audio": audio_data # Store audio to replay if needed
            })
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
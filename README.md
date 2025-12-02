# 🧠 Parent-Teacher Query Chatbot (RAG + Gemini 2.0 Flash)

## 📘 Overview
The **Parent-Teacher Query Chatbot** is an intelligent communication assistant designed to bridge the gap between parents and teachers.  
Built using **Retrieval-Augmented Generation (RAG)** and powered by **Google’s Gemini 2.0 Flash** Large Language Model (LLM), the chatbot provides **instant, context-aware responses** to parent queries — reducing the workload on teachers and improving communication efficiency.

---

## 🚀 Key Features

- **🤖 Intelligent Query Handling** — Uses RAG to retrieve relevant academic and administrative data before generating accurate, context-aware answers.
- **💬 Natural Conversations** — Powered by Gemini 2.0 Flash for smooth, human-like communication.
- **📚 Centralized Knowledge Base** — All communication records, FAQs, schedules, and announcements are stored in **MongoDB**.
- **⚡ Fast and Efficient** — Reduces the need for repetitive manual responses by teachers, saving time and effort.
- **🔒 Secure Data Management** — Sensitive information about students and parents is securely handled using encrypted storage.
- **📈 Scalable Architecture** — Can easily integrate with school management systems or be deployed as a web or mobile chatbot.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Language Model** | Gemini 2.0 Flash |
| **Retrieval Framework** | RAG (Retrieval-Augmented Generation) |
| **Database** | MongoDB |
| **Backend** | Python |
| **Frontend** | Streamlit (for UI dashboard) |
| **Vector Store** | ChromaDB + MongoDB Atlas Vector Search |

---

## ⚙️ System Workflow

1. **Parent Query Input** — A parent sends a question (e.g., *“When is the next parent-teacher meeting?”*).
2. **RAG Pipeline**  
   - **Retriever:** Fetches relevant documents, schedules, or announcements from MongoDB.  
   - **Generator:** Gemini 2.0 Flash formulates a precise, human-like answer using retrieved context.
3. **Response Delivery** — The chatbot provides a clear and contextual response instantly.
4. **Logging & Feedback** — Each interaction is stored in MongoDB for tracking and improvement.

---

## 💡 Impact

- **⏱️ Saves Teachers’ Time:** Automates repetitive question handling like schedules, progress updates, and announcements.  
- **🤝 Enhances Communication:** Ensures parents receive consistent and prompt responses.  
- **📊 Data Insights:** Helps schools analyze common queries to identify communication gaps.  
- **🌐 Always Available:** 24/7 assistance without manual intervention.

---

## 🧰 Future Enhancements

- Integration with **School ERP Systems** for real-time student performance updates.  
- **Multilingual Support** for diverse parent communities.  
- **Voice-based Query Support** for accessibility.  
- **Role-based Access** for teachers, administrators, and parents.

---

## 👨‍🏫 Example Use Case

> **Parent:** “Can you tell me when the mid-term exams start?”  
> **Chatbot:** “The mid-term exams for Grade 8 will begin on *15th December 2025* as per the latest circular.”  

> **Parent:** “Who is the class teacher for my child, Aarav?”  
> **Chatbot:** “Aarav’s class teacher is *Mrs. Shreya Kulkarni* (Grade 8-B). You can reach her at *shreya.kulkarni@school.edu*.”

---



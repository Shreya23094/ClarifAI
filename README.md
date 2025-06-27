# 🤖 ClarifAI — Your Smart Explanation Assistant

ClarifAI is an AI-powered web application that helps users easily understand complex research papers, concepts, or technical content in a personalized explanation style and length. Whether you're a beginner, a tech enthusiast, or a coder, ClarifAI simplifies knowledge delivery — your way.
---

## ✨ Features:

- 📄 **Flexible Input Options**  
  Upload a PDF or type in your own content.

- 🎨 **Personalized Explanation Styles**  
  Choose from Beginner-Friendly, Technical, Code-Oriented, Mathematical, or write your own custom style.

- 📏 **Control the Length**  
  Get short, medium, or detailed answers — tailored to your needs.

- ⚡ **Powered by Hugging Face Transformers**  
  Uses `google/gemma-2-2b-it` LLM for fast, high-quality natural language understanding and generation.

---

## 🚀 Live Demo:

Try it out on Streamlit:  
👉 [clarif-ai.streamlit.app](https://clarif-ai.streamlit.app)

---

## 🛠️ Tech Stack:

| Tool             | Purpose                              |
|------------------|--------------------------------------|
| Streamlit        | Frontend UI                          |
| LangChain        | Prompt chaining and orchestration    |
| Hugging Face     | LLM inference (Gemma-2B)             |
| Python           | Core programming language            |
| Pydantic         | Structured data modeling (optional)  |
| dotenv + secrets | Environment and API key handling     |

---

## 📂 Project Structure:

```bash
clarifai/
├── app.py                  # Main Streamlit app
├── template.json           # Prompt template used in LangChain
├── requirements.txt        # Dependencies
└── .streamlit/
    └── config.toml         # (Optional) Streamlit theming config

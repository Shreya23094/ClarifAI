from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.set_page_config(page_title="ClarifAI", layout="centered")
st.header("ClarifAI")
st.text("Effortlessly understand complex topics in your preferred explanation style.")

# Input Method Selection
options = ['-- Select an option --', 'Upload a File', 'Type in the content']
paper_type = st.selectbox("Choose how you'd like to provide the content:", options)

paper_input = None
if paper_type == 'Upload a File':
    paper_upload = st.file_uploader("Upload a research paper or document (PDF or text).")
    if paper_upload is not None:
        try:
            paper_input = paper_upload.read().decode("utf-8")  # decode to str
        except:
            st.error("Unable to read file. Please upload a valid text-based file.")
    else:
        st.warning("Please upload a valid file.")

elif paper_type == 'Type in the content':
    paper_input = st.text_area("Enter the topic or content you'd like explained:")

else:
    st.info("Please select an input type to continue.")

# Style Selection
style_input = st.selectbox(
    "Select the explanation style:",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical", "Others"]
)
if style_input == "Others":
    style_input = st.text_input("Enter a custom explanation style:")

# Length Selection
length_input = st.selectbox(
    "Choose the desired explanation length:",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load Prompt Template
try:
    template = load_prompt("template.json")
except Exception as e:
    st.error(f"Error loading prompt template: {e}")
    st.stop()

# Generate Explanation
if st.button("Generate Explanation"):
    if paper_type != '-- Select an option --' and paper_input:
        with st.spinner("Generating explanation..."):
            chain = template | model
            result = chain.invoke({
                'paper_input': paper_input,
                'style_input': style_input,
                'length_input': length_input
            })
        st.success("Here’s your customized explanation:")
        st.write(result.content)
    else:
        st.warning("Please complete all required fields before generating the explanation.")

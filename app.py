import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(layout="wide")

st.title("AI Summarizer")

text = st.text_area("Введите статью здесь: ", height=250)

if st.button("Выжать суть!"):
    if not api_key:
        st.write("Ошибка: API ключ не найден.")
    else: 
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        Выдели 5 главных мыслей из этого текста списком:
        {text}
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
                )
            st.write("Краткое содержание: ")
            st.write(response.text)
        except Exception as e:
            st.write("Ошибка: ", e)
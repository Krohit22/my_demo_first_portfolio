import streamlit as st
from google import generativeai as genai
import os


genai.configure(api_key="AIzaSyDh5OuOcdweMVsaCQxcFAgjgWtCl6eOamk")
model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)
with col1:
    st.subheader("🕵️Hi")
    st.title("I am krishna rajpurohit")


with col2:
    st.image("image/p1.jpeg")

st.title("i am Krishna's Ai yoyo")
st.markdown("""  <style>
    .stButton>button {
        background-color: #675c6a;
        color: white;
        border:none;
        }
        
        .stButton>button:hover {
        background-color: #7b5d72;
        color:#c2c3c5;
        }
        """,unsafe_allow_html=True)
st.write("Ask me anything")
user_question = st.text_input("",placeholder="enter")
if st.button("ASK",use_container_width=400) :
    prompt = user_question
    response = model.generate_content(prompt)
    assert isinstance(response.text, object)
    st.text_area("",value=response.text, disabled=True)



col1,col2 = st.columns(2)

with col1:
    st.subheader("Recommend youtube channel for CV and AI")
    st.write("- youtube channel - Murtaza's Workshop - Robotics and AI")
    st.write("- 400k+ Subcriber")
    st.write("- over 150 free tuutorials")


with col2:
    video1 = "https://www.youtube.com/live/_2UqdX8dcsU?si=vOgJuf2iJCRptjtL"
    width1 = 500
    height1 = 300
    use_html = f"""<video width = {width1} height = {height1} controls> <source src="{video1}" type=video/mp4> </video>"""
    st.markdown(use_html,unsafe_allow_html=True)

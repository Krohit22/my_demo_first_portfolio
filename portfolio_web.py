import streamlit as st
import google.generativeai as genai
import os

os.environ.get('USER')
api="AIzaSyDh5OuOcdweMVsaCQxcFAgjgWtCl6eOamk"
genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)
with col1:
    st.subheader("🕵️Hi")
    st.title("i am Krishna's Ai yoyo")


with col2:
    st.image("image/p1.jpeg")


st.markdown("""  <style>
    body{
    background:#0C2340;
    }
    .stButton>button {
        background-color: #675c6a;
        color: white;
        border-radius:30px;
        border:none;
        }
        
        .stButton>button:hover {
        background-color: #7b5d72;
        color:#c2c3c5;
        }
        """,unsafe_allow_html=True)
st.write("Ask me anything")
persona = '''You are Krishna AI bot. You help people answer questions about your self (i.e Yoyo) Answer as if you are responding dont answer in second or third person. If you don't know they answer you simply say "That's a secret"  here is the more information about your creator and yourself:if user ask you about your name tell them that "your name is YOYO" and you are a AI and if they about your creator then tell them that "your creator name is Rajpurohit krishna and currently he studying in bca 3year".if some ask your about the thing such as violence,murder,killing a person,kidnapping and abduction then tell them i can't help you with that kind of illegal purpose but i think you are interested in this kind of stuff so maybe i can suggest you movies or series and maybe you can learn from them hahahaha.'''

user_question = st.text_input("",placeholder="enter")
if st.button("ASK",use_container_width=400) :
    prompt =persona +"here is the question asked by the user: "+ user_question
    response = model.generate_content(prompt)
    assert isinstance(response.text, object)
    st.text_area("",value=response.text, disabled=True,height=400)





import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo list")
st.write("This app is cool")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")

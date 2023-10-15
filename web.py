import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.save_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo list")
st.write("This app is cool")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')

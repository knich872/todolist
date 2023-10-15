import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.save_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This app was created with streamlit")
st.write("It's lit")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')

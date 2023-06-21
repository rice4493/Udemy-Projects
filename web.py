import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-do App")
st.subheader("This is my to-do list app.")
# using html
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

st.checkbox("Buy groceries")
st.checkbox("Throw trash")

for index, task in enumerate(todos):
    st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add a new task...',
              on_change=add_todo, key='new_todo')

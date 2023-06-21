import streamlit as st
import functions

todos = functions.get_todos('/Users/yuktanoela/PycharmProjects/UdemyProjects/List')

st.set_page_config(layout='wide')

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos('/Users/yuktanoela/PycharmProjects/UdemyProjects/List', todos)


st.title("To-do App")
st.subheader("This is my to-do list app.")
# using html
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

for index, task in enumerate(todos):
    checked = st.checkbox(task, key=f'action_{index}')
    if checked:
        todos.pop(index)
        functions.write_todos('/Users/yuktanoela/PycharmProjects/UdemyProjects/List', todos)
        st.experimental_rerun()

st.text_input(label='', placeholder='Add a new task...',
              on_change=add_todo, key='new_todo')

import pandas
import streamlit as st

st.set_page_config(layout='wide')

st.title("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean imperdiet nibh sed leo luctus viverra. Nullam sit amet 
condimentum eros, non porttitor ex. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras quam urna, luctus eu 
urna a, molestie volutpat velit. Pellentesque vel congue dui, a laoreet felis. Mauris tempor ultrices enim eu egestas. 
Vestibulum id congue urna.
"""
st.write(content)

st.header('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data-company.csv')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images-company/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images-company/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images-company/' + row['image'])

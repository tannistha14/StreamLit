import streamlit as st
import numpy
import pandas

st.title("Hello! this is our first application!")

st.write("below is our data of employees!")

data1=pandas.DataFrame({
    "Emp_ID":[101,102,103,104],
    "Emp_name":["Sachin","Rahul","Virat","Yash"]
})
st.write(data1)

data2=pandas.DataFrame(numpy.random.randn(25,3),columns=["A","B","C"])
st.bar_chart(data2)
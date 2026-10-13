import streamlit as st

# basics

st.title("Hello Streamlit")
st.write("First Streamlit App!")
st.header("Welcome to Streamlit")
st.subheader("This is a subheading")
st.text("This is the text!")


def Greet(name):
    st.write(f"Heyy! {name}")

value=st.text_input("Enter Your Name please!")
#Buttons, checkboxes, sliders
if st.button("Greet"):
    Greet(value)

if st.checkbox("I aggree"):
    st.write("You aggreed!")

val2=st.slider("Select a level: ", 1 , 2 , 3 )
st.write(f"level Selected: {val2}")

#File Uplaoder
st.file_uploader("Upload a file!", type=['zip'])

st.button("Upload")
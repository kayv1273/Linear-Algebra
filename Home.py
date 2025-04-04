import streamlit as st


st.set_page_config(
    page_title="Linear Algebra",
    # page_icon="👋",
)

st.title("Welcome to Linear Algebra!")
st.write("""
    **Linear Algebra** is here to help you practice linear algebra problems in the form of ax + b = c with ease.

    Please select a mode from the sidebar:

    - **Basic Mode**: This mode focuses on solving simple linear equations with integer solutions. Primarily for beginners or anyone needing to practice.

    - **Expert Mode**: This mode focuses on solving equations with decimal solutions. Primarily for those who are looking for a challenge.

    **How it works:**
    1. Once you select a mode, an equation will be generated randomly for you to solve.
    2. You will input your solution in the text box.
    3. You'll get instant feedback on whether your answer is correct or not.
    4. After each problem, you can move on to the next problem and continue practicing.

    **Happy Solving!**
    Keep practicing, and you'll improve your solving skills in no time!
""")
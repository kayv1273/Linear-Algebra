import streamlit as st
import random
import streamlit_shadcn_ui as ui

def generate_random(start: int, end: int):
    num = 0
    while num == 0:
        num = random.randint(start, end)
    return num

def generate_valid_equation(start: int, end: int):
    a = generate_random(start, end)
    x = random.randint(start, end)
    b = random.randint(start, end)
    c = a * x + b
    return a, b, c, x

# Initialize the problem once using session state
if "a" not in st.session_state:
    a, b, c, solution_x = generate_valid_equation(-10, 10)
    st.session_state.a = a
    st.session_state.b = b
    st.session_state.c = c
    st.session_state.solution_x = solution_x

st.set_page_config(page_title="Basic Page", page_icon="📈")
st.title("Linear Algebra: Basic Mode")

# Access the saved values from session state
a = st.session_state.a
b = st.session_state.b
c = st.session_state.c
solution_x = st.session_state.solution_x

# # Display the equation
st.write(f"Solve: {a}x + {b} = {c}")

# User input textbox
user_input = st.text_input("x = ", "")

# Check answer
if user_input:
    try:
        # Answer specifics
        user_answer = int(user_input)
        word = ""
        e_word = ""
        if b < 0:
            word = "Adding"
            e_word = "add"
            b = -(b)
        else:
            word = "Subtracting"
            e_word = "subtract"
        if user_answer == solution_x:
            st.success(f"Correct! {word} {b} to each side and dividing both sides by {a} gives x = {solution_x}.")
        else:
            st.error(f"Incorrect. You should {e_word} {b} to both sides and then divide {a} from both sides.")
    except ValueError:
        st.error("Please enter a valid integer.")

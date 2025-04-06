import streamlit as st
from streamlit_drawable_canvas import st_canvas
import gen_equation as ge

# Title 
st.set_page_config(page_title="Basic Mode", page_icon=None)
st.markdown(
    "<h1>LinearAlgebra: <span style='color:green'>Basic Mode</span></h1>",
    unsafe_allow_html=True
)

# Initialize the problem once using session state
a, b, c, x = ge.init_session_state("BASIC")

# Display the equation on screen
st.subheader(f"Solve: {a}x + {b} = {c}")

# User input textbox
user_input = st.text_input("x = ", "")

# Check user answer
ge.check_answer(user_input, a, b, c, x, "BASIC")

# Optional Scratch paper in sidebar
with st.sidebar:
    st.markdown("### Scratch Paper:")
    canvas_result = st_canvas(
        stroke_width=3,
        stroke_color='#000000',
        background_color='#FFFFFF',
        height=450,
        drawing_mode='freedraw',
    )
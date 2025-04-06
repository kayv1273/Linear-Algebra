import streamlit as st
from streamlit_drawable_canvas import st_canvas
import gen_equation as ge

# Title 
st.set_page_config(page_title="Expert Mode", page_icon=None)
st.markdown(
    "<h1>LinearAlgebra: <span style='color:red'>Expert Mode</span></h1>",
    unsafe_allow_html=True
)

# Initialize the problem once using session state
_a, _b, _c, _x = ge.init_session_state("EXPERT")

# Display the equation on screen and in terminal
st.subheader(f"Solve: {_a}x + {_b} = {_c}")

# User input textbox
st.write("(Round to the nearest 2 decimals)")
user_input = st.text_input("x = ", "")

# Check user answer
ge.check_answer(user_input, _a, _b, _c, _x, "EXPERT")

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
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from streamlit_drawable_canvas import st_canvas
import gen_equation as ge

# Title 
st.set_page_config(page_title="Expert Page", page_icon="📈")
st.markdown(
    "<h1>Linear Algebra: <span style='color:red'>Expert Mode</span></h1>",
    unsafe_allow_html=True
)

# Initialize the problem once using session state
if "_a" not in st.session_state:
    _a, _b, _c, _x = ge.generate_equation(-10, 10, "Expert")
    st.session_state._a = _a
    st.session_state._b = _b
    st.session_state._c = _c
    st.session_state._x = _x

    # Display solution in terminal 
    print(f"[EXPERT] x = {_x} (Equation: {_a}x + {_b} = {_c})")
# Access the saved values from session state
_a = st.session_state._a
_b = st.session_state._b
_c = st.session_state._c
_x = st.session_state._x

# Display the equation on screen and in terminal
st.subheader(f"Solve: {_a}x + {_b} = {_c} (Round to the nearest 2 decimals)")

# User input textbox
user_input = st.text_input("x = ", "")

answer_spec = {
    "pos": ["Subtracting", "from"],
    "neg": ["Adding", "to"]
}

# Check user answer
if user_input:
    try:
        user_answer = float(user_input)
        op = "pos"

        if _b < 0:
            op = "neg"
            _b = -(_b)
        
        # Correct Solution
        if user_answer == _x:
            st.success(f"Correct! {answer_spec[op][0]} {_b} {answer_spec[op][1]} each side and dividing both sides by {_a} gives x = {_x}.")
            st.balloons()
            
            # Refresh session states and rerun the app (page refresh)
            if st.button("Next Problem", type="primary"):
                streamlit_js_eval(js_expressions="parent.window.location.reload()")

        # Incorrect Solution
        else:
            st.error(f"Incorrect. You should try {answer_spec[op][0].lower()} {_b} {answer_spec[op][1]} both sides and then divide {_a} from both sides.")
    
    # Non-numerical value is entered
    except ValueError:
        st.error("Please enter a valid number.")

# Optional Scratch paper in sidebar
with st.sidebar:
    st.markdown("### Scratch Paper:")
    canvas_result = st_canvas(
        stroke_width=3,
        stroke_color='#000000',
        background_color='#FFFFFF',
        height=450,
        drawing_mode='freedraw',
        key="canvas_sidebar",
    )
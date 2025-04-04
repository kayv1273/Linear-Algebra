import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from streamlit_drawable_canvas import st_canvas
import gen_equation as ge

# Title 
st.set_page_config(page_title="Basic Page", page_icon="📈")
st.markdown(
    "<h1>Linear Algebra: <span style='color:green'>Basic Mode</span></h1>",
    unsafe_allow_html=True
)

# Initialize the problem once using session state
if "a" not in st.session_state:
    a, b, c, x = ge.generate_equation(-10, 10, "Basic")
    st.session_state.a = a
    st.session_state.b = b
    st.session_state.c = c
    st.session_state.x = x

    # Display solution in terminal 
    print(f"[BASIC] x = {x} (Equation: {a}x + {b} = {c})")
# Access the saved values from session state
a = st.session_state.a
b = st.session_state.b
c = st.session_state.c
x = st.session_state.x

# Display the equation on screen
st.subheader(f"Solve: {a}x + {b} = {c}")

# User input textbox
user_input = st.text_input("x = ", "")

answer_spec = {
    "pos": ["Subtracting", "from"],
    "neg": ["Adding", "to"]
}

# Check user answer
if user_input:
    try:
        user_answer = int(user_input)
        op = "pos"

        if b < 0:
            op = "neg"
            b = -(b)

        # Correct Solution
        if user_answer == x:
            st.success(f"Correct! {answer_spec[op][0]} {b} {answer_spec[op][1]} each side and dividing both sides by {a} gives x = {x}.")
            st.balloons()
            
            # Refresh session states and rerun the app (page refresh)
            if st.button("Next Problem", type="secondary"):
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
        
        # Incorrect Solution
        else:
            st.error(f"Incorrect. You should try {answer_spec[op][0].lower()} {b} {answer_spec[op][1]} both sides and then divide {a} from both sides.")
    
    # Non-integer values are an error
    except ValueError:
        st.error("Please enter a valid integer.")

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
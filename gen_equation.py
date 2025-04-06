import random
import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def generate_random(start: int, end: int) -> int:
    """
    Generate a random non-zero integer between start and end.

    Args:
        start (int): The lower bound of the number range.
        end (int): The upper bound of the number range.

    Returns:
        int: A randomly generated non-zero integer.
    """
    num = 0
    while num == 0:
        num = random.randint(start, end)
    return num


def generate_equation(start: int, end: int, mode: str) -> tuple:
    """
    Generates a linear equation of the form ax + b = c and returns all values.

    In "BASIC" mode, x is an integer.  
    In "EXPERT" mode, x is a rounded decimal (float with 2 decimal places).

    Args:
        start (int): The lower bound of the number range.
        end (int): The upper bound of the number range.
        mode (str): Either "BASIC" or "EXPERT", determines solution type.

    Returns:
        tuple: A tuple containing four values:
            a (int): Coefficient of x.
            b (int): Constant term.
            c (int or float): The result of ax + b.
            x (int or float): The solution for equation.
    """
    a = generate_random(start, end)
    b = generate_random(start, end)
    x = generate_random(start, end)
    c = a * x + b
    if mode == "EXPERT":
        x = round(random.uniform(start, end), 2)
        c = round(a * x + b, 2)
    return a, b, c, x


def init_session_state(mode: str):
    """
    Initializes the session state with a new equation each time the page is refreshed.

    Args:
        mode (str): The difficulty mode of the equation.

    Returns:
        tuple: Containing the equation components (a, b, c, x).
    """
    global wrong_count

    keys = [f"{mode}_a", f"{mode}_b", f"{mode}_c", f"{mode}_x"]

    # Generate the session states
    if keys[0] not in st.session_state:
        a, b, c, x = generate_equation(-10, 10, mode)
        st.session_state[keys[0]] = a
        st.session_state[keys[1]] = b
        st.session_state[keys[2]] = c
        st.session_state[keys[3]] = x
        wrong_count = 0

        # Display equation for dev
        print(f"[{mode}] x = {x} (Equation: {a}x + {b} = {c})")

    return (
        st.session_state[keys[0]],
        st.session_state[keys[1]],
        st.session_state[keys[2]],
        st.session_state[keys[3]]
    )


def check_answer(user_input : str, a : int, b : int, c: int, x : int, mode: str):
    """
    Checks if the user's input is the correct solution of the equation and
    displays feedback.

    Args:
        user_input (str): The input provided by the user.
        a (int): Coefficient of x.
        b (int): Constant term.
        x (int or float): The solution for equation.
        mode (str): Either "BASIC" or "EXPERT", determines solution type.

    Returns:
        None
    """
    global wrong_count

    answer_spec = {
        "pos": ["Subtracting", "from", "-"],
        "neg": ["Adding", "to", "+"]
    }

    # Check user answer
    if user_input:
        try:
            user_answer = -1000

            if mode == "BASIC":
                user_answer = int(user_input)
            elif mode == "EXPERT":
                user_answer = float(user_input)

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
                wrong_count += 1

                # Displays reveal answer after 5 wrong inputs
                if wrong_count > 4:
                    if st.button("Reveal Answer", type="secondary"):
                        st.write(f"Step 1: {a}x = {c} {answer_spec[op][2]} {b}")
                        st.write(f"Step 2: x = ({c} {answer_spec[op][2]} {b}) / {a}")
                        st.write(f"Final Answer: x = {x}")
                st.error(f"Incorrect. You should try {answer_spec[op][0].lower()} {b} {answer_spec[op][1]} both sides and then divide {a} from both sides.")
        
        # Non-integer values are an error
        except ValueError:
            st.error("Please enter a valid number.")
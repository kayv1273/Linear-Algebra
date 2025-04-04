import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_extras.switch_page_button import switch_page
import pages

st.set_page_config(
    page_title="Linear Algebra",
    # page_icon="👋",
)

# st.markdown(
#     """
#     <style>
#         [data-testid="stSidebar"] {
#             display: none;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.title("Welcome to Linear Algebra!")
st.write("Please select a mode from the side bar. Basic mode deals with only integer solutions. Expert mode deals with rounded decimal solutions.")
st.write("Happy solving!")

# st.markdown(
#     """
#     <a href="/Basic" target="_self">
#         <button style="
#             background-color: #4CAF50;
#             color: white;
#             padding: 10px 24px;
#             border: none;
#             border-radius: 8px;
#             text-align: center;
#             text-decoration: none;
#             display: inline-block;
#             font-size: 16px;
#             cursor: pointer;
#         ">
#             Basic
#         </button>
#     </a>
#     """,
#     unsafe_allow_html=True
# )
# st.markdown(
#     """
#     <a href="/Expert" target="_self">
#         <button style="
#             background-color: #FF603E;
#             color: white;
#             padding: 10px 24px;
#             border: none;
#             border-radius: 8px;
#             text-align: center;
#             text-decoration: none;
#             display: inline-block;
#             font-size: 16px;
#             cursor: pointer;
#         ">
#             Expert
#         </button>
#     </a>
#     """,
#     unsafe_allow_html=True
# )
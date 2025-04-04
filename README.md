# Linear Algebra: Technical Generalist Project

## Overview

This project helps students practice solving basic linear equations with one variable through the equation form ax + b = c, where a, b and c are integers, and the equation has an integer solution.

The requirements for this project were:

1. Random Equation Generation
   - Each time the apps runs (or refreshes), it should display a new equation with randomly chosen values for a, b and c.
   - Make sure the generated equation always has an integer solution.
2. User Input
   - Provide a numeric input field where the student can enter their answer for the value of x.
3. Feedback
   - After the student submits their answer, the app should let them know whether they were correct or not.
   - Display a success message for correct answers, and an encouragement or prompt to try again if the answer is incorrect.
4. User Experience
   - Keep the interface clean, intuitive and student-friendly.

These requirements were met and can be found in the Basic Mode page of the application.

### Assumptions made by me:

    - The numbers generated are non-zero.

## Getting Started

To boot up this project locally, you must have the following imports:

1. streamlit
2. streamlit_js_eval
3. streamlit_drawable_canvas

## Set up

1. Clone repository:

```sh
git clone https://github.com/kayv1273/Linear-Algebra
```

2. Run the server with command in terminal:

```sh
streamlit run Home.py
```

## Resources

- [Streamlit Doc](https://docs.streamlit.io)
- [Streamlit Drawable Canvas](https://github.com/andfanilo/streamlit-drawable-canvas)
- [ChatGPT](https://chatgpt.com)

## Extra Features

- Expert Mode: This mode was an extra feature added by me (for fun) to implement an ax + b = c equation with a decimal solution. It is exactly the same format as the Basic Mode, but the answer will have to be rounded to 2 decimals.

- Scratch Paper: In the side bar for the Basic and Expert Mode Pages, there is a drawable canvas that the user can have scratch paper. This is entirely optional and up to the user whether or not they want to use it.

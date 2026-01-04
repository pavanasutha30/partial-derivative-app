
import streamlit as st
import sympy as sp

# --- PAGE CONFIG ---
st.set_page_config(page_title="Partial Derivative Lab", layout="centered")

# --- APP TITLE ---
st.title("Partial Derivative Explorer")
st.markdown("Explore and compute partial derivatives for functions $f(x, y)$.")

# --- CREATE TABS ---
tab_info, tab_calc = st.tabs(["📚 Definitions", "🧮 Calculator"])

# --- TAB 1: DEFINITIONS & EXPLANATION ---
with tab_info:
    st.header("What is a Partial Derivative?")
    st.write("""
    For a function of two variables $f(x, y)$, the partial derivative represents the rate of change 
    of the function with respect to one variable while holding the other constant.
    """)

    st.subheader("The Partial Derivative with respect to $x$")
    st.write("Holding $y$ as a constant:")
    st.latex(r"\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}")

    st.subheader("The Partial Derivative with respect to $y$")
    st.write("Holding $x$ as a constant:")
    st.latex(r"\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}")



    st.info("""
    **Visual Tip:** If you imagine a 3D surface, the partial derivative $\\partial f/\\partial x$ 
    is the slope of the line tangent to the surface when you slice it parallel to the x-axis.
    """)

# --- TAB 2: CALCULATOR ---
with tab_calc:
    st.header("Multivariable Calculator")
    st.write("Enter your function below using `x` and `y`.")

    # Input field
    user_func = st.text_input("Enter function $f(x, y)$:", value="x**2 + 3*x*y + sin(y)")

    try:
        # Define the symbols
        x, y = sp.symbols('x y')

        # Parse the user input into a math expression
        f = sp.sympify(user_func)

        # Calculate the derivatives
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)

        # Display Results
        st.markdown("---")
        st.subheader("Step-by-Step Result")

        st.write("Input Function:")
        st.latex(f"f(x, y) = {sp.latex(f)}")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("### W.R.T. $x$")
            st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(df_dx))
            st.caption("Calculated by treating $y$ as a constant.")

        with c2:
            st.markdown("### W.R.T. $y$")
            st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(df_dy))
            st.caption("Calculated by treating $x$ as a constant.")

    except Exception as e:
        st.error(f"Make sure to use correct syntax (e.g., `*` for multiplication and `**` for powers). Error: {e}")

# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")

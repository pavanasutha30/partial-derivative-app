
import streamlit as st
import sympy as sp

# Page configuration
st.set_page_config(page_title="Partial Derivative Explorer", layout="wide")

st.title("Multivariable Calculus: Partial Derivatives")

# --- UPDATED TABS ---
tab1, tab2, tab3 = st.tabs(["🏠 General", "📖 Definitions & Theorems", "🧮 Calculator"])

# --- TAB 1: GENERAL ---
with tab1:
    st.header("Introduction to Multivariable Functions")
    st.write("""
    In the real world, most things depend on more than one factor. For example, the volume of a 
    cylinder depends on both its **radius** ($r$) and its **height** ($h$). 
    
    In mathematics, we represent these relationships as functions of two or more variables:
    """)
    st.latex(r"z = f(x, y)")
    
    st.info("""
    **The Goal of this App:** This tool helps you understand how a function changes when you move in just one direction 
    (either the $x$-direction or the $y$-direction) while keeping everything else perfectly still.
    """)

# --- TAB 2: DEFINITIONS & THEOREMS ---
with tab2:
    st.header("Mathematical Foundations")
    
    st.subheader("1. Formal Definition")
    st.write("The partial derivative of $f(x, y)$ with respect to $x$ at a point $(a, b)$ is:")
    st.latex(r"f_x(a, b) = \lim_{h \to 0} \frac{f(a+h, b) - f(a, b)}{h}")
    
    st.write("The partial derivative of $f(x, y)$ with respect to $y$ at a point $(a, b)$ is:")
    st.latex(r"f_y(a, b) = \lim_{k \to 0} \frac{f(a, b+k) - f(a, b)}{k}")

    

    st.subheader("2. Clairaut's Theorem")
    st.write("""
    An important theorem in multivariable calculus states that if the second-order partial 
    derivatives are continuous, then the order of differentiation doesn't matter:
    """)
    st.latex(r"\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}")

# --- TAB 3: CALCULATOR ---
with tab3:
    st.header("Partial Derivative Calculator")
    st.write("Enter a function of $x$ and $y$ to compute $\\frac{\\partial f}{\\partial x}$ and $\\frac{\\partial f}{\\partial y}$.")

    user_input = st.text_input("Enter function $f(x, y)$:", value="x**3 + x**2*y**3 - 2*y**2")
    
    try:
        x, y = sp.symbols('x y')
        f = sp.sympify(user_input)
        
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)
        
        st.divider()
        st.write("**Calculated Derivatives:**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(df_dx))
        with col2:
            st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(df_dy))
            
    except Exception as e:
        st.error(f"Syntax Error: {e}")

# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")


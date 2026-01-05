import streamlit as st
import sympy as sp

# Page configuration
st.set_page_config(page_title="Partial Derivatives Lab", layout="wide")

# 1. UPDATED MAIN TITLE
st.title("Partial Derivatives as Rates of Change")

# Create Three Tabs
tab1, tab2, tab3 = st.tabs(["🏠 General", "📖 Definitions & Theorems", "🧮 Calculator"])

# --- TAB 1: GENERAL ---
with tab1:
    st.header("Partial Derivatives and Rates of Change")
    
    st.write("""
    In calculus, a derivative represents a rate of change. For a multivariable function $z = f(x, y)$, 
    a **partial derivative** measures how the output ($z$) changes when only *one* of the input variables 
    changes while the other is held constant. For example, if $z$ represents the temperature on a metal plate 
    at coordinates $(x, y)$, the partial derivative with respect to $x$ tells us how fast the temperature 
    is rising or falling as we move strictly in the east-west direction. This concept is vital in physics, 
    economics, and engineering, where we often need to isolate the impact of a single factor in a 
    complex system.
    """)

    

    st.subheader("Real-World Applications")
    st.write("Partial derivatives are used whenever multiple factors influence a single outcome:")
    
    # Real-world examples table
    st.table([
        {"Field": "Economics", "Function": "Production Cost", "Rate of Change Meaning": "How cost changes if labor increases but capital stays the same."},
        {"Field": "Meteorology", "Function": "Air Pressure", "Rate of Change Meaning": "How pressure changes as you move North, holding Altitude constant."},
        {"Field": "Thermodynamics", "Function": "Gas Pressure", "Rate of Change Meaning": "How pressure changes as Temperature rises, holding Volume constant."},
        {"Field": "Medicine", "Function": "Drug Concentration", "Rate of Change Meaning": "How concentration changes over time for a specific dosage amount."}
    ])
    
    st.info("""
    **The Goal of this App:** Use the tabs above to learn the formal definitions or use the calculator 
    to find the exact rates of change for any multivariable function.
    """)
    

# --- TAB 2: DEFINITIONS & THEOREMS ---
with tab2:
    st.header("Mathematical Foundations")
    
    # 3. ADDED SUBTOPIC: NOTATIONS
    st.subheader("Notations for Partial Derivatives")
    st.write("""
    There are several common ways to write partial derivatives. If $z = f(x, y)$, the following 
    notations all mean the same thing:
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**For the derivative with respect to $x$:**")
        st.latex(r"f_x, \quad \frac{\partial f}{\partial x}, \quad \frac{\partial z}{\partial x}, \quad D_1f, \quad D_xf")
    with col_b:
        st.markdown("**For the derivative with respect to $y$:**")
        st.latex(r"f_y, \quad \frac{\partial f}{\partial y}, \quad \frac{\partial z}{\partial y}, \quad D_2f, \quad D_yf")

    st.divider()

    # 4. ADDED SUBTOPIC: RULES
    st.subheader("Rules for Finding Partial Derivatives of $z=f(x, y)$")
    st.write("""
    To find partial derivatives efficiently, follow these two fundamental rules:
    """)
    
    st.success("""
    1. **To find $f_x$:** Regard $y$ as a constant and differentiate $f(x, y)$ with respect to $x$ using 
    standard single-variable differentiation rules (Power rule, Product rule, etc.).
    
    2. **To find $f_y$:** Regard $x$ as a constant and differentiate $f(x, y)$ with respect to $y$.
    """)
    
    st.info("""
    **Example:** If $f(x, y) = x^2y$, then to find $f_x$, we treat $y$ like a number (e.g., 5). 
    The derivative of $x^2(5)$ is $2x(5)$, so $f_x = 2xy$.
    """)

# --- TAB 3: CALCULATOR ---
with tab3:
    st.header("Partial Derivative Calculator")
    st.write("Enter a function to see the rates of change $\\frac{\\partial f}{\\partial x}$ and $\\frac{\\partial f}{\\partial y}$.")

    user_input = st.text_input("Enter function $f(x, y)$:", value="x**2 * y + sin(x*y)")
    
    try:
        x, y = sp.symbols('x y')
        f = sp.sympify(user_input)
        
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)
        
        st.divider()
        res1, res2 = st.columns(2)
        
        with res1:
            st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(df_dx))
        with res2:
            st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(df_dy))
            
    except Exception as e:
        st.error(f"Check your math syntax! Error: {e}")

# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")



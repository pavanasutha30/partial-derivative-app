import streamlit as st
import sympy as sp

# Page configuration
st.set_page_config(page_title="Partial Derivatives Lab", layout="wide")

# 1. MAIN TITLE
st.title("Partial Derivatives as Rates of Change")

# Create Three Tabs
tab1, tab2, tab3 = st.tabs(["🏠 General", "📖 Definitions & Theorems", "🧮 Calculator"])

# --- TAB 1: GENERAL ---
with tab1:
    st.header("Partial Derivatives and Rates of Change")
    
    st.write("""
    In calculus, a derivative represents a rate of change. For a multivariable function $z = f(x, y)$, 
    a **partial derivative** measures how the output ($z$) changes when only *one* of the input variables 
    changes while the other is held constant. 
    
    This concept is vital in physics, economics, and engineering, where we often need to isolate the 
    impact of a single factor in a complex system.
    """)

    st.subheader("Real-World Applications")
    st.table([
        {"Field": "Economics", "Function": "Production Cost", "Rate of Change Meaning": "How cost changes if labor increases but capital stays the same."},
        {"Field": "Meteorology", "Function": "Air Pressure", "Rate of Change Meaning": "How pressure changes as you move North, holding Altitude constant."},
        {"Field": "Thermodynamics", "Function": "Gas Pressure", "Rate of Change Meaning": "How pressure changes as Temperature rises, holding Volume constant."},
        {"Field": "Medicine", "Function": "Drug Concentration", "Rate of Change Meaning": "How concentration changes over time for a specific dosage amount."}
    ])

# --- TAB 2: DEFINITIONS & THEOREMS ---
with tab2:
    st.header("Mathematical Foundations")
    
    # LIMIT DEFINITION
    st.subheader("1. The Limit Definition")
    st.write("The formal definition of a partial derivative uses limits, similar to single-variable calculus:")
    col_lim1, col_lim2 = st.columns(2)
    with col_lim1:
        st.latex(r"f_x(x, y) = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}")
    with col_lim2:
        st.latex(r"f_y(x, y) = \lim_{k \to 0} \frac{f(x, y+k) - f(x, y)}{k}")

    st.divider()

    # NOTATIONS
    st.subheader("2. Notations for Partial Derivatives")
    st.write("Different textbooks use different symbols to represent the same operation:")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**With respect to $x$:**")
        st.latex(r"f_x, \quad \frac{\partial f}{\partial x}, \quad \frac{\partial z}{\partial x}, \quad D_x f")
    with col_b:
        st.markdown("**With respect to $y$:**")
        st.latex(r"f_y, \quad \frac{\partial f}{\partial y}, \quad \frac{\partial z}{\partial y}, \quad D_y f")

    st.divider()

    # RULES
    st.subheader("3. Rules for Finding Partial Derivatives of $z=f(x,y)$")
    st.info("""
    1. **To find $f_x$:** Treat $y$ as a constant. Differentiate normally with respect to $x$.
    2. **To find $f_y$:** Treat $x$ as a constant. Differentiate normally with respect to $y$.
    """)

    

    st.divider()

    # CLAIRAUT'S THEOREM
    st.subheader("4. Clairaut's Theorem (Mixed Partials)")
    st.write("""
    This theorem states that if a function $f$ is defined on a disk $D$ and the mixed second-order 
    partial derivatives are continuous, then the order of differentiation does not matter:
    """)
    st.latex(r"\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}")

# --- TAB 3: CALCULATOR ---
with tab3:
    st.header("Partial Derivative Calculator")
    st.write("Enter your function $f(x, y)$ below:")

    user_input = st.text_input("Function Input (e.g., x**2 * y + 5*y):", value="x**2 * y + sin(x*y)")
    
    try:
        x, y = sp.symbols('x y')
        f = sp.sympify(user_input)
        
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.success("Result for $\partial f / \partial x$")
            st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(df_dx))
        with c2:
            st.success("Result for $\partial f / \partial y$")
            st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(df_dy))
            
    except Exception as e:
        st.error("Error: Please check your mathematical syntax.")
        
# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")




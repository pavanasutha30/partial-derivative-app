import streamlit as st
import sympy as sp
import random

# Page configuration
st.set_page_config(page_title="Partial Derivatives Lab", layout="wide")

st.title("Partial Derivatives as Rates of Change")

# Create Three Tabs
tab1, tab2, tab3 = st.tabs(["🏠 General", "📖 Definitions & Theorems", "🧮 Calculator & Practice"])

# --- TAB 1: GENERAL (Retained) ---
with tab1:
    st.header("Partial Derivatives and Rates of Change")
    st.write("""
    In calculus, a derivative represents a rate of change. For a multivariable function $z = f(x, y)$, 
    a **partial derivative** measures how the output ($z$) changes when only *one* of the input variables 
    changes while the other is held constant.
    """)
    st.subheader("Real-World Applications")
    st.table([
        {"Field": "Economics", "Function": "Production Cost", "Rate of Change Meaning": "How cost changes if labor increases but capital stays the same."},
        {"Field": "Meteorology", "Function": "Air Pressure", "Rate of Change Meaning": "How pressure changes as you move North, holding Altitude constant."},
        {"Field": "Thermodynamics", "Function": "Gas Pressure", "Rate of Change Meaning": "How pressure changes as Temperature rises, holding Volume constant."},
        {"Field": "Medicine", "Function": "Drug Concentration", "Rate of Change Meaning": "How concentration changes over time for a specific dosage amount."}
    ])

# --- TAB 2: DEFINITIONS & THEOREMS (Retained) ---
with tab2:
    st.header("Mathematical Foundations")
    st.subheader("1. The Limit Definition")
    col_lim1, col_lim2 = st.columns(2)
    with col_lim1: st.latex(r"f_x(x, y) = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}")
    with col_lim2: st.latex(r"f_y(x, y) = \lim_{k \to 0} \frac{f(x, y+k) - f(x, y)}{k}")
    
    st.subheader("2. Notations")
    st.latex(r"f_x, \quad \frac{\partial f}{\partial x}, \quad \frac{\partial z}{\partial x}")
    
    st.subheader("3. Clairaut's Theorem")
    st.latex(r"\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}")

# --- TAB 3: CALCULATOR & PRACTICE ---
with tab3:
    calc_mode, practice_mode = st.radio("Choose Mode:", ["Calculator with Steps", "Real-Life Problem Generator"], horizontal=True)

    x, y = sp.symbols('x y')

    if calc_mode == "Calculator with Steps":
        st.header("Step-by-Step Calculator")
        user_input = st.text_input("Enter function $f(x, y)$:", value="x**2 * y + 3*y**4")
        
        try:
            f = sp.sympify(user_input)
            df_dx = sp.diff(f, x)
            df_dy = sp.diff(f, y)

            st.write("### Solution Steps")
            
            # Step-by-Step Logic for X
            with st.expander("Show steps for ∂f/∂x"):
                st.write("**Rule:** Treat $y$ as a constant.")
                st.write(f"1. Identify terms containing $x$: {f}")
                st.write(f"2. Differentiate with respect to $x$:")
                st.latex(r"\frac{\partial}{\partial x}(" + sp.latex(f) + ")")
                st.write("3. Final Result:")
                st.success(f"∂f/∂x = {df_dx}")

            # Step-by-Step Logic for Y
            with st.expander("Show steps for ∂f/∂y"):
                st.write("**Rule:** Treat $x$ as a constant.")
                st.write(f"1. Identify terms containing $y$: {f}")
                st.write(f"2. Differentiate with respect to $y$:")
                st.latex(r"\frac{\partial}{\partial y}(" + sp.latex(f) + ")")
                st.write("3. Final Result:")
                st.success(f"∂f/∂y = {df_dy}")

        except:
            st.error("Please enter a valid function.")

    else:
        st.header("Real-Life Scenario Generator")
        
        # Scenarios Database
        scenarios = [
            {
                "title": "Ideal Gas Law",
                "context": "The pressure $P$ of a gas is given by $P(T, V) = \\frac{8.31T}{V}$, where $T$ is temperature and $V$ is volume.",
                "func": 8.31 * x / y,  # x=T, y=V
                "vars": ("T", "V"),
                "question": "Find the rate of change of pressure with respect to Temperature ($T$)."
            },
            {
                "title": "Production Output",
                "context": "A factory's production is $Q(L, K) = 50L^{0.5}K^{0.5}$, where $L$ is labor and $K$ is capital.",
                "func": 50 * (x**0.5) * (y**0.5), # x=L, y=K
                "vars": ("L", "K"),
                "question": "Find the marginal productivity of Labor (∂Q/∂L)."
            }
        ]

        if st.button("Generate New Problem"):
            st.session_state.problem = random.choice(scenarios)
        
        if 'problem' in st.session_state:
            prob = st.session_state.problem
            st.subheader(prob["title"])
            st.write(prob["context"])
            st.info(prob["question"])
            
            if st.button("Show Problem Solution"):
                f_prob = prob["func"]
                diff_prob = sp.diff(f_prob, x)
                st.write("**Step 1:** Identify the variable to differentiate. Here it is", prob["vars"][0])
                st.write("**Step 2:** Treat", prob["vars"][1], "as a constant.")
                st.write("**Step 3:** Apply differentiation:")
                st.latex(sp.latex(diff_prob))
        
# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")





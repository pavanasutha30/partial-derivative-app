import streamlit as st
import sympy as sp
import random

# Page configuration
st.set_page_config(page_title="Partial Derivatives Lab", layout="wide")

st.title("Partial Derivatives as Rates of Change")

# Create Three Tabs
tab1, tab2, tab3 = st.tabs(["🏠 General", "📖 Definitions & Theorems", "🧮 Calculator & Practice"])

# --- TAB 1: GENERAL ---
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

# --- TAB 2: DEFINITIONS & THEOREMS ---
with tab2:
    st.header("Mathematical Foundations")
    st.subheader("1. The Limit Definition")
    col_lim1, col_lim2 = st.columns(2)
    with col_lim1: st.latex(r"f_x(x, y) = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}")
    with col_lim2: st.latex(r"f_y(x, y) = \lim_{k \to 0} \frac{f(x, y+k) - f(x, y)}{k}")
    
    st.subheader("2. Notations")
    st.latex(r"f_x, \quad \frac{\partial f}{\partial x}, \quad \frac{\partial z}{\partial x}")
    
    st.subheader("3. Rules for Finding Partial Derivatives")
    st.info("To find $f_x$, treat $y$ as a constant. To find $f_y$, treat $x$ as a constant.")
    
    st.subheader("4. Clairaut's Theorem")
    st.latex(r"\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}")

# --- TAB 3: CALCULATOR & PRACTICE ---
with tab3:
    # FIXED LINE: Only one variable to store the selection
    mode = st.radio("Choose Mode:", ["Calculator with Steps", "Real-Life Problem Generator"], horizontal=True)

    x, y = sp.symbols('x y')

    if mode == "Calculator with Steps":
        st.header("Step-by-Step Calculator")
        user_input = st.text_input("Enter function $f(x, y)$:", value="x**2 * y + 3*y**4")
        
        try:
            f = sp.sympify(user_input)
            df_dx = sp.diff(f, x)
            df_dy = sp.diff(f, y)

            st.write("### Solution Results")
            
            col1, col2 = st.columns(2)
            with col1:
                st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(df_dx))
                with st.expander("Show Steps for x"):
                    st.write("**Process:**")
                    st.write("1. Look at $f(x, y) = ", f, "$")
                    st.write("2. Treat $y$ as a constant value.")
                    st.write("3. Apply the power/chain rules to $x$.")
                    st.success(f"Result: {df_dx}")
                    
            with col2:
                st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(df_dy))
                with st.expander("Show Steps for y"):
                    st.write("**Process:**")
                    st.write("1. Look at $f(x, y) = ", f, "$")
                    st.write("2. Treat $x$ as a constant value.")
                    st.write("3. Apply the power/chain rules to $y$.")
                    st.success(f"Result: {df_dy}")
        except:
            st.error("Invalid math syntax. Use * for multiply and ** for power.")

    else:
        st.header("Real-Life Scenario Generator")
        
        scenarios = [
            {
                "title": "Ideal Gas Law",
                "context": "The pressure $P$ of a gas is given by $P(T, V) = \\frac{8.31T}{V}$.",
                "func": 8.31 * x / y, 
                "vars": ("T", "V"),
                "question": "Find the rate of change of pressure with respect to Temperature ($T$)."
            },
            {
                "title": "Production Output (Cobb-Douglas)",
                "context": "A factory's production is $Q(L, K) = 50L^{0.5}K^{0.5}$.",
                "func": 50 * (x**0.5) * (y**0.5),
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
                st.write(f"**Step 1:** We want to find the derivative with respect to **{prob['vars'][0]}**.")
                st.write(f"**Step 2:** Treat **{prob['vars'][1]}** as a constant.")
                st.write("**Step 3:** Perform the differentiation:")
                st.latex(r"\text{Result: } " + sp.latex(diff_prob))
# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")






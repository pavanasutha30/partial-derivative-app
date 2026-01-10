import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
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
    mode = st.radio("Choose Mode:", ["Calculator & 3D Visualizer", "Real-Life Problem Generator"], horizontal=True)
    x_sym, y_sym = sp.symbols('x y')

    if mode == "Calculator & 3D Visualizer":
        st.header("Step-by-Step Calculator & Visualizer")
        user_input = st.text_input("Enter function $f(x, y)$:", value="x**2 - y**2")
        
        try:
            f_expr = sp.sympify(user_input)
            df_dx = sp.diff(f_expr, x_sym)
            df_dy = sp.diff(f_expr, y_sym)

            # --- STEP BY STEP SECTION ---
            st.subheader("🔍 Worked Problem Example")
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                st.success(f"**Partial w.r.t x (∂f/∂x)**")
                st.latex(sp.latex(df_dx))
                with st.expander("Show Steps"):
                    st.write("1. Treat $y$ as a constant.")
                    st.write(f"2. Apply differentiation to: ${sp.latex(f_expr)}$")
                    st.write(f"3. Result: ${sp.latex(df_dx)}$")
            with col_calc2:
                st.success(f"**Partial w.r.t y (∂f/∂y)**")
                st.latex(sp.latex(df_dy))
                with st.expander("Show Steps"):
                    st.write("1. Treat $x$ as a constant.")
                    st.write(f"2. Apply differentiation to: ${sp.latex(f_expr)}$")
                    st.write(f"3. Result: ${sp.latex(df_dy)}$")

            # --- VISUALIZATION SECTION ---
            st.divider()
            st.subheader("📊 3D Meaningful Visualization")
            
            # Create data for plot
            f_func = sp.lambdify((x_sym, y_sym), f_expr, "numpy")
            x_vals = np.linspace(-5, 5, 50)
            y_vals = np.linspace(-5, 5, 50)
            X, Y = np.meshgrid(x_vals, y_vals)
            try:
                Z = f_func(X, Y)
                if isinstance(Z, (int, float)): # Handle constant functions
                    Z = np.full(X.shape, Z)

                fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
                fig.update_layout(title='Surface Plot of f(x, y)', autosize=False,
                                  width=700, height=700,
                                  margin=dict(l=65, r=50, b=65, t=90))
                st.plotly_chart(fig)
                
                # Aspect Explanations
                st.markdown("""
                **3 Key Aspects of this Visualization:**
                1. **Surface Geometry:** The 3D shape represents all possible outputs of $f(x,y)$.
                2. **$f_x$ (x-slope):** If you move along the X-axis (left-right), the steepness of the surface is $\\frac{\\partial f}{\\partial x}$.
                3. **$f_y$ (y-slope):** If you move along the Y-axis (forward-back), the steepness is $\\frac{\\partial f}{\\partial y}$.
                """)
            except:
                st.warning("Visualization not available for this complex function.")

        except Exception as e:
            st.error(f"Syntax Error: {e}")

    else:
        st.header("Real-Life Scenario Generator")
        
        scenarios = [
            {
                "title": "Thermodynamics: Ideal Gas Law",
                "context": "The pressure $P$ of a gas is given by $P(T, V) = \\frac{8.31T}{V}$.",
                "func": 8.31 * x_sym / y_sym, 
                "vars": ("Temperature T", "Volume V"),
                "question": "Find the rate of change of pressure with respect to Temperature.",
                "interpretation": "This derivative represents how much the pressure increases for every 1-unit increase in temperature while volume is constant."
            },
            {
                "title": "Economics: Cobb-Douglas Production",
                "context": "A factory output is $Q(L, K) = 50L^{0.5}K^{0.5}$, where $L$ is labor and $K$ is capital.",
                "func": 50 * (x_sym**0.5) * (y_sym**0.5),
                "vars": ("Labor L", "Capital K"),
                "question": "Find the Marginal Productivity of Labor (∂Q/∂L).",
                "interpretation": "This derivative shows the additional output produced by adding one more unit of labor while keeping capital fixed."
            }
        ]

        if st.button("Generate New Problem"):
            st.session_state.problem = random.choice(scenarios)
        
        if 'problem' in st.session_state:
            prob = st.session_state.problem
            st.subheader(prob["title"])
            st.write(prob["context"])
            st.warning(f"**Question:** {prob['question']}")
            
            if st.button("Reveal Solution & Interpretation"):
                f_prob = prob["func"]
                diff_prob = sp.diff(f_prob, x_sym)
                st.write(f"**Step 1:** Differentiate with respect to {prob['vars'][0]}.")
                st.write(f"**Step 2:** Treat {prob['vars'][1]} as a constant.")
                st.latex(r"\text{Solution: } " + sp.latex(diff_prob))
                st.success(f"**Meaning:** {prob['interpretation']}")
                
# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")








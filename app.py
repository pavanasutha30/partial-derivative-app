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
    st.write("""
    In mathematics, a partial derivative allows us to isolate the effect of a single independent variable on a 
    system that depends on multiple factors. Mathematically, this is done by treating all other variables 
    as constants—essentially "freezing" them in place. By doing so, we reduce a multivariable function to a 
    single-variable one, allowing us to calculate the **instantaneous rate of change** along a specific axis. 
    This is equivalent to finding the slope of the tangent line to the surface when it is intersected by a 
    plane parallel to the coordinate axes.
    """)
    
    st.write("""
    This technique is vital in various fields where we need to understand how one specific change impacts 
    an outcome, as shown in the table below:
    """)
    
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
    
    st.subheader("2. Notations for Partial Derivatives")
    st.write("The following notations are used to represent partial derivatives:")
    
    col_not1, col_not2 = st.columns(2)
    
    with col_not1:
        st.markdown("**With respect to $x$:**")
        st.latex(r"f_x(x, y) = \frac{\partial f}{\partial x} = \frac{\partial z}{\partial x} = f_1 = D_1f")
        
    with col_not2:
        st.markdown("**With respect to $y$:**")
        st.latex(r"f_y(x, y) = \frac{\partial f}{\partial y} = \frac{\partial z}{\partial y} = f_2 = D_2f")
    
    st.subheader("3. Rules for Finding Partial Derivatives")
    st.info("""
    1. To find $f_x$, regard $y$ as a constant and differentiate $f(x,y)$ with respect to $x$.
    2. To find $f_y$, regard $x$ as a constant and differentiate $f(x,y)$ with respect to $y$.
    """)
    
    st.subheader("4. Clairaut's Theorem (Mixed Partials)")
    st.write("""
    Suppose $f$ is defined on a disk $D$ that contains the point $(a,b)$. 
    If the functions $f_{xy}$ and $f_{yx}$ are both continuous on $D$, then:
    """)
    st.latex(r"f_{xy}(a, b) = f_{yx}(a, b)")
    # Alternatively, in Leibniz notation:
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
            st.subheader("🔍 Worked Problem Example (Exam-Style)")
            
            # Helper to generate steps
            def get_manual_steps(expression, var_to_diff, var_to_fix):
                terms = sp.Add.make_args(expression)
                steps = []
                steps.append(f"**Step 1:** We are differentiating with respect to ${var_to_diff}$. We treat ${var_to_fix}$ as a constant.")
                steps.append(f"**Step 2:** Break the function into its individual terms: {', '.join(['$' + sp.latex(t) + '$' for t in terms])}")
                
                term_results = []
                for t in terms:
                    diff_t = sp.diff(t, var_to_diff)
                    term_results.append(sp.latex(diff_t))
                    steps.append(f"- The derivative of ${sp.latex(t)}$ is ${sp.latex(diff_t)}$.")
                
                final_res = sp.latex(sp.diff(expression, var_to_diff))
                steps.append(f"**Step 3:** Combine the results to get the final answer:")
                return steps, final_res

            col_calc1, col_calc2 = st.columns(2)
            
            with col_calc1:
                st.success(f"**Partial w.r.t $x$ ($\partial f/\partial x$)**")
                x_steps, x_final = get_manual_steps(f_expr, x_sym, y_sym)
                st.latex(r"\frac{\partial f}{\partial x} = " + x_final)
                with st.expander("View Full Exam-Style Solution"):
                    for s in x_steps:
                        st.write(s)
                    st.latex(r"\text{Final Result: } " + x_final)

            with col_calc2:
                st.success(f"**Partial w.r.t $y$ ($\partial f/\partial y$)**")
                y_steps, y_final = get_manual_steps(f_expr, y_sym, x_sym)
                st.latex(r"\frac{\partial f}{\partial y} = " + y_final)
                with st.expander("View Full Exam-Style Solution"):
                    for s in y_steps:
                        st.write(s)
                    st.latex(r"\text{Final Result: } " + y_final)

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
        
        # Expanded Scenarios Database (5 Problems)
        scenarios = [
            {
                "title": "Thermodynamics: Ideal Gas Law",
                "context": "The pressure $P$ of a gas is given by $P(T, V) = \\frac{8.31T}{V}$, where $T$ is Temperature and $V$ is Volume.",
                "func": 8.31 * x_sym / y_sym, 
                "vars": ("Temperature (T)", "Volume (V)"),
                "question": "Find the rate of change of pressure with respect to Temperature (∂P/∂T).",
                "interpretation": "This tells us how much the pressure increases for every 1-unit increase in temperature, assuming the container size (volume) does not change."
            },
            {
                "title": "Economics: Cobb-Douglas Production",
                "context": "A factory output is $Q(L, K) = 50L^{0.5}K^{0.5}$, where $L$ is Labor and $K$ is Capital.",
                "func": 50 * (x_sym**0.5) * (y_sym**0.5),
                "vars": ("Labor (L)", "Capital (K)"),
                "question": "Find the Marginal Productivity of Labor (∂Q/∂L).",
                "interpretation": "This represents the additional output gained by hiring one more worker (unit of labor) while keeping your equipment and machines (capital) constant."
            },
            {
                "title": "Biology: Body Surface Area (BSA)",
                "context": "The Mosteller formula for BSA is $B(w, h) = \\sqrt{\\frac{wh}{3600}}$, where $w$ is weight (kg) and $h$ is height (cm).",
                "func": sp.sqrt(x_sym * y_sym / 3600),
                "vars": ("Weight (w)", "Height (h)"),
                "question": "Find the rate of change of BSA with respect to Weight (∂B/∂w).",
                "interpretation": "This indicates how much a patient's body surface area changes per kilogram of weight gain, which is crucial for determining accurate medication dosages."
            },
            {
                "title": "Geometry: Volume of a Cylinder",
                "context": "The volume of a cylinder is $V(r, h) = \\pi r^2 h$, where $r$ is radius and $h$ is height.",
                "func": sp.pi * x_sym**2 * y_sym,
                "vars": ("Radius (r)", "Height (h)"),
                "question": "Find the rate of change of Volume with respect to Radius (∂V/∂r).",
                "interpretation": "This represents the 'Marginal Volume'—how much the total volume expands as you increase the thickness of the cylinder while keeping its length the same."
            },
            {
                "title": "Physics: Resistance in Parallel",
                "context": "For two resistors in parallel, the total resistance $R$ is $R(x, y) = \\frac{xy}{x+y}$, where $x$ and $y$ are individual resistances.",
                "func": (x_sym * y_sym) / (x_sym + y_sym),
                "vars": ("Resistor X", "Resistor Y"),
                "question": "Find the sensitivity of total resistance with respect to Resistor X (∂R/∂x).",
                "interpretation": "This shows how sensitive the entire electrical circuit is to a change in the first resistor. It helps engineers understand which component has the most influence."
            }
        ]

        if st.button("Generate New Problem"):
            st.session_state.problem = random.choice(scenarios)
        
        if 'problem' in st.session_state:
            prob = st.session_state.problem
            st.subheader(f"📍 {prob['title']}")
            st.write(prob["context"])
            
            
            
            st.warning(f"**Question:** {prob['question']}")
            
            if st.button("Reveal Solution & Interpretation"):
                f_prob = prob["func"]
                diff_prob = sp.diff(f_prob, x_sym)
                
                st.markdown("---")
                st.write("### 🖋️ Step-by-Step Solution")
                st.write(f"**Step 1:** Identify the focus variable. We want to find the rate of change for **{prob['vars'][0]}**.")
                st.write(f"**Step 2:** Regard **{prob['vars'][1]}** as a constant.")
                st.write(f"**Step 3:** Differentiate the expression:")
                st.latex(r"\frac{\partial}{\partial " + sp.latex(x_sym) + r"} \left(" + sp.latex(f_prob) + r"\right)")
                
                st.latex(r"\text{Result: } " + sp.latex(diff_prob))
                
                st.success(f"**Mathematical Meaning:** {prob['interpretation']}")
                
# --- SIDEBAR HELP ---
st.sidebar.header("Math Syntax Guide")
st.sidebar.code("x^2   -> x**2\n3xy   -> 3*x*y\nsin x -> sin(x)\ne^x   -> exp(x)")















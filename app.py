import streamlit as st
import pyomo.environ as pyo
from pyomo.opt import SolverFactory, SolverStatus, TerminationCondition
import matplotlib.pyplot as plt
import numpy as np
import time

# Page configuration
st.set_page_config(page_title="Optimization Dashboard", layout="wide")

st.title("🚀 Linear Programming Optimization Dashboard")
st.markdown("""
This dashboard is based on the `ex_LP_pyomo.py` model.
Adjust the parameters in the sidebar and click **"Run Optimization"** to see the results.
""")

# --- Sidebar: Inputs ---
st.sidebar.header("🛠 Configuration")

# 1) Solver Selection (glpk and cbc only)
selected_solver = st.sidebar.selectbox("Select Solver", ['glpk', 'cbc'], index=0)

st.sidebar.subheader("Variable Bounds")
max_x = st.sidebar.number_input("Upper bound for x", min_value=1.0, max_value=50.0, value=10.0, step=0.1, format="%.1f")
max_y = st.sidebar.number_input("Upper bound for y", min_value=1.0, max_value=50.0, value=10.0, step=0.1, format="%.1f")

st.sidebar.subheader("Constraints (Right Hand Side)")
rhs1 = st.sidebar.slider("C1: -x + 2y \u2264", min_value=-20.0, max_value=20.0, value=8.0)
rhs2 = st.sidebar.slider("C2: 2x + y \u2264", min_value=0.0, max_value=40.0, value=14.0)
rhs3 = st.sidebar.slider("C3: 2x - y \u2264", min_value=0.0, max_value=30.0, value=10.0)

# 2) Execute Button
execute_button = st.sidebar.button("Run Optimization", type="primary")

# --- Tabs Configuration ---
tab1, tab2 = st.tabs(["📊 Dashboard", "📝 Mathematical Explanation"])

# --- Optimization Logic ---
def solve_optimization(solver_name, b_x, b_y, r1, r2, r3):
    model = pyo.ConcreteModel()
    model.x = pyo.Var(bounds=(0, b_x))
    model.y = pyo.Var(bounds=(0, b_y))
    
    model.C1 = pyo.Constraint(expr= -model.x + 2 * model.y <= r1)
    model.C2 = pyo.Constraint(expr= 2 * model.x + model.y <= r2)
    model.C3 = pyo.Constraint(expr= 2 * model.x - model.y <= r3)
    
    model.obj = pyo.Objective(expr= model.x + model.y, sense=pyo.maximize)
    
    try:
        opt = SolverFactory(solver_name)
        results = opt.solve(model, tee=False)
        
        if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
            return {
                "success": True,
                "x": pyo.value(model.x),
                "y": pyo.value(model.y),
                "obj": pyo.value(model.obj),
                "status": "Optimal Solution Found"
            }
        else:
            return {"success": False, "status": f"No solution found ({results.solver.termination_condition})"}
    except Exception as e:
        return {"success": False, "status": f"Solver Error: {str(e)}"}

# --- Process Execution ---
res = None
if execute_button:
    # Progress Bar
    progress_bar = st.sidebar.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01) # Simulated wait
        progress_bar.progress(percent_complete + 1)
    
    res = solve_optimization(selected_solver, max_x, max_y, rhs1, rhs2, rhs3)
    st.sidebar.success("Execution Complete")

# --- Tab 1: Dashboard ---
with tab1:
    if res and res["success"]:
        st.subheader("Optimization Results")
        col1, col2, col3 = st.columns(3)
        col1.metric("Optimal x", f"{res['x']:.2f}")
        col2.metric("Optimal y", f"{res['y']:.2f}")
        col3.metric("Objective Value Z (x+y)", f"{res['obj']:.2f}")
        st.success(res["status"])
    elif res:
        st.error(res["status"])
    else:
        st.info("Click the **'Run Optimization'** button in the sidebar to start calculations.")

    st.divider()
    
    st.subheader("📈 Visualization of Feasible Region")
    
    def plot_model(b_x, b_y, r1, r2, r3, opt_x=None, opt_y=None):
        x_vals = np.linspace(0, b_x + 2, 400)
        y_vals = np.linspace(0, b_y + 2, 400)
        X, Y = np.meshgrid(x_vals, y_vals)
        
        feasible = (X >= 0) & (X <= b_x) & \
                   (Y >= 0) & (Y <= b_y) & \
                   (-X + 2*Y <= r1) & \
                   (2*X + Y <= r2) & \
                   (2*X - Y <= r3)
        
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Plot constraint lines
        ax.plot(x_vals, (r1 + x_vals) / 2, label=f'-x + 2y = {r1}', color='blue', alpha=0.5)
        ax.plot(x_vals, r2 - 2*x_vals, label=f'2x + y = {r2}', color='green', alpha=0.5)
        ax.plot(x_vals, 2*x_vals - r3, label=f'2x - y = {r3}', color='orange', alpha=0.5)
        
        # Shade feasible region
        ax.imshow(feasible.astype(int), extent=(X.min(), X.max(), Y.min(), Y.max()), 
                  origin="lower", cmap="Blues", alpha=0.3)
        
        # Plot boundaries
        ax.axvline(0, color='black', lw=1)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(b_x, color='gray', linestyle='--', label=f'x limit={b_x}')
        ax.axhline(b_y, color='gray', linestyle='--', label=f'y limit={b_y}')

        if opt_x is not None and opt_y is not None:
            ax.scatter(opt_x, opt_y, color='red', s=150, edgecolors='white', label='Optimal Solution', zorder=5)
        
        ax.set_xlim(0, b_x + 1)
        ax.set_ylim(0, b_y + 1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend(loc='upper right')
        ax.grid(True, linestyle=':', alpha=0.6)
        return fig

    if res and res["success"]:
        fig = plot_model(max_x, max_y, rhs1, rhs2, rhs3, res["x"], res["y"])
        st.pyplot(fig)
    else:
        fig = plot_model(max_x, max_y, rhs1, rhs2, rhs3)
        st.pyplot(fig)

# --- Tab 2: Mathematical Explanation ---
with tab2:
    st.subheader("📝 Model Definition & Explanation")
    
    st.latex(r"""
    \begin{aligned}
    \text{1. Objective Function: } & \text{Maximize } Z = x + y \\
    \text{2. Constraints: } & -x + 2y \le """ + f"{rhs1}" + r""" \\
    & 2x + y \le """ + f"{rhs2}" + r""" \\
    & 2x - y \le """ + f"{rhs3}" + r""" \\
    \text{3. Variable Bounds: } & 0 \le x \le """ + f"{max_x}" + r""" \\
    & 0 \le y \le """ + f"{max_y}" + r" \\" + r"""
    \end{aligned}
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Explanation of Components
    
    #### 1. Objective Function
    - **$Z = x + y$**: This is the value we want to maximize. For example, if $x$ and $y$ represent production quantities of two products, we are trying to maximize their total output.
    
    #### 2. Constraints
    Real-world problems always have limitations. This model has three linear constraints:
    - **Constraint 1 (Blue line)**: $-x + 2y \le RHS$.
    - **Constraint 2 (Green line)**: $2x + y \le RHS$.
    - **Constraint 3 (Orange line)**: $2x - y \le RHS$.
    
    The **shaded blue area (Feasible Region)** represents all possible $(x, y)$ combinations that satisfy every constraint simultaneously.
    
    #### 3. Variable Bounds
    - $x, y \ge 0$ ensures that quantities cannot be negative.
    - The upper bounds (e.g., $x \le 10$) represent the maximum capacity or resource availability for each variable.
    
    #### The Rule of Optimization
    In Linear Programming, the optimal solution always occurs at one of the **vertices (corners)** of the feasible region. This app calculates the exact point where $Z$ is maximized and marks it with a red dot.
    """)

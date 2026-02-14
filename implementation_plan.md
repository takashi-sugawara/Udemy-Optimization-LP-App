# Implementation Plan: Streamlit Optimization App

## 1. Technical Stack
- **Framework**: Streamlit (latest version)
- **Modeling Language**: Pyomo
- **Mathematical Optimization Solvers**: 
    - **GLPK** (Primary default)
    - **CBC** / **SCIP** (Selectable via UI if installed in the environment)
- **Data & Computation**: NumPy
- **Visualization**: Matplotlib
- **Language**: Python 3.x

## 2. Architecture & Design
### 2.1. Component Structure
The application will be built as a single-entry Python script `app.py` to maintain simplicity and ease of deployment. 
- **Optimization Module**: Encapsulates Pyomo model building and solver invocation.
- **Visualization Module**: Logic to calculate intersection points of linear constraints and fill the feasible polygon.
- **UI Module**: Streamlit components for layout and user interaction.

### 2.2. Data Flow
1. User adjusts inputs (sliders/dropdowns) in the Streamlit Sidebar.
2. The `app.py` triggers the optimization logic with new parameters.
3. Pyomo interacts with the selected external solver (GLPK, etc.).
4. Optimization results and constraint functions are passed to the visualization unit.
5. The Main Panel refreshes to display metrics and the Matplotlib plot.

## 3. Key Technical Challenges & Solutions
- **Solver Availability Check**: The app must detect which solvers are actually installed on the user's system to avoid crashing during selection.
- **Feasible Region Plotting**: Handling multiple linear inequalities to find the overlap requires a robust method using `np.linspace` and `np.minimum/maximum` or polygon vertex calculation.
- **Error Handling**: Graceful messaging when the user sets constraints that make the model "Infeasible".

## 4. User Interface Details
- **Sidebar**:
    - **Solver Selection**: A `st.selectbox` containing `['glpk', 'cbc', 'scip', 'highs']`.
    - **Decision Variable Bounds**: `st.number_input` or `st.slider`.
    - **Constraint Parameters**: `st.slider` for RHS of $C1, C2, C3$.
- **Main Panel**:
    - **Top Row**: Three `st.metric` cards for $x$, $y$, and Total Profit ($Z$).
    - **Center**: A high-quality Matplotlib plot showing constraints, the feasible region, and the optimal solution point.
    - **Bottom**: An expander containing the mathematical representation of the problem using LaTeX.

## 5. Deployment & Environment
- Deployment focused on local execution via `streamlit run app.py`.
- Requirements file (`requirements.txt`) should include `streamlit`, `pyomo`, `matplotlib`, and `numpy`.

# Task List: Streamlit Optimization App Implementation

## Phase 1: Environment Setup
- [x] Create `requirements.txt` with `streamlit`, `pyomo`, `matplotlib`, and `numpy`.
- [x] Verify local installation of solvers (`glpk` is mandatory, `cbc`/`scip` optional).

## Phase 2: Core Optimization Logic
- [x] Define a function `solve_model(params, solver_name)` that takes UI inputs and returns the Pyomo results.
- [x] Implement robust solver selection logic with fallbacks/error handling.
- [x] Add logic to check solver availability on the system.

## Phase 3: Visualization Component
- [x] Create a plotting function using Matplotlib to draw constraint lines.
- [x] Implement logic to identify and fill the feasible region polygon.
- [x] Add a marker for the optimal solution point $(x^*, y^*)$.

## Phase 4: UI Development (Streamlit)
- [x] Build the Sidebar with `st.selectbox` for solvers and `st.slider` for variables and constraints.
- [x] Create the Main Panel layout with `st.columns` and `st.metric` for result display.
- [x] Integrate the plotting function into the main UI.
- [x] Add an expander for LaTeX-formatted mathematical model display.

## Phase 5: Testing & Debugging
- [x] Test the app with various constraint values to ensure the graph updates correctly.
- [x] Verify behavior when the model becomes "Infeasible".
- [x] Final UI Polish (labels, units, and layout adjustments).

# Specification: Streamlit Optimization Dashboard

## 1. Project Overview
This project aims to convert a static Pyomo optimization script (`ex_LP_pyomo.py`) into an interactive web application using Streamlit. The app will provide a user-friendly interface for researchers or students to explore Linear Programming (LP) models by adjusting parameters and visualizing the results in real-time.

## 2. User Personas
- **Optimization Students**: Learning how constraints affect the feasible region and optimal solutions.
- **Business Analysts**: Testing "what-if" scenarios for resource allocation based on linear models.

## 3. User Stories
- As a user, I want to see how changing a resource limit (constraint RHS) affects my total profit (objective value).
- As a user, I want a visual representation of the feasible region to understand where the optimal solution lies on the boundary.
- As a user, I want to see the exact numerical values of the decision variables to make informed decisions.

## 4. Functional Requirements
### 4.1. Parameter Configuration (Sidebar)
- **Variable Bounds**: Input fields to set the maximum value for $x$ and $y$ (default range 0 to 10).
- **Constraint Settings**: 
    - Adjust RHS for $C1: -x + 2y \le \text{RHS1}$
    - Adjust RHS for $C2: 2x + y \le \text{RHS2}$
    - Adjust RHS for $C3: 2x - y \le \text{RHS3}$
- **Solve Trigger**: A "Run Optimization" button to execute the Pyomo solver.

### 4.2. Optimization Logic
- Use **Pyomo** to define the model.
- Use **GLPK** (or SCIP) as the underlying solver.
- Handle potential infeasibility gracefully with a user-facing error message.

### 4.3. Results & Visualization (Main Panel)
- **Metrics**: Display $x$, $y$, and the Objective Value ($Z$) using `st.metric`.
- **Plot**: 
    - 2D coordinate system.
    - Lines representing the equations $-x + 2y = \text{RHS1}$, etc.
    - Shaded area representing the feasible region where all constraints are satisfied.
    - A marker indicating the optimal point $(x^*, y^*)$.
- **Model Summary**: A text/LaTeX representation of the mathematical model being solved.

## 5. UI/UX Design
- **Language**: The entire user interface, including labels, metrics, and explanations, must be in **English**.
- **Color Palette**: Modern, professional (Streamlit's default theme with custom primary accent).
- **Layout**: Sidebar for controls, Main area split into "Summary Metrics" at the top and "Visualization" in the center.

## 6. Technical Constraints
- Must be compatible with the local Python environment (Pyomo and GLPK installed).
- Streamlit version 1.30 or higher.
- Matplotlib or Plotly for the graphical components.

## 7. Success Criteria
- The app launches without errors using `streamlit run app.py`.
- Moving a slider updates the graph and the optimization results correctly.
- The visualization accurately reflects the mathematical constraints.

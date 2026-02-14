# Streamlit Optimization Dashboard

An interactive web application built with Streamlit and Pyomo to solve and visualize a Linear Programming (LP) problem. This project was developed as a learning outcome of a mathematical optimization course.

## 🚀 Features
- **Interactive Solvers**: Choose between `GLPK` and `CBC` solvers.
- **Dynamic Parameters**: Adjust decision variable bounds and constraint values through a side menu.
- **Real-time Visualization**: See the feasible region and optimal solution plotted on a 2D graph.
- **Mathematical Insights**: View the underlying mathematical model with clear explanations.

## 🛠 Tech Stack
- **Dashboard**: [Streamlit](https://streamlit.io/)
- **Modeling**: [Pyomo](http://www.pyomo.org/)
- **Computation**: NumPy, Matplotlib
- **Solvers**: GLPK, CBC

## 📦 Installation & Usage

### Prerequisites
Make sure you have Python installed. You also need optimization solvers installed on your system:
- **GLPK**: `brew install glpk` (macOS) or `sudo apt install glpk-utils` (Ubuntu)
- **CBC**: `brew install coin-or-tools/coinor/cbc` (macOS)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/[repository-name].git
   cd [repository-name]
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📝 Credits
This project was developed based on the `ex_LP_pyomo.py` exercise from an optimization course.

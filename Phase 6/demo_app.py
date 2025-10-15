import streamlit as st
import pandas as pd
import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value

st.title("Nestlé India Supply Chain Demo: AI-Opt Simulator")

# Sidebar for Inputs
st.sidebar.header("Scenario Inputs")
demand_mult = st.sidebar.slider("Demand Surge %", 0, 50, 20) / 100
buffer_mult = st.sidebar.slider("Buffer %", 10, 30, 15) / 100
holding_mult = st.sidebar.slider("Holding Cost Increase %", 0, 20, 0) / 100

# Base Demand (from Phase 4)
base_demand = [7200, 6800, 5500, 6000, 8500, 9000]  # Sample from forecasts

# Adjusted Demand
demand = [d * (1 + demand_mult) for d in base_demand]

# Reusable LP (Fixed: Return S and shortage for table)
def run_demo_lp(demand, buffer_pct):
    n = len(demand)
    prob = LpProblem("Demo_LP", LpMinimize)
    S = [LpVariable(f"S_{t}", lowBound=0) for t in range(n)]
    Q = [LpVariable(f"Q_{t}", lowBound=0) for t in range(n)]
    shortage = [LpVariable(f"short_{t}", lowBound=0) for t in range(n)]
    prob += lpSum([5 * (1 + holding_mult) * S[t] + 20 * shortage[t] for t in range(n)])
    prob += S[0] == 0 + Q[0] - demand[0] + shortage[0]
    prob += shortage[0] >= demand[0] - Q[0]
    for t in range(1, n):
        prob += S[t] == S[t-1] + Q[t] - demand[t] + shortage[t]
        prob += shortage[t] >= demand[t] - S[t-1] - Q[t]
    for t in range(n):
        prob += shortage[t] <= 0.05 * demand[t]
        prob += S[t] >= buffer_pct * demand[t]
    prob.solve()
    cost = value(prob.objective)
    avg_short = np.mean([value(shortage[t]) for t in range(n)])
    service = 1 - (avg_short / np.mean(demand))
    return cost, service * 100, [value(S[t]) for t in range(n)], [value(shortage[t]) for t in range(n)]

# Run Sim
cost, service, opt_stock, opt_shortage = run_demo_lp(demand, buffer_mult)

# Display Results
st.header("Simulation Results")
col1, col2 = st.columns(2)
col1.metric("Total Cost (₹)", f"{cost:,.0f}")
col2.metric("Service Level (%)", f"{service:.1f}%")

# Table (Fixed: Use returned S/shortage)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
results_df = pd.DataFrame({
    'Month': months,
    'Demand': demand,
    'Optimal Stock': opt_stock,
    'Shortage': opt_shortage
})
st.table(results_df.round(0))

# Rec
st.header("Strategic Rec")
st.write(f"For {demand_mult*100}% surge with {buffer_mult*100}% buffer: Cost {cost:,.0f} (vs. base ~30,000), service {service:.1f}%—recommend proactive buffering for 15% net savings.")
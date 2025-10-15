# AI-Driven Supply Chain Optimization for Nestlé India

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![ML](https://img.shields.io/badge/ML-Keras%2C%20PuLP-orange)](https://keras.io/)
[![Opt](https://img.shields.io/badge/Opt-LP%2FVRP-green)](https://google.github.io/or-tools/)

## Overview
End-to-end strategy project optimizing Nestlé India's FMCG supply chain (e.g., Maggi) amid seasonal spikes (30% festivals) and logistics delays (15% costs). Used LSTM forecasting (7% MAPE) + LP/VRP for inventory/routing, simulating 15% cost reduction (₹75 Cr annual) at 95% service.

- **Problem**: Demand variability, rural fragmentation (Phase 1 research).
- **Approach**: Data EDA, AI models, opt sims, scenarios (Phases 2-5).
- **Results**: 15% net savings, robust to 20% surges.
- **Demo**: [Streamlit App](phase6/demo_app.py) for what-if (run `streamlit run phase6/demo_app.py`).

## Phases & Learnings
1. **Research & Planning**: Challenges table, SMART objectives (15% cost target).
2. **Data & EDA**: Kaggle FMCG (590 rows), 30% festival uplift plots.
3. **Forecasting**: LSTM tuned to 7% MAPE; comparison table.
4. **Optimization**: LP 50% inventory savings, VRP 10% logistics cut; scenarios +8% surge.
5. **Evaluation**: KPIs 15% net, sensitivity recs (e.g., 25% buffer).
6. **Polish**: This README, report [here](docs/full_report.md), demo app.

## Key Recommendations
1. Deploy LSTM for top 5 products; integrate ERP for auto-replenish (7% accuracy → 20% less stockouts).
2. Adopt 15% buffer EOQ; pilot rural for 50% holding cut (₹300 Cr scale).
3. Multi-hub VRP for quick commerce; save 10% logistics (₹100 Cr amid delays).
4. Dashboard for scenarios; monitor festivals/monsoons (95% service).
5. Scale chain-wide; ESG: 5% waste reduction.

## Resume Bullets
- Led AI-opt project for Nestlé India FMCG, simulating 15% cost reduction (₹75 Cr annual) via LSTM (7% MAPE) and LP/VRP.
- Conducted EDA/sensitivity on Kaggle data, deriving 5 recs for resilience (e.g., 25% festival buffer for 95% service).
- Built interactive Streamlit demo for exec scenarios, showcasing 20% surge mitigation.

## Tech Stack & Setup
- Python, Pandas, Keras, PuLP.
- `pip install -r requirements.txt`
- Run demo: `streamlit run phase6/demo_app.py`

## Limitations
- Deterministic sim; stochastic next.
- Maggi focus; multi-SKU validation.

Fork/Star for your portfolio! Questions? [Your LinkedIn].
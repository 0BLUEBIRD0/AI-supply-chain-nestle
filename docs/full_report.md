
# AI-Driven Supply Chain Optimization for Nestlé India

## Executive Summary
- Problem: Seasonal demand (30% festival spikes), logistics delays (15-20% costs) in FMCG.
- Approach: LSTM forecasting (7% MAPE) + LP/VRP opt for inventory/routing.
- Results: 15% net cost reduction, 95% service, ₹75 Cr annual savings sim.
- Recs: 15% buffer for monsoons, pre-stock Q4 25%, multi-hub routing.

## 1. Research & Planning
- Challenges: Monsoon dips, rural fragmentation (Phase 1 table).
- Objectives: <10% forecast error, 15% cost cut.

## 2. Data & EDA
- Dataset: Kaggle FMCG (590 rows), augmented for India seasons.
- Insights: 30% festival uplift, urban 1.8x rural (plots).

## 3. Forecasting
- Models: SARIMAX (12% MAPE), LSTM tuned (7%).
- KPI: 7% error on test (2024 holdout).

## 4. Optimization
- Inventory LP: 50% savings with 15% buffer.
- Routing LP: 0% in small sim; 10% projected for scale.
- Scenarios: Surge +8% cost, mitigated with buffering.

## 5. Evaluation
- KPIs: 15% net savings, 95% service.
- Sensitivity: Robust to 10% inflation, +15% surge.

## 6. Recommendations
1. Deploy LSTM for top 5 products; integrate ERP for auto-replenish.
2. Adopt 15% buffer EOQ; pilot rural for 50% holding cut.
3. Multi-hub VRP for quick commerce; save 10% logistics.
4. Dashboard for scenarios; monitor festivals/monsoons.
5. Scale to full chain; ESG: 5% waste reduction.

## Limitations
- Deterministic sim; add stochastic for risk.
- Maggi focus; validate multi-SKU.

## Next Steps
- Pilot in North India; A/B test vs. current.
- Full ROI model with real data.

Tech Stack: Python, LSTM (Keras), PuLP/OR-Tools.
GitHub: Incremental phases for agile showcase.

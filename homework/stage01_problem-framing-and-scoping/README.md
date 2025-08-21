
# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
- We want to evaluate whether the current ETF strategy can work effectively next year. This includes forcasting expected returns and understanding associated risks to support investment decisions.

## Stakeholder & User
- Decision owner: PM
- Tool/operator: PM & Investment Analysts

## Useful Answer
- Descriptive / Predictive / Causal: Predictive
- Metric or artifact: Weekly return forcasts with risk bands; visual senario charts; CSV file of predicted returs

## Assumptions & Constraints
- **Assumptions:**
  - Stationarity: ETF returns and strategy characteristics are stable over time
  - Liquidity: The ETF can be easily bought and sold without affecting price
  - Transaction costs: Trading costs are accounted for
  - Capacity: Strategy can handle the intended investment size
- **Constraints:**
  - Benchmark: Which index or portfolio to compare performance against
  - Horizon: Prediction time frame (e.g., weekly, monthly)
  - Evaluation metric: How performance will be measured (e.g., return, risk-adjusted metrics)
  - Others: Investment limits, compliance, or risk restrictions

## Known Unknowns / Risks
- **Market behavior uncertainty:** ETF returns may change due to unexpected market events.  
- **Model risk:** Predictive model might not capture all factors affecting ETF performance. 
- **Data limitations:** Missing or delayed data could affect forecast accuracy.  
- **Strategy capacity:** Large capital inflows might impact liquidity and execution.  

## Lifecycle Mapping
Goal → Stage → Deliverable
- Evaluate whether the ETF strategy will perform next year → Problem Framing & Scoping (Stage 01) → README.md with scoping paragraph

## Repo Plan
/data/, /src/, /notebooks/, /docs/
cadence for updates: Weekly updates after new model runs or analysis; README.md updated after each stage

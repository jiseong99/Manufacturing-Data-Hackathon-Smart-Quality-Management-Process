# Smart Quality Management Process for Injection Molding (사출성형 공정)

A smart quality management pipeline for injection molding that combines **quality-control methodology** (control charts, attribute sampling) with **AI-based inspection**.  
This project proposes a practical approach to optimize **yield (산출율)** and **cost** by introducing **pseudo labeling** for unlabeled process data and training predictive models optimized for **high recall**.

---

## Overview

Injection molding is a mass-production manufacturing method, but it is difficult to **monitor machine/process states in real time** during production, and many factories lack a direct dependent variable (quality label), making data-infrastructure construction expensive and slow.  
To address this, we propose a process that:

- Creates **evidence-based labels** from process signals (Pseudo Labeling)
- Trains an **AI model for pre-inspection (AI 기반 사전 전수 검사)**
- Integrates **sampling inspection policy** (ANSI/ASQ Z1.4-based attribute sampling) to reduce risk and cost

---

## Key Contributions

1. **Optimization targets aligned with manufacturing reality**
   - Uses two practical KPIs: **Yield (산출율)** and **Cost (비용)**

2. **New smart quality management process**
   - Combines traditional QC methods and ML models into one end-to-end workflow

3. **Pseudo Labeling for manufacturing data infrastructure**
   - Generates Normal/Abnormal labels from unlabeled process-only datasets

---

## Data

- Dataset: Injection Molding Predictive Maintenance AI dataset (CSV)
- Size: **26,796,510 rows** total (about **1,030,635 rows × 26 columns**)
- Features: anonymized process signals (temperature, pressure, time, speed, etc.)
- Limitation: **No dependent variable (no quality label)**

---

## Proposed Pipeline

### 1) Pseudo Labeling (Label Generation)

We label the process as Normal/Abnormal using a stricter, control-chart-based approach:

- Compute **moving range (Rm) control chart** for controllable key variables
- Reduce 23 independent variables into a representative variable via **PCA**
- Apply **weighted sum** using correlation with representative variables
- Produce final Normal/Abnormal labels

Focused controllable variables directly related to defects:
- Crack: `Barrel_Temp_Z1~Z4 (℃)`
- Jetting: `Plasticizing_Screw_Velocity (rpm)`
- Flash/Burr: `Cooling_Time (sec)`, `VP_Press (MPa)`, `Back_Flow (MPa)`

### 2) Predictive Model (AI-based Pre-Inspection)

Preprocessing:
- Drop meaningless column(s) (e.g., `No_Shot`)
- `Label Encoding` for nominal identifiers (e.g., Lot)
- `MinMaxScaler` due to different units/ranges across columns

Modeling strategy:
- AutoML with **PyCaret** to benchmark multiple algorithms quickly
- Evaluation metric: **Recall maximization** (minimize Type II risk, β)
- Class imbalance handled via **Under/Over Sampling**
- Model improvement:
  - `GridSearch` parameter tuning
  - **Soft Voting Ensemble**

Class imbalance (example from slides):
- Normal: 1,002,137
- Abnormal: 28,277

---

## Experiments & Results

### A) Label Experiment (Existing labeling vs. Pseudo labeling)

- More strict and evidence-based labeling becomes possible (control-chart driven)
- Pass decisions ~**91% consistent**
- Abnormal lots increased by **74**
- Estimated defect rate becomes **~2.1%**, similar to realistic industrial requirements

### B) Attribute Sampling Experiment (Process comparison)

Sampling policy:
- Based on **ANSI/ASQ Z1.4**
- Inspection level: **General II (GⅡ)** chosen (non-destructive inspection, broader coverage at reasonable cost)

Outcome:
- **Yield improved**: 73% → **79%**
- **Error rate (Type 1&2)** reduced: 16% → **1.5%**

---

## Conclusion

By integrating **QC methods + AI**, this approach:
- Improves credibility and practicality of the solution
- Addresses the “no real-time monitoring” limitation of injection molding
- Contributes to future development of real-time anomaly handling systems in manufacturing analytics

---

## Team

IESC  
- 강민규
- 김우석
- 김한성
- 한지성

---

## Notes

This repository is based on the project presentation:  
**“사출성형 공정을 위한 스마트 품질관리 프로세스”**.

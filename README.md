# Smart Quality Management Process for Injection Molding

A smart quality management pipeline for injection molding that integrates
traditional quality-control methodologies (control charts, attribute sampling)
with machine learning–based inspection to optimize yield and cost under real-world manufacturing constraints.

---

## TL;DR
- Built an end-to-end smart quality management pipeline for injection molding
- Solved the absence of quality labels using control-chart-based pseudo labeling
- Trained recall-optimized predictive models under extreme class imbalance
- Improved yield from **73% → 79%** while reducing error rate from **16% → 1.5%**

---

## Overview
Injection molding is a mass-production manufacturing process, but real-world factories often face the following challenges:

- No real-time monitoring of machine/process states
- No explicit dependent variable (quality labels)
- High cost and latency in building labeled data infrastructure

To address these constraints, this project proposes a practical, deployable pipeline that:

- Generates evidence-based labels from process signals (pseudo labeling)
- Trains AI models for pre-inspection (full population screening)
- Integrates statistical sampling inspection (ANSI/ASQ Z1.4) to reduce risk and cost

---

## Key Contributions

### 1. Optimization Targets Aligned with Manufacturing Reality
- Uses practical KPIs instead of offline accuracy:
  - **Yield** (production output rate)
  - **Cost** (scrap and inspection cost)

### 2. End-to-End Smart Quality Management Pipeline
- Integrates traditional QC methods and ML models into a single workflow
- Designed for deployment under industrial constraints

### 3. Pseudo Labeling for Manufacturing Data Infrastructure
- Generates **Normal / Abnormal** labels from unlabeled, process-only datasets
- Enables supervised learning without costly manual inspection labels

---

## Data

- **Dataset**: Injection Molding Predictive Maintenance AI dataset (CSV)
- **Scale**: 26,796,510 rows total  
  (≈ 1,030,635 samples × 26 features)
- **Features**: Anonymized process signals  
  (temperature, pressure, time, speed, etc.)
- **Limitation**: No dependent variable (no quality label)

---

## Proposed Pipeline

### 1. Pseudo Labeling (Label Generation)

Labels are generated using a strict, control-chart-driven approach:

- Compute moving range (Rm) control charts for key controllable variables
- Reduce 23 independent variables into a representative variable via PCA
- Apply weighted aggregation based on correlation with representative variables
- Produce final **Normal / Abnormal** labels

Focused controllable variables directly linked to defect mechanisms:

- **Crack**: Barrel_Temp_Z1 ~ Z4 (°C)
- **Jetting**: Plasticizing_Screw_Velocity (rpm)
- **Flash / Burr**: Cooling_Time (sec), VP_Press (MPa), Back_Flow (MPa)

---

### 2. Predictive Model (AI-based Pre-Inspection)

#### Preprocessing
- Drop meaningless columns (e.g., `No_Shot`)
- Label encoding for nominal identifiers (e.g., `Lot`)
- MinMax scaling to handle heterogeneous feature ranges

#### Modeling Strategy
- AutoML benchmarking using **PyCaret**
- Primary evaluation metric: **Recall**
  - Minimize Type II error (β-risk)
- Handle severe class imbalance via under/over sampling

#### Model Improvement
- GridSearch-based hyperparameter tuning
- Soft voting ensemble

Class distribution example:
- Normal: 1,002,137
- Abnormal: 28,277

---

## Experiments & Results

### A. Labeling Experiment  
(Existing heuristic labeling vs. proposed pseudo labeling)

- Control-chart-driven labeling is stricter and more evidence-based
- Pass decisions ≈ **91% consistent**
- Abnormal lots increased by **+74**
- Estimated defect rate ≈ **2.1%**, aligned with realistic industrial requirements

---

### B. Attribute Sampling Experiment  
(Process comparison)

- Sampling policy based on **ANSI/ASQ Z1.4**
- Inspection level: **General II (GII)**
  - Non-destructive inspection
  - Balanced coverage and cost

**Outcome**
- Yield improved: **73% → 79%**
- Error rate (Type I & II): **16% → 1.5%**

---

## Conclusion

By integrating quality-control theory with machine learning, this approach:

- Improves credibility and deployability of AI solutions in manufacturing
- Addresses the absence of real-time monitoring and labeled data
- Provides a foundation for future real-time anomaly handling systems

---

## Why This Project Matters
This project emphasizes applying machine learning under real-world manufacturing constraints:

- No ground-truth labels
- Extreme class imbalance
- High cost of false negatives
- Operational KPIs prioritized over offline accuracy

Rather than optimizing theoretical performance, the pipeline focuses on
**robustness, interpretability, and operational impact**, making it well-suited
for deployment-oriented ML and MLOps roles.

---

## Team
IESC  
- Min-Gyu Kang  
- Woo-Seok Kim  
- Han-Seong Kim  
- **Ji-Seong Han**

---

## Notes
This repository is based on the project presentation:

**“Smart Quality Management Process for Injection Molding”**  
(original presentation materials are in Korean)

An English summary of the methodology and results is provided in this README.

# ARSI: Agentic Road Safety Intelligence
Track 1: Agentic AI 

## 🚀 Overview
ARSI is a decentralized multi-agent system built to solve the "Static Map Gap." Using **Gemini 1.5 Flash**, it transforms user-reported hazards into verified, risk-assessed navigation data. The system doesn't just show a map; it **reasons** about whether a pothole is a threat to a bike versus a car.

## 📺 System Simulation Demo
> **Visualizing the Multi-Agent Pipeline in Action**

[Screenshot_demo]https://github.com/Lakshmi98496/ARSI-Agentic-Road-Safety/commit/f91e4fea111c99eec26091dd78788b0d29209f5d

*The screenshot above demonstrates the transition from a user report to Agentic validation and the final severity calculation pushed to the rider's HUD.*

## 🧠 The Agentic Brain
* **Validation Agent:** Filters noise and malicious reports using truth-score logic.
* **Risk Reasoning Agent:** Uses Gemini 1.5 Flash to calculate situational severity based on vehicle dynamics ($S = (H \times V) / P$).
* **Lifecycle Agent:** Employs temporal decay ($V_{t} = V_{0} \cdot e^{-\lambda t}$) to ensure the map remains self-healing.

## 🛠️ Technical Stack
* **LLM:** Gemini 1.5 Flash (Agentic Orchestration)
* **Database:** PostGIS & Firebase for Spatial Indexing
* **Simulation:** Python-based Multi-Agent Framework
* **Frontend:** Flutter HUD Prototype

## 📂 Project Structure
* `arsi_simulation.py`: Core logic for the Agentic Pipeline simulation.
* `README.md`: Documentation and Architecture Overview.

---
**Submission for Track 1: Agentic AI**

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00e5ff&height=200&section=header&text=Project%20PRAVAH&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Smart%20India%20Hackathon%202026%20%7C%20Oil%20India%20Limited&descAlignY=55&descAlign=50" />

### **AI-Powered Real-Time Measurement Across Channels**
*Next-Generation Drilling Intelligence & Hazard Prevention System*

[![SIH 2026](https://img.shields.io/badge/SIH_2026-PS_SIH26121-FF9900?style=for-the-badge&logo=hackaday&logoColor=white)](#)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](#)
[![Status: Active Development](https://img.shields.io/badge/Status-Active_Development-00e5ff?style=for-the-badge)](#)

---
</div>

## 🌐 Vision

**Project PRAVAH** (formerly eRTMAC-NWIS) bridges the critical gap between live drilling telemetry and decades of undocumented institutional memory. By transforming unstructured Daily Drilling Reports (DDRs) into a dynamic Knowledge Graph and pairing it with live sensor anomaly detection, PRAVAH acts as an **AI Copilot for Drilling Engineers**, capable of predicting hazards like stuck pipe and mud loss before they escalate.

> **"From raw data monitoring to evidence-grounded intelligence."**

---

## 🏗️ Architecture & Modules

PRAVAH is built on a modular, microservice-inspired architecture. Each module handles a critical segment of the intelligence pipeline.

<details open>
<summary><b>🧩 Module 1: Data Foundation & NLP (Historical Memory)</b></summary>
Extracts structured 18-class hazard events from unstructured natural language Daily Drilling Reports (DDRs) using specialized NLP. It transforms decades of text logs into a highly queryable event database.
</details>

<details open>
<summary><b>🌍 Module 2: Geospatial AHP Similarity (Who is Relevant?)</b></summary>
Uses the Analytic Hierarchy Process (AHP) to calculate multi-dimensional offset well similarity. It evaluates geographic distance, trajectory shape (FastDTW), BHA mechanical configurations, and formation stratigraphy to find truly relevant historical analogs.
</details>

<details open>
<summary><b>⚡ Module 3: Real-Time Telemetry & Anomaly Detection</b></summary>
Ingests live rig telemetry (simulated WITSML feed) and runs **Dual-Algorithm Detection** (Rolling Z-Score for transients, Recursive CUSUM for slow drift). Aligns live sequences against historical failures using the Smith-Waterman algorithm to generate early warnings.
</details>

<details open>
<summary><b>🕸️ Module 4: Knowledge Graph & GraphRAG (The Copilot)</b></summary>
A visually stunning, interactive 3D Knowledge Graph built on Neo4j/NetworkX. Features **GraphRAG Evidence Retrieval**, allowing engineers to query the graph naturally and receive highly cited, evidence-backed answers about past formation hazards and successful interventions.
</details>

<details open>
<summary><b>🤖 Module 5: Engineering Agent (Command Center)</b></summary>
A high-tech conversational interface that acts as the overarching intelligence layer. Engineers can chat with PRAVAH to synthesize data across all modules, generate pre-spud risk briefings, and retrieve real-time telemetry analytics.
</details>

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PowerShell (for Windows environments)
- Git

### Installation & Launch
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yug210705/Project-Pravah.git
   cd Project-Pravah
   ```

2. **Launch the Gateway:**
   We provide a one-click PowerShell launcher that automatically handles virtual environment creation, dependency installation, and starts the unified API Gateway and all 5 micro-modules.
   ```powershell
   .\start_all.ps1
   ```

3. **Access the Dashboard:**
   Open your browser and navigate to the unified command center:
   👉 `http://localhost:5000`

---

## 🔬 Core Technologies

| Category | Technologies Used |
|----------|-------------------|
| **Backend & APIs** | FastAPI, Uvicorn, Python, Pandas, NumPy |
| **Frontend UI** | HTML5, CSS Grid, Vanilla JS, Glassmorphism UI |
| **AI & NLP** | HuggingFace, Gemini/Qwen LLM Integrations, LangChain |
| **Graph & Search** | NetworkX, ChromaDB (Vector Store), GraphRAG |
| **Algorithms** | Smith-Waterman Sequence Alignment, FastDTW, CUSUM, AHP |

---

## 📊 Impact & Backtest Results

During our time-travel backtest on the real Equinor Volve WITSML dataset (Well 15/9-F-9A), PRAVAH demonstrated:
- 🚨 **+106.48 meters** of early warning before a confirmed stuck pipe incident.
- ⏱️ **~44 minutes** of actionable lead time at standard rate of penetration.
- 📉 **Zero data leakage**, utilizing only data available prior to the incident timestamp.

---

## 🤝 Contribution Guidelines

This project is actively developed for SIH 2026. 
1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

*Please ensure no sensitive API keys or `.env` files are committed to the repository.*

<div align="center">
<br/>

**Built with 💻 and ☕ by Team PRAVAH**

</div>

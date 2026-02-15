AI-Driven Intelligent Grievance Management System

A microservice-based AI-assisted grievance management system with enforced Human-in-the-Loop (HITL) execution control.

---

Project Overview

This system intelligently analyzes user complaints using semantic similarity (SBERT embeddings) and enforces structured decision control through a backend execution layer.

The AI does not autonomously decide outcomes. Instead, it generates confidence signals that trigger controlled execution logic in the backend.

---

Architecture

Frontend → Backend (HITL Enforcement) → AI Service (Semantic Validation)

Core Contribution
Enforced Human-in-the-Loop (HITL) execution control mechanism driven by AI confidence thresholds.

AI Role
- Semantic complaint validation
- Department suggestion
- Confidence scoring

Backend Role
- Enforces execution control
- Blocks or approves submission based on AI confidence
- Prevents unsafe automated routing

---

Project Structure

Ai-Grievance-System/
│
├── ai-service/ # FastAPI AI microservice
│ ├── app.py
│ ├── model.py
│ └── requirements.txt
│
├── backend/ # Node.js Express server
│ ├── server.js
│ └── routes/
│
├── frontend/ # Simple UI
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md

---

Tech Stack

- Python (FastAPI)
- SentenceTransformers (SBERT)
- Node.js (Express)
- HTML / CSS / JavaScript
- REST API Architecture

---

How It Works

1. User submits complaint.
2. Backend sends complaint to AI microservice.
3. AI computes semantic similarity against department prototypes.
4. AI returns:
   - Suggested department
   - Confidence score
   - Confidence level
   - HITL flag
5. Backend enforces decision:

| Confidence | Action |
|------------|---------|
| HIGH       | Approved |
| MEDIUM     | Requires Confirmation |
| LOW        | Blocked |

Project Status

This project is currently under active development.

The current version demonstrates:
- AI-powered semantic validation
- Human-in-the-Loop execution control
- Backend enforcement logic
- Basic frontend interface

Further improvements and production-level enhancements will be added in future updates.

---

Upcoming Enhancements

- Database integration (MongoDB/PostgreSQL)
- Authentication & Role-Based Access Control
- Admin Dashboard
- Complaint Tracking System
- Deployment (Docker / Cloud Hosting)
- Logging & Audit Trail



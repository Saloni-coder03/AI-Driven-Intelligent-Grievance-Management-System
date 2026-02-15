from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import Dict


# Load SBERT Model (Lightweight + Production Stable)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Department Knowledge Base (Concept Prototypes)
DEPARTMENTS = {
    "Academics": "Issues related to exams, grading, attendance, internal marks, course registration, timetable, certificates, internships, placements.",
    "Administrative": "Issues related to finance, scholarships, documentation, DSW, administrative approvals.",
    "Hostel": "Complaints about hostel rooms, mess food, maintenance, security, wifi, cleanliness.",
    "Technical": "Complaints related to system errors, portals, login problems, lab equipment, technical infrastructure."
}

# Precompute Department Embeddings (Optimization)
department_embeddings = {
    name: model.encode(description)
    for name, description in DEPARTMENTS.items()
}

# Confidence Thresholds (Can Be Made Configurable)
HIGH_THRESHOLD = 0.75
MEDIUM_THRESHOLD = 0.55


# Core Semantic Analysis Function
def analyze_complaint(text: str) -> Dict:
    """
    Perform semantic validation of complaint text.

    Returns:
        {
            suggested_department: str,
            confidence_score: float,
            confidence_level: str,
            hitl_required: bool,
            advisory_message: str
        }
    """

    complaint_embedding = model.encode(text)

    best_department = None
    highest_score = -1.0

    
    # Concept–Prototype Validation
    for dept, dept_embedding in department_embeddings.items():
        score = cosine_similarity(
            [complaint_embedding],
            [dept_embedding]
        )[0][0]

        if score > highest_score:
            highest_score = score
            best_department = dept

    confidence_score = round(float(highest_score), 4)

    # Confidence-Driven Control Flow
    if confidence_score >= HIGH_THRESHOLD:
        confidence_level = "HIGH"
        hitl_required = False
        advisory_message = "High confidence match. Normal processing allowed."

    elif confidence_score >= MEDIUM_THRESHOLD:
        confidence_level = "MEDIUM"
        hitl_required = True
        advisory_message = (
            "Moderate confidence detected. "
            "User confirmation recommended before submission."
        )

    else:
        confidence_level = "LOW"
        hitl_required = True
        advisory_message = (
            "Low confidence match. Manual verification required before submission."
        )

    # Structured AI Response
    return {
        "suggested_department": best_department,
        "confidence_score": confidence_score,
        "confidence_level": confidence_level,
        "hitl_required": hitl_required,
        "advisory_message": advisory_message
    }

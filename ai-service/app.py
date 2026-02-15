from fastapi import FastAPI
from pydantic import BaseModel
from model import analyze_complaint

# Create FastAPI app instance
app = FastAPI(
    title="AI Grievance Service",
    description="Semantic complaint validation using SBERT embeddings",
    version="1.0"
)

# Request schema for incoming complaints
class ComplaintRequest(BaseModel):
    text: str

# Health check endpoint
@app.get("/")
def health_check():
    return {
        "status": "AI Service is running"
    }

# Complaint analysis endpoint
@app.post("/predict")
def predict_complaint(request: ComplaintRequest):
    """
    Analyze complaint text and return:
    - Suggested department
    - Confidence score
    - Confidence level
    - HITL requirement flag
    """

    complaint_text = request.text

    # Call semantic analysis function from model.py
    result = analyze_complaint(complaint_text)

    return result

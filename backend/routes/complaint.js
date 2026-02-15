// Complaint submission route
const express = require("express");
const axios = require("axios");

const router = express.Router();

// POST /api/submit-complaint
router.post("/submit-complaint", async (req, res) => {
    try {
        const { text, selectedDepartment } = req.body;

        if (!text || !selectedDepartment) {
            return res.status(400).json({
                message: "Complaint text and selected department are required"
            });
        }

        // Step 1: Call AI Service
        const aiResponse = await axios.post(
            "http://127.0.0.1:8000/predict",
            { text }
        );

        const analysis = aiResponse.data;

        const {
            suggested_department,
            confidence_level,
            confidence_score,
            hitl_required
        } = analysis;

        // Step 2: HITL Enforcement Logic
        
        // Case 1: High confidence → Allow submission
        if (confidence_level === "HIGH" && !hitl_required) {
            return res.json({
                status: "APPROVED",
                message: "Complaint submitted successfully",
                ai_analysis: analysis
            });
        }

        // Case 2: Medium confidence → Require user confirmation
        if (confidence_level === "MEDIUM") {
            return res.json({
                status: "REQUIRES_CONFIRMATION",
                message: "AI confidence is moderate. Please confirm department selection.",
                ai_suggestion: suggested_department,
                confidence_score
            });
        }

        // Case 3: Low confidence → Hard block
        if (confidence_level === "LOW") {
            return res.json({
                status: "BLOCKED",
                message: "Low AI confidence. Manual review required before submission.",
                ai_suggestion: suggested_department,
                confidence_score
            });
        }

        // Fallback
        return res.json({
            status: "UNKNOWN",
            message: "Unexpected confidence state",
            ai_analysis: analysis
        });

    } catch (error) {
        console.error(error.message);
        return res.status(500).json({
            message: "Error processing complaint"
        });
    }
});

module.exports = router;

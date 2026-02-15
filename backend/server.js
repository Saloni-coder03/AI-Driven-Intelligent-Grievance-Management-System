//Human-in-the-Loop (HITL) execution control layer 
const express = require("express");
const cors = require("cors");

const complaintRoutes = require("./routes/complaint");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use("/api", complaintRoutes);

// Health check
app.get("/", (req, res) => {
    res.json({ message: "Backend server running" });
});

const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Backend running on http://localhost:${PORT}`);
});

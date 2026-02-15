const form = document.getElementById("complaintForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const complaint = document.getElementById("complaint").value;

    try {
        const response = await fetch("http://localhost:5000/api/complaint", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, email, complaint })
        });

        const data = await response.json();

        document.getElementById("responseMessage").innerText =
            "Complaint submitted successfully!";
        
        form.reset();

    } catch (error) {
        document.getElementById("responseMessage").innerText =
            "Error submitting complaint.";
    }
});

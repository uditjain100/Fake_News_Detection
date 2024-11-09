document.getElementById("newsForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const newsText = document.getElementById("newsInput").value;
    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: newsText })
    });
    
    const result = await response.json();
    document.getElementById("result").textContent = `Prediction: ${result.prediction}`;
});

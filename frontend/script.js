document.getElementById('asteroid-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form data
    const formData = new FormData(this);

    // Convert form data to JSON
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    // Send a POST request to the server with the form data
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result
        const predictionResult = document.getElementById('prediction-result');
        predictionResult.innerHTML = `Danger level: ${data.result}`;
    })
    .catch(error => console.error('Error:', error));
});
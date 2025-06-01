let pieChartInstance = null;

document.getElementById('ckdForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = {};

  for (let [key, value] of formData.entries()) {
    data[key] = parseFloat(value);
  }

  fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    const resultDiv = document.getElementById('result');
    let predictionText = "";
    let predictionColor = "";
    let predictionValue = 0;

    if (result.prediction === 1) {
      predictionText = "Prediction: Chronic Kidney Disease Detected.";
      predictionColor = "red";
      predictionValue = 1;
    } else if (result.prediction === 0) {
      predictionText = "Prediction: No Chronic Kidney Disease.";
      predictionColor = "green";
      predictionValue = 0;
    } else if (result.error) {
      predictionText = "Error: " + result.error;
      predictionColor = "red";
    } else {
      predictionText = "Unexpected response from server.";
      predictionColor = "red";
    }

    resultDiv.textContent = predictionText;
    resultDiv.style.color = predictionColor;

    if (result.prediction === 0 || result.prediction === 1) {
      renderPieChart(data, predictionValue);
    }
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('result').textContent = "An error occurred.";
  });
});


function renderPieChart(data, prediction) {
  // Select some key inputs for visualization - you can change or add more
  // We'll normalize values for better pie proportions
  
  // Max values to normalize inputs roughly (you can adjust)
  const maxVals = {
    age: 100,
    bp: 200,
    al: 5,
    hemo: 20,
  };

  // Normalize values (0 to 1 scale)
  const age = Math.min(data.age / maxVals.age, 1);
  const bp = Math.min(data.bp / maxVals.bp, 1);
  const al = Math.min(data.al / maxVals.al, 1);
  const hemo = Math.min(data.hemo / maxVals.hemo, 1);

  // Data for the pie: inputs + prediction slice (weight 1 or 0)
  // To visualize prediction we add a slice labeled CKD Detected or Not
  const pieData = [
    age,
    bp,
    al,
    hemo,
    1 // prediction slice weight = 1 for visibility
  ];

  const labels = [
    `Age (${data.age})`,
    `Blood Pressure (${data.bp})`,
    `Albumin (${data.al})`,
    `Hemoglobin (${data.hemo})`,
    prediction === 1 ? "CKD Detected" : "No CKD"
  ];

  const colors = [
    '#4caf50', // green for age
    '#2196f3', // blue for BP
    '#ff9800', // orange for Albumin
    '#9c27b0', // purple for Hemoglobin
    prediction === 1 ? '#f44336' : '#8bc34a' // red if CKD else light green
  ];

  const ctx = document.getElementById('pieChart').getContext('2d');

  if (pieChartInstance) {
    pieChartInstance.destroy();
  }

  pieChartInstance = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        data: pieData,
        backgroundColor: colors,
        borderColor: '#fff',
        borderWidth: 2,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom'
        },
        title: {
          display: true,
          text: 'Input Values and Prediction Visualization'
        }
      }
    }
  });
}

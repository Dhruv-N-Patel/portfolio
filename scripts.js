document.querySelectorAll('.remove-btn').forEach(button => {
    button.addEventListener('click', () => {
        alert('Remove action triggered');
    });
});

document.querySelectorAll('.add-btn').forEach(button => {
    button.addEventListener('click', () => {
        alert('Add action triggered');
    });
});

document.querySelector('.process-btn').addEventListener('click', () => {
    alert('Processing simulation...');
});

// Add a chart using Chart.js for the Historic Analysis
const ctx = document.getElementById('historicChart').getContext('2d');
const historicChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Average Distance to Provider',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

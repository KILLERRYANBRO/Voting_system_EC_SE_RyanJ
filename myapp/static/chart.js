document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('voteChart').getContext('2d');
  const voteChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: window.chartData.names,
      datasets: [{
        label: 'Votes',
        data: window.chartData.votes,
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          precision: 0
        }
      }
    }
  });
});

const boyData = window.chartData.boys;
const girlData = window.chartData.girls;

let boyChart, girlChart;

function renderCharts() {
  const boyCtx = document.getElementById('boyChart').getContext('2d');
  const girlCtx = document.getElementById('girlChart').getContext('2d');

  boyChart = new Chart(boyCtx, {
    type: 'bar',
    data: {
      labels: boyData.names,
      datasets: [{
        label: 'Boy Votes',
        data: boyData.votes,
        backgroundColor: 'deepskyblue'
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true, ticks: { precision: 0 } }
      }
    }
  });

  girlChart = new Chart(girlCtx, {
    type: 'bar',
    data: {
      labels: girlData.names,
      datasets: [{
        label: 'Girl Votes',
        data: girlData.votes,
        backgroundColor: 'hotpink'
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true, ticks: { precision: 0 } }
      }
    }
  });
}

// Function to toggle between chart displays
function showChart(gender) {
  if (gender === 'boy') {
    document.getElementById('boyChartContainer').style.display = 'block';
    document.getElementById('girlChartContainer').style.display = 'none';
  } else {
    document.getElementById('boyChartContainer').style.display = 'none';
    document.getElementById('girlChartContainer').style.display = 'block';
  }
}

// Render charts when DOM is ready
document.addEventListener('DOMContentLoaded', renderCharts);

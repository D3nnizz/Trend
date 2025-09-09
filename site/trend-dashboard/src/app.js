const dropdown = document.getElementById('timeframe-dropdown');
const chartContainer = document.getElementById('chart-container');
let chart;

const loadCSV = async (file) => {
    const response = await fetch(`data/${file}`);
    const data = await response.text();
    return parseCSV(data);
};

const parseCSV = (data) => {
    const rows = data.split('\n').slice(1);
    return rows.map(row => {
        const columns = row.split(',');
        return {
            time: columns[0],
            value: parseFloat(columns[1])
        };
    });
};

const updateChart = async (file) => {
    const data = await loadCSV(file);
    const labels = data.map(entry => entry.time);
    const values = data.map(entry => entry.value);

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(chartContainer, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Trend Data',
                data: values,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};

const init = () => {
    const files = [
        'trend_15m.csv',
        'trend_1h.csv',
        'trend_30m.csv',
        'trend_3m.csv',
        'trend_5m.csv'
    ];

    files.forEach(file => {
        const option = document.createElement('option');
        option.value = file;
        option.textContent = file.replace('.csv', '').replace('_', ' ');
        dropdown.appendChild(option);
    });

    dropdown.addEventListener('change', (event) => {
        updateChart(event.target.value);
    });

    updateChart(files[0]); // Load the first file by default
};

document.addEventListener('DOMContentLoaded', init);
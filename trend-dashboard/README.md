# Trend Dashboard

## Overview
The Trend Dashboard is a web application that visualizes time series data from various CSV files. Users can select different timeframes from a dropdown menu to dynamically update the chart displayed on the dashboard.

## Project Structure
```
trend-dashboard
├── src
│   ├── index.html        # Main HTML document for the dashboard
│   ├── app.js            # JavaScript code for loading data and rendering charts
│   ├── styles.css        # CSS styles for the dashboard layout and design
│   └── data              # Folder containing CSV data files
│       ├── trend_15m.csv # Time series data for 15-minute intervals
│       ├── trend_1h.csv  # Time series data for 1-hour intervals
│       ├── trend_30m.csv # Time series data for 30-minute intervals
│       ├── trend_3m.csv  # Time series data for 3-minute intervals
│       └── trend_5m.csv  # Time series data for 5-minute intervals
├── package.json          # npm configuration file with project dependencies
└── README.md             # Documentation for the project
```

## Getting Started

### Prerequisites
- Node.js and npm installed on your machine.

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd trend-dashboard
   ```
3. Install the required dependencies:
   ```
   npm install
   ```

### Running the Dashboard
1. Open the `src/index.html` file in your web browser.
2. Use the dropdown menu to select a timeframe and view the corresponding data in the chart.

## Features
- Dynamic chart rendering based on selected CSV data.
- User-friendly interface with a dropdown menu for easy navigation between different timeframes.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
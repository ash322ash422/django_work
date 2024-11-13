// src/App.js
import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

const DataVisualization = () => {
  const [scatterData, setScatterData] = useState([]);
  const [lineData, setLineData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      // const response = await axios.get('http://127.0.0.1:8000/api/data/');
      const response = await axios.get('http://127.0.0.1:8000/api/data/random_variation/');
      const data = response.data;
      
      // Process data for scatter plot
      setScatterData([{
        x: data.scatter_data.x,
        y: data.scatter_data.y,
        mode: 'markers',
        type: 'scatter',
        marker: {
          color: 'rgb(51, 204, 204)',
          size: 10,
        },
        name: 'Scatter Plot'
      }]);

      // Process data for line graph
      setLineData([{
        x: data.line_data.x,
        y: data.line_data.y,
        type: 'scatter',
        mode: 'lines',
        line: {
          color: 'rgb(255, 127, 80)',
          width: 2
        },
        name: 'Line Graph'
      }]);

      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
      console.error('Error fetching data:', err);
    }
  };

  useEffect(() => {
    // Initial fetch
    fetchData();

    // Set up interval for periodic refresh
    const intervalId = setInterval(() => {
      fetchData();
    }, 10000); // 10000 milliseconds = 10 seconds

    // Cleanup function to clear interval when component unmounts
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array means this effect runs once on mount

  if (loading) return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-xl font-semibold">Loading data...</div>
    </div>
  );
  
  if (error) return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-xl font-semibold text-red-600">
        Error: {error}
      </div>
    </div>
  );

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Data Visualization Dashboard(Refreshes every 10 sec)</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Scatter Plot</h2>
          <Plot
            data={scatterData}
            layout={{
              width: 600,
              height: 400,
              title: 'Scatter Plot Analysis',
              xaxis: { title: 'X Value' },
              yaxis: { title: 'Y Value' },
              margin: { t: 40 }
            }}
            config={{ responsive: true }}
          />
        </div>

        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Line Graph</h2>
          <Plot
            data={lineData}
            layout={{
              width: 600,
              height: 400,
              title: 'Trend Analysis',
              xaxis: { title: 'X Value' },
              yaxis: { title: 'Value' },
              margin: { t: 40 }
            }}
            config={{ responsive: true }}
          />
        </div>
      </div>

      {/* Debug section - uncomment if needed */}
      {/* <div className="mt-8 p-4 bg-gray-100 rounded">
        <h3 className="text-lg font-semibold mb-2">Debug Information:</h3>
        <pre className="whitespace-pre-wrap">
          {JSON.stringify({
            scatterData: scatterData[0],
            lineData: lineData[0]
          }, null, 2)}
        </pre>
      </div> */}
    </div>
  );
};

export default DataVisualization;
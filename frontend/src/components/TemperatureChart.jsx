import React from 'react';
import { Box, Heading, Text, Spinner } from '@chakra-ui/react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, Filler);

const TemperatureChart = ({ data, loading }) => {
  if (loading) {
    return (
      <Box bg="gray.800" p={8} borderRadius="2xl" textAlign="center" h="500px">
        <Spinner size="xl" color="blue.500" />
      </Box>
    );
  }

  // Get data from API
  const historicalYears = data?.historical_years || [];
  const historicalTemps = data?.historical_temps || [];
  const futureYears = Array.from({ length: 26 }, (_, i) => 2025 + i);
  const futureTemps = data?.future_predictions || [];

  console.log('Chart Data:', { 
    historicalYears: historicalYears.length, 
    historicalTemps: historicalTemps.length,
    futureYears: futureYears.length,
    futureTemps: futureTemps.length
  });

  // Create datasets
  const historicalDataArray = [...historicalTemps, ...Array(26).fill(null)];
  const futureDataArray = [...Array(historicalYears.length).fill(null), ...futureTemps];

  const chartData = {
    labels: [...historicalYears, ...futureYears],
    datasets: [
      {
        label: 'Historical Data',
        data: historicalDataArray,
        borderColor: '#06b6d4',
        backgroundColor: 'rgba(6, 182, 212, 0.2)',
        borderWidth: 4,
        fill: true,
        tension: 0.4,
        pointRadius: 4,
        pointHoverRadius: 8,
        pointBackgroundColor: '#06b6d4',
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      },
      {
        label: 'AI Prediction',
        data: futureDataArray,
        borderColor: '#ef4444',
        backgroundColor: 'rgba(239, 68, 68, 0.2)',
        borderWidth: 4,
        borderDash: [10, 5],
        fill: true,
        tension: 0.4,
        pointRadius: 4,
        pointHoverRadius: 8,
        pointBackgroundColor: '#ef4444',
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      }
    ]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: { 
          color: '#e2e8f0', 
          padding: 20, 
          font: { size: 14, weight: '600' },
          usePointStyle: true,
          pointStyle: 'circle'
        }
      },
      tooltip: {
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        titleColor: '#60a5fa',
        bodyColor: '#e2e8f0',
        borderColor: '#3b82f6',
        borderWidth: 2,
        padding: 16,
        displayColors: true,
        titleFont: { size: 16, weight: 'bold' },
        bodyFont: { size: 14 },
        callbacks: {
          label: function(context) {
            return context.dataset.label + ': ' + context.parsed.y.toFixed(2) + '°C';
          }
        }
      }
    },
    scales: {
      x: {
        grid: { 
          color: 'rgba(148, 163, 184, 0.1)',
          drawBorder: false
        },
        ticks: { 
          color: '#94a3b8', 
          maxTicksLimit: 12, 
          font: { size: 12 },
          maxRotation: 45,
          minRotation: 45
        },
        title: {
          display: true,
          text: 'Year',
          color: '#94a3b8',
          font: { size: 14, weight: 'bold' }
        }
      },
      y: {
        grid: { 
          color: 'rgba(148, 163, 184, 0.1)',
          drawBorder: false
        },
        ticks: { 
          color: '#94a3b8', 
          font: { size: 12 },
          callback: function(value) {
            return value + '°C';
          }
        },
        title: {
          display: true,
          text: 'Temperature (°C)',
          color: '#94a3b8',
          font: { size: 14, weight: 'bold' }
        },
        min: 13,
        max: 18,
        beginAtZero: false
      }
    },
    interaction: { 
      intersect: false, 
      mode: 'index',
      axis: 'x'
    },
    elements: {
      line: {
        tension: 0.4
      },
      point: {
        radius: 4,
        hoverRadius: 8
      }
    }
  };

  return (
    <Box 
      bg="gray.800" 
      p={8} 
      borderRadius="2xl" 
      border="2px" 
      borderColor="blue.500/30"
      boxShadow="0 10px 40px rgba(59, 130, 246, 0.2)"
    >
      <Heading size="lg" mb={6} color="blue.400" display="flex" alignItems="center">
        📈 Temperature Anomaly Projection (1850 - 2050)
      </Heading>
      <Box h="500px" position="relative">
        <Line data={chartData} options={options} />
      </Box>
      <Box mt={6} display="flex" gap={8} fontSize="sm" justifyContent="center" flexWrap="wrap">
        <Box display="flex" alignItems="center" gap={3} p={3} bg="cyan.900/20" borderRadius="lg" border="1px" borderColor="cyan.500/30">
          <Box w="40px" h="4px" bg="cyan.500" borderRadius="full" />
          <Text color="cyan.400" fontWeight="600">Historical Data (1850-2024)</Text>
        </Box>
        <Box display="flex" alignItems="center" gap={3} p={3} bg="red.900/20" borderRadius="lg" border="1px" borderColor="red.500/30">
          <Box w="40px" h="4px" bg="red.500" borderRadius="full" borderStyle="dashed" />
          <Text color="red.400" fontWeight="600">AI Prediction (2025-2050)</Text>
        </Box>
      </Box>
    </Box>
  );
};

export default TemperatureChart;
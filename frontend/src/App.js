import React, { useState, useEffect } from 'react';
import { Box, Grid, Heading, Container, VStack, SimpleGrid, Text } from '@chakra-ui/react';
import { WiThermometer, WiCloud, WiRaindrops, WiStrongWind } from 'react-icons/wi';
import Dashboard from './components/Dashboard';
import TemperatureChart from './components/TemperatureChart';
import CitySelector from './components/CitySelector';
import HinglishChatbot from './components/HinglishChatbot';
import PredictionPanel from './components/PredictionPanel';

const API_URL = 'https://climate-backend-mxw4.onrender.com';

function App() {
  const [climateData, setClimateData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchClimateData();
  }, []);

  const fetchClimateData = async () => {
    try {
      const response = await fetch(`${API_URL}/api/climate-data`);
      const data = await response.json();
      setClimateData(data);
      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setLoading(false);
    }
  };

  return (
    <Box bg="linear-gradient(135deg, #0f172a 0%, #1e293b 100%)" minH="100vh" color="white" pb={8}>
      <Box bg="rgba(15, 23, 42, 0.95)" borderBottom="3px" borderColor="blue.500/50" py={8} mb={6}>
        <Container maxW="container.xl">
          <VStack spacing={3} textAlign="center">
            <Heading fontSize="3xl" bgGradient="linear(to-r, blue.400, cyan.400)" bgClip="text">
              🌍 Climate Intelligence Hub
            </Heading>
            <Text fontSize="md" color="gray.300">AI-Powered Climate Prediction</Text>
          </VStack>
        </Container>
      </Box>

      <Container maxW="container.xl" px={4}>
        <SimpleGrid columns={{ base: 2, md: 4 }} gap={6} mb={8}>
          <StatCard icon={WiThermometer} title="Global Temp" value={`${climateData?.current_temp || 15.14}°C`} color="cyan" />
          <StatCard icon={WiCloud} title="2050 Forecast" value={`${climateData?.forecast_2050 || 16.5}°C`} color="orange" />
          <StatCard icon={WiRaindrops} title="CO₂ Level" value={`${climateData?.co2_levels?.[climateData?.co2_levels.length - 1] || 417} ppm`} color="red" />
          <StatCard icon={WiStrongWind} title="Confidence" value={`${climateData?.confidence || 98.4}%`} color="green" />
        </SimpleGrid>

        <Box mb={6}>
          <TemperatureChart data={climateData} loading={loading} />
        </Box>

        <Grid templateColumns={{ base: "1fr", lg: "1fr 1fr 400px" }} gap={6}>
          <PredictionPanel data={climateData} loading={loading} />
          <CitySelector API_URL={API_URL} />
          <HinglishChatbot API_URL={API_URL} />
        </Grid>
      </Container>
    </Box>
  );
}

const StatCard = ({ icon: Icon, title, value, color }) => (
  <Box bg={`${color}.900/20`} border="2px" borderColor={`${color}.500/40`} p={6} borderRadius="2xl" textAlign="center">
    <Icon size={40} color={`${color}.400`} style={{ margin: '0 auto 12px' }} />
    <Text fontSize="sm" color={`${color}.400`} mb={2}>{title}</Text>
    <Text fontSize="3xl" fontWeight="bold">{value}</Text>
  </Box>
);

export default App;
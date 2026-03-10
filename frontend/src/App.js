import React, { useState, useEffect } from 'react';
import { Box, Container, VStack, SimpleGrid, Text, Heading } from '@chakra-ui/react';
import { WiThermometer, WiCloud, WiRaindrops, WiStrongWind } from 'react-icons/wi';
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
      {/* Header */}
      <Box bg="rgba(15, 23, 42, 0.95)" borderBottom="3px" borderColor="blue.500/50" py={8} mb={6}>
        <Container maxW="container.xl">
          <VStack spacing={3} textAlign="center">
            <Heading fontSize="3xl" bgGradient="linear(to-r, blue.400, cyan.400)" bgClip="text">
              🌍 Climate Intelligence Hub
            </Heading>
            <Text fontSize="md" color="gray.300">AI-Powered Climate Prediction & Analysis Platform</Text>
          </VStack>
        </Container>
      </Box>

      <Container maxW="container.xl" px={4}>
        {/* Stats Cards */}
        <SimpleGrid columns={{ base: 2, md: 4 }} gap={6} mb={8}>
          <StatCard icon={WiThermometer} title="Global Temperature" value={`${climateData?.current_temp || 15.14}°C`} color="cyan" />
          <StatCard icon={WiCloud} title="2050 Forecast" value={`${climateData?.forecast_2050 || 16.5}°C`} color="orange" />
          <StatCard icon={WiRaindrops} title="CO₂ Level" value={`${climateData?.co2_levels?.[climateData?.co2_levels.length - 1] || 417} ppm`} color="red" />
          <StatCard icon={WiStrongWind} title="Confidence" value={`${climateData?.confidence || 98.4}%`} color="green" />
        </SimpleGrid>

        {/* Chart */}
        <Box mb={6}>
          <TemperatureChart data={climateData} loading={loading} />
        </Box>

        {/* 3 Column Layout */}
        <SimpleGrid columns={{ base: 1, lg: 3 }} gap={6}>
          <PredictionPanel data={climateData} loading={loading} />
          <CitySelector API_URL={API_URL} />
          <HinglishChatbot API_URL={API_URL} />
        </SimpleGrid>

        {/* Educational Section */}
        <Box mt={8}>
          <EducationalSection />
        </Box>
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

const EducationalSection = () => (
  <Box bg="gray.800/50" p={8} borderRadius="2xl" border="2px" borderColor="gray.700">
    <Heading size="lg" mb={6} color="purple.400" textAlign="center">📚 Climate Change Basics</Heading>
    <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} gap={6}>
      <InfoCard icon="🌡️" title="Global Warming" content="Earth ka average temperature badh raha hai greenhouse gases ki wajah se. 1850 se ab tak 1.2°C increase ho chuka hai." color="orange" />
      <InfoCard icon="🏭" title="Carbon Emissions" content="CO₂, methane aur doosre gases atmosphere mein heat trap karte hain. 2030 tak 45% reduction zaroori hai." color="red" />
      <InfoCard icon="🌊" title="Sea Level Rise" content="Glaciers melt ho rahe hain aur sea level badh raha hai. Coastal cities ko risk hai." color="blue" />
      <InfoCard icon="🌳" title="Solutions" content="Renewable energy, tree plantation, electric vehicles, aur sustainable lifestyle apnao." color="green" />
    </SimpleGrid>
  </Box>
);

const InfoCard = ({ icon, title, content, color }) => (
  <Box p={6} bg={`${color}.900/10`} borderRadius="xl" border="2px" borderColor={`${color}.500/30`}>
    <Text fontSize="4xl" mb={3}>{icon}</Text>
    <Heading size="md" mb={3} color={`${color}.400`}>{title}</Heading>
    <Text fontSize="sm" color="gray.300">{content}</Text>
  </Box>
);

export default App;
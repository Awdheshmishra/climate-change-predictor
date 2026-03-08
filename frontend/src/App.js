import React, { useState, useEffect } from 'react';
import { Box, Grid, Heading, Container, VStack, SimpleGrid, Text, Icon } from '@chakra-ui/react';
import { WiThermometer, WiCloud, WiRaindrops, WiStrongWind } from 'react-icons/wi';
import Dashboard from './components/Dashboard';
import TemperatureChart from './components/TemperatureChart';
import CitySelector from './components/CitySelector';
import HinglishChatbot from './components/HinglishChatbot';
import PredictionPanel from './components/PredictionPanel';

function App() {
  const [climateData, setClimateData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedCity, setSelectedCity] = useState(null);

  useEffect(() => {
    fetchClimateData();
  }, []);

  const fetchClimateData = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/climate-data');
      const data = await response.json();
      setClimateData(data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching climate ', error);
      setLoading(false);
    }
  };

  return (
    <Box bg="linear-gradient(135deg, #0f172a 0%, #1e293b 100%)" minH="100vh" color="white" pb={8}>
      {/* Hero Header */}
      <Box bg="rgba(15, 23, 42, 0.95)" borderBottom="3px" borderColor="blue.500/50" py={8} mb={6}>
        <Container maxW="container.xl">
          <VStack spacing={3} textAlign="center">
            <Heading 
              fontSize={{ base: "3xl", md: "5xl" }} 
              bgGradient="linear(to-r, blue.400, cyan.400, green.400)" 
              bgClip="text"
              fontWeight="bold"
            >
              🌍 Climate Intelligence Hub
            </Heading>
            <Text fontSize={{ base: "md", md: "xl" }} color="gray.300" maxW="700px">
              AI-Powered Climate Prediction & Analysis Platform
            </Text>
            <Text fontSize="sm" color="gray.400">
              Real-time forecasting • City-specific insights • Hinglish Chatbot
            </Text>
          </VStack>
        </Container>
      </Box>

      <Container maxW="container.xl" px={{ base: 4, md: 8 }}>
        {/* Quick Stats Cards */}
        <SimpleGrid columns={{ base: 2, md: 4 }} gap={6} mb={8}>
          <StatCard 
            icon={WiThermometer}
            title="Global Temperature"
            value={`${climateData?.current_temp || 15.14}°C`}
            subtitle="Current Average"
            color="cyan"
          />
          <StatCard 
            icon={WiCloud}
            title="2050 Forecast"
            value={`${climateData?.forecast_2050 || 16.5}°C`}
            subtitle="Predicted Rise"
            color="orange"
          />
          <StatCard 
            icon={WiRaindrops}
            title="CO₂ Level"
            value={`${climateData?.co2_levels?.[climateData?.co2_levels.length - 1] || 417} ppm`}
            subtitle="Atmospheric"
            color="red"
          />
          <StatCard 
            icon={WiStrongWind}
            title="Confidence"
            value={`${climateData?.confidence || 98.4}%`}
            subtitle="Accuracy Rate"
            color="green"
          />
        </SimpleGrid>

        {/* Temperature Chart - Full Width */}
        <Box mb={6}>
          <TemperatureChart data={climateData} loading={loading} />
        </Box>

        {/* Main Grid - 3 Columns */}
        <Grid templateColumns={{ base: "1fr", lg: "1fr 1fr 400px" }} gap={6}>
          {/* Risk Assessment */}
          <Box>
            <PredictionPanel data={climateData} loading={loading} />
          </Box>

          {/* City Selector */}
          <Box>
            <CitySelector onSelectCity={setSelectedCity} selectedCity={selectedCity} />
          </Box>

          {/* Chatbot */}
          <Box>
            <HinglishChatbot />
          </Box>
        </Grid>

        {/* Educational Section */}
        <Box mt={8}>
          <EducationalSection />
        </Box>
      </Container>

      {/* Footer */}
      <Box mt={12} py={6} textAlign="center" bg="rgba(15, 23, 42, 0.8)" borderTop="1px" borderColor="gray.700">
        <Text color="gray.400" fontSize="sm">
          🌱 Built with ❤️ for a sustainable future
        </Text>
        <Text color="gray.500" fontSize="xs" mt={2}>
          Data sources: NASA, NOAA, IMD | Last updated: {new Date().toLocaleDateString()}
        </Text>
      </Box>
    </Box>
  );
}

// Enhanced Stat Card
const StatCard = ({ icon: Icon, title, value, subtitle, color }) => (
  <Box 
    bg={`${color}.900/20`}
    border="2px"
    borderColor={`${color}.500/40`}
    p={6}
    borderRadius="2xl"
    textAlign="center"
    _hover={{ 
      transform: 'translateY(-8px)', 
      boxShadow: `0 20px 40px ${color}.500/30`,
      borderColor: `${color}.400`
    }}
    transition="all 0.3s"
  >
    <Icon size={40} color={`${color}.400`} style={{ margin: '0 auto 12px' }} />
    <Text fontSize="sm" color={`${color}.400`} mb={2} fontWeight="600" textTransform="uppercase" letterSpacing="wide">
      {title}
    </Text>
    <Text fontSize="4xl" fontWeight="bold" mb={2} color="white">{value}</Text>
    <Text fontSize="xs" color="gray.400">{subtitle}</Text>
  </Box>
);

// Educational Section
const EducationalSection = () => (
  <Box bg="gray.800/50" p={8} borderRadius="2xl" border="2px" borderColor="gray.700">
    <Heading size="lg" mb={6} color="purple.400" textAlign="center">
      📚 Climate Change Basics
    </Heading>
    <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} gap={6}>
      <InfoCard 
        icon="🌡️"
        title="Global Warming"
        content="Earth ka average temperature badh raha hai greenhouse gases ki wajah se. 1850 se ab tak 1.2°C increase ho chuka hai."
        color="orange"
      />
      <InfoCard 
        icon="🏭"
        title="Carbon Emissions"
        content="CO₂, methane aur doosre gases atmosphere mein heat trap karte hain. 2030 tak 45% reduction zaroori hai."
        color="red"
      />
      <InfoCard 
        icon="🌊"
        title="Sea Level Rise"
        content="Glaciers melt ho rahe hain aur sea level badh raha hai. Coastal cities ko risk hai."
        color="blue"
      />
      <InfoCard 
        icon="🌳"
        title="Solutions"
        content="Renewable energy, tree plantation, electric vehicles, aur sustainable lifestyle apnao."
        color="green"
      />
    </SimpleGrid>
  </Box>
);

const InfoCard = ({ icon, title, content, color }) => (
  <Box 
    p={6} 
    bg={`${color}.900/10`} 
    borderRadius="xl" 
    border="2px" 
    borderColor={`${color}.500/30`}
    _hover={{ borderColor: `${color}.400`, transform: 'translateY(-4px)' }}
    transition="all 0.3s"
  >
    <Text fontSize="4xl" mb={3}>{icon}</Text>
    <Heading size="md" mb={3} color={`${color}.400`}>{title}</Heading>
    <Text fontSize="sm" color="gray.300" lineHeight="tall">{content}</Text>
  </Box>
);

export default App;
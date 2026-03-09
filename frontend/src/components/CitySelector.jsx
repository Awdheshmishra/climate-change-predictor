import React, { useState } from 'react';
import {
  Box,
  Heading,
  Select,
  VStack,
  Text,
  Grid,
  Badge,
  Spinner,
  Tabs,
  TabList,
  TabPanels,
  Tab,
  TabPanel,
  Icon
} from '@chakra-ui/react';
import { FaMapMarkerAlt } from 'react-icons/fa';

const indianStates = [
  { value: 'delhi', name: 'Delhi', emoji: '🏛️', temp: 26.5, aqi: 320, rainfall: 780 },
  { value: 'mumbai', name: 'Mumbai, Maharashtra', emoji: '🌊', temp: 28.3, aqi: 180, rainfall: 2200 },
  { value: 'kolkata', name: 'Kolkata, West Bengal', emoji: '🏙️', temp: 27.8, aqi: 195, rainfall: 1580 },
  { value: 'chennai', name: 'Chennai, Tamil Nadu', emoji: '🏖️', temp: 29.5, aqi: 165, rainfall: 1400 },
  { value: 'bangalore', name: 'Bangalore, Karnataka', emoji: '💻', temp: 24.5, aqi: 145, rainfall: 970 },
  { value: 'hyderabad', name: 'Hyderabad, Telangana', emoji: '🕌', temp: 28.0, aqi: 175, rainfall: 850 },
  { value: 'pune', name: 'Pune, Maharashtra', emoji: '🎓', temp: 25.5, aqi: 160, rainfall: 750 },
  { value: 'ahmedabad', name: 'Ahmedabad, Gujarat', emoji: '🏭', temp: 28.5, aqi: 210, rainfall: 650 },
  { value: 'jaipur', name: 'Jaipur, Rajasthan', emoji: '🏰', temp: 27.5, aqi: 195, rainfall: 550 },
  { value: 'lucknow', name: 'Lucknow, Uttar Pradesh', emoji: '🌳', temp: 25.8, aqi: 210, rainfall: 850 }
];

const internationalCities = [
  { value: 'newyork', name: 'New York, USA', emoji: '🗽', temp: 13.0, aqi: 65, rainfall: 1200 },
  { value: 'london', name: 'London, UK', emoji: '🎡', temp: 11.5, aqi: 55, rainfall: 750 },
  { value: 'paris', name: 'Paris, France', emoji: '🗼', temp: 12.5, aqi: 60, rainfall: 650 },
  { value: 'tokyo', name: 'Tokyo, Japan', emoji: '🗾', temp: 16.0, aqi: 45, rainfall: 1530 },
  { value: 'dubai', name: 'Dubai, UAE', emoji: '🏙️', temp: 33.0, aqi: 145, rainfall: 100 },
  { value: 'singapore', name: 'Singapore', emoji: '🦁', temp: 28.0, aqi: 55, rainfall: 2340 }
];

const CitySelector = ({ API_URL }) => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState(0);

  const handleCityChange = async (cityValue, type) => {
    if (!cityValue || !API_URL) {
      console.log('No city value or API URL');
      return;
    }

    setLoading(true);
    try {
      console.log('Fetching city data:', cityValue, 'from:', API_URL);
      const response = await fetch(`${API_URL}/api/city/${cityValue}/quick`);
      const data = await response.json();
      console.log('City data received:', data);
      setPrediction(data);
    } catch (error) {
      console.error('Error fetching city data:', error);
    }
    setLoading(false);
  };

  const getAQIColor = (aqi) => {
    if (aqi <= 50) return 'green';
    if (aqi <= 100) return 'yellow';
    if (aqi <= 150) return 'orange';
    if (aqi <= 200) return 'red';
    return 'purple';
  };

  const getAQILabel = (aqi) => {
    if (aqi <= 50) return 'Good';
    if (aqi <= 100) return 'Moderate';
    if (aqi <= 150) return 'Unhealthy';
    if (aqi <= 200) return 'Very Unhealthy';
    return 'Hazardous';
  };

  return (
    <Box bg="gray.800" p={6} borderRadius="2xl" border="2px" borderColor="purple.500/30" h="full">
      <Heading size="md" mb={4} color="purple.400" display="flex" alignItems="center">
        <Icon as={FaMapMarkerAlt} mr={2} />
        🌍 City Climate Prediction
      </Heading>

      <Tabs index={activeTab} onChange={setActiveTab} variant="enclosed" colorScheme="purple" mb={4}>
        <TabList>
          <Tab fontSize="sm">🇮🇳 Indian</Tab>
          <Tab fontSize="sm">🌏 International</Tab>
        </TabList>
      </Tabs>

      {activeTab === 0 ? (
        <Select
          placeholder="📍 Select City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value, 'india')}
          bg="gray.700"
          borderColor="gray.600"
        >
          {indianStates.map(city => (
            <option key={city.value} value={city.value}>
              {city.emoji} {city.name}
            </option>
          ))}
        </Select>
      ) : (
        <Select
          placeholder="🌍 Select City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value, 'international')}
          bg="gray.700"
          borderColor="gray.600"
        >
          {internationalCities.map(city => (
            <option key={city.value} value={city.value}>
              {city.emoji} {city.name}
            </option>
          ))}
        </Select>
      )}

      {loading && (
        <Box textAlign="center" py={8}>
          <Spinner size="xl" color="purple.500" />
          <Text mt={4} color="gray.400">Loading...</Text>
        </Box>
      )}

      {prediction && !loading && prediction.current && prediction.prediction_2050 && (
        <VStack spacing={4} align="stretch">
          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="blue.900/30" p={4} borderRadius="xl">
              <Text color="blue.400" fontSize="xs" mb={1}>CURRENT</Text>
              <Heading size="xl">{prediction.current.temperature}°C</Heading>
            </Box>
            <Box bg="red.900/30" p={4} borderRadius="xl">
              <Text color="red.400" fontSize="xs" mb={1}>2050</Text>
              <Heading size="xl">{prediction.prediction_2050.temperature}°C</Heading>
            </Box>
          </Grid>

          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="orange.900/30" p={4} borderRadius="xl">
              <Text color="orange.400" fontSize="xs" mb={1}>AQI</Text>
              <Heading size="lg">{prediction.current.aqi}</Heading>
              <Badge mt={1} colorScheme={getAQIColor(prediction.current.aqi)} fontSize="xs">
                {getAQILabel(prediction.current.aqi)}
              </Badge>
            </Box>
            <Box bg="cyan.900/30" p={4} borderRadius="xl">
              <Text color="cyan.400" fontSize="xs" mb={1}>RAINFALL</Text>
              <Heading size="lg">{prediction.current.rainfall_mm} mm</Heading>
            </Box>
          </Grid>

          <Box bg="green.900/20" p={4} borderRadius="xl">
            <Heading size="sm" color="green.400" mb={2}>💡 Recommendations:</Heading>
            {prediction.recommendations && prediction.recommendations.slice(0, 3).map((rec, idx) => (
              <Text key={idx} fontSize="sm" color="gray.300">• {rec}</Text>
            ))}
          </Box>
        </VStack>
      )}

      {!prediction && !loading && (
        <Box textAlign="center" py={8} color="gray.500">
          <Text fontSize="sm">Select a city to view prediction</Text>
        </Box>
      )}
    </Box>
  );
};

export default CitySelector;
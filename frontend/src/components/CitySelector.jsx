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
  Icon,
  SimpleGrid
} from '@chakra-ui/react';
import { FaMapMarkerAlt, FaBuilding, FaGlobe } from 'react-icons/fa';

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
  { value: 'lucknow', name: 'Lucknow, Uttar Pradesh', emoji: '🌳', temp: 25.8, aqi: 210, rainfall: 850 },
  { value: 'kanpur', name: 'Kanpur, UP', emoji: '🏭', temp: 26.2, aqi: 285, rainfall: 720 },
  { value: 'nagpur', name: 'Nagpur, Maharashtra', emoji: '🍊', temp: 27.0, aqi: 175, rainfall: 1100 },
  { value: 'indore', name: 'Indore, MP', emoji: '🏆', temp: 26.0, aqi: 165, rainfall: 950 },
  { value: 'bhopal', name: 'Bhopal, MP', emoji: '🕌', temp: 25.5, aqi: 170, rainfall: 1050 },
  { value: 'patna', name: 'Patna, Bihar', emoji: '📚', temp: 26.8, aqi: 225, rainfall: 1050 },
  { value: 'vadodara', name: 'Vadodara, Gujarat', emoji: '🎭', temp: 28.0, aqi: 185, rainfall: 800 },
  { value: 'ghaziabad', name: 'Ghaziabad, UP', emoji: '🏭', temp: 26.5, aqi: 295, rainfall: 700 },
  { value: 'ludhiana', name: 'Ludhiana, Punjab', emoji: '🌾', temp: 24.5, aqi: 235, rainfall: 650 },
  { value: 'agra', name: 'Agra, UP', emoji: '🕌', temp: 26.5, aqi: 245, rainfall: 650 },
  { value: 'nashik', name: 'Nashik, Maharashtra', emoji: '🍇', temp: 25.5, aqi: 155, rainfall: 750 },
  { value: 'faridabad', name: 'Faridabad, Haryana', emoji: '🏭', temp: 26.8, aqi: 285, rainfall: 680 },
  { value: 'meerut', name: 'Meerut, UP', emoji: '🏭', temp: 26.2, aqi: 265, rainfall: 700 },
  { value: 'rajkot', name: 'Rajkot, Gujarat', emoji: '🦁', temp: 28.0, aqi: 175, rainfall: 650 },
  { value: 'kalyan', name: 'Kalyan, Maharashtra', emoji: '🏘️', temp: 28.0, aqi: 190, rainfall: 2000 },
  { value: 'thane', name: 'Thane, Maharashtra', emoji: '', temp: 28.2, aqi: 185, rainfall: 2100 },
  { value: 'varanasi', name: 'Varanasi, UP', emoji: '🕉️', temp: 26.5, aqi: 235, rainfall: 950 },
  { value: 'srinagar', name: 'Srinagar, J&K', emoji: '🏔️', temp: 14.5, aqi: 85, rainfall: 650 },
  { value: 'chandigarh', name: 'Chandigarh', emoji: '🌳', temp: 24.0, aqi: 165, rainfall: 850 },
  { value: 'coimbatore', name: 'Coimbatore, TN', emoji: '🏭', temp: 27.5, aqi: 145, rainfall: 650 },
  { value: 'kochi', name: 'Kochi, Kerala', emoji: '🌴', temp: 28.5, aqi: 125, rainfall: 2800 },
  { value: 'thiruvananthapuram', name: 'Trivandrum, Kerala', emoji: '🏛️', temp: 28.0, aqi: 115, rainfall: 2500 },
  { value: 'guwahati', name: 'Guwahati, Assam', emoji: '🍵', temp: 25.5, aqi: 155, rainfall: 1700 },
  { value: 'bhubaneswar', name: 'Bhubaneswar, Odisha', emoji: '🛕', temp: 28.0, aqi: 165, rainfall: 1550 },
  { value: 'ranchi', name: 'Ranchi, Jharkhand', emoji: '🏞️', temp: 24.5, aqi: 145, rainfall: 1400 },
  { value: 'raipur', name: 'Raipur, Chhattisgarh', emoji: '🌾', temp: 26.5, aqi: 175, rainfall: 1300 },
  { value: 'dehradun', name: 'Dehradun, Uttarakhand', emoji: '🏔️', temp: 20.5, aqi: 125, rainfall: 1350 },
  { value: 'shimla', name: 'Shimla, HP', emoji: '🏔️', temp: 16.5, aqi: 75, rainfall: 1100 },
  { value: 'gangtok', name: 'Gangtok, Sikkim', emoji: '🏔️', temp: 16.0, aqi: 65, rainfall: 2500 },
  { value: 'imphal', name: 'Imphal, Manipur', emoji: '🌸', temp: 22.5, aqi: 95, rainfall: 1400 },
  { value: 'agartala', name: 'Agartala, Tripura', emoji: '🌳', temp: 25.5, aqi: 115, rainfall: 2100 }
];

const internationalCities = [
  { value: 'newyork', name: 'New York, USA', emoji: '🗽', temp: 13.0, aqi: 65, rainfall: 1200 },
  { value: 'london', name: 'London, UK', emoji: '🎡', temp: 11.5, aqi: 55, rainfall: 750 },
  { value: 'paris', name: 'Paris, France', emoji: '🗼', temp: 12.5, aqi: 60, rainfall: 650 },
  { value: 'tokyo', name: 'Tokyo, Japan', emoji: '🗾', temp: 16.0, aqi: 45, rainfall: 1530 },
  { value: 'beijing', name: 'Beijing, China', emoji: '🏯', temp: 13.0, aqi: 185, rainfall: 585 },
  { value: 'dubai', name: 'Dubai, UAE', emoji: '🏙️', temp: 33.0, aqi: 145, rainfall: 100 },
  { value: 'singapore', name: 'Singapore', emoji: '🦁', temp: 28.0, aqi: 55, rainfall: 2340 },
  { value: 'sydney', name: 'Sydney, Australia', emoji: '🦘', temp: 19.0, aqi: 35, rainfall: 1210 },
  { value: 'toronto', name: 'Toronto, Canada', emoji: '🍁', temp: 9.5, aqi: 45, rainfall: 830 },
  { value: 'berlin', name: 'Berlin, Germany', emoji: '🍺', temp: 10.5, aqi: 50, rainfall: 570 },
  { value: 'moscow', name: 'Moscow, Russia', emoji: '🏰', temp: 6.0, aqi: 75, rainfall: 707 },
  { value: 'cairo', name: 'Cairo, Egypt', emoji: '🔺', temp: 28.0, aqi: 165, rainfall: 25 },
  { value: 'saopaulo', name: 'São Paulo, Brazil', emoji: '🇧🇷', temp: 20.0, aqi: 95, rainfall: 1455 },
  { value: 'mexicocity', name: 'Mexico City, Mexico', emoji: '🌮', temp: 17.0, aqi: 125, rainfall: 820 },
  { value: 'bangkok', name: 'Bangkok, Thailand', emoji: '🛕', temp: 29.5, aqi: 115, rainfall: 1620 },
  { value: 'kualalumpur', name: 'Kuala Lumpur, Malaysia', emoji: '🏙️', temp: 28.5, aqi: 95, rainfall: 2530 },
  { value: 'jakarta', name: 'Jakarta, Indonesia', emoji: '🏝️', temp: 28.0, aqi: 135, rainfall: 1790 },
  { value: 'manila', name: 'Manila, Philippines', emoji: '🏝️', temp: 28.5, aqi: 105, rainfall: 2100 },
  { value: 'karachi', name: 'Karachi, Pakistan', emoji: '🕌', temp: 27.5, aqi: 195, rainfall: 250 },
  { value: 'dhaka', name: 'Dhaka, Bangladesh', emoji: '🇧🇩', temp: 26.5, aqi: 215, rainfall: 2120 },
  { value: 'colombo', name: 'Colombo, Sri Lanka', emoji: '🇱🇰', temp: 28.0, aqi: 95, rainfall: 2330 },
  { value: 'kathmandu', name: 'Kathmandu, Nepal', emoji: '🏔️', temp: 18.5, aqi: 185, rainfall: 1400 },
  { value: 'kabul', name: 'Kabul, Afghanistan', emoji: '🏔️', temp: 12.5, aqi: 165, rainfall: 310 },
  { value: 'tehran', name: 'Tehran, Iran', emoji: '🕌', temp: 17.5, aqi: 175, rainfall: 230 }
];

const CitySelector = ({ onSelectCity, selectedCity, API_URL }) => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState(0);

  const handleCityChange = async (cityValue, type) => {
    if (!cityValue) return;

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/api/city/${cityValue}/quick`);
      const data = await response.json();
      setPrediction(data);
      onSelectCity(data);
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  const getRecommendations = (city, type) => {
    if (type === 'india') {
      return [
        "🌳 Tree plantation drives karo",
        "💧 Water conservation priority do",
        "🚲 Public transport ko promote karo",
        "♻️ Waste management improve karo",
        "🏭 Industrial pollution control karo"
      ];
    } else {
      return [
        "🌍 Global climate action support karo",
        "🌱 Sustainable practices adopt karo",
        "🔋 Renewable energy use badhao",
        "🚗 Electric vehicles promote karo"
      ];
    }
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
    if (aqi <= 150) return 'Unhealthy for Sensitive';
    if (aqi <= 200) return 'Unhealthy';
    if (aqi <= 300) return 'Very Unhealthy';
    return 'Hazardous';
  };

  return (
    <Box bg="gray.800" p={6} borderRadius="2xl" border="2px" borderColor="purple.500/30" h="full">
      <Heading size="md" mb={4} color="purple.400" display="flex" alignItems="center">
        <Icon as={FaMapMarkerAlt} mr={2} />
        🌍 City/State Climate Prediction
      </Heading>

      <Tabs index={activeTab} onChange={setActiveTab} variant="enclosed" colorScheme="purple" mb={4}>
        <TabList>
          <Tab fontSize="sm">🇮🇳 Indian States</Tab>
          <Tab fontSize="sm">🌏 International</Tab>
        </TabList>
      </Tabs>

      {activeTab === 0 ? (
        <Select
          placeholder="📍 Select Indian State/City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value, 'india')}
          bg="gray.700"
          borderColor="gray.600"
          _hover={{ borderColor: 'purple.400' }}
          _focus={{ borderColor: 'purple.500', boxShadow: '0 0 0 1px purple.500' }}
        >
          {indianStates.map(city => (
            <option key={city.value} value={city.value}>
              {city.emoji} {city.name}
            </option>
          ))}
        </Select>
      ) : (
        <Select
          placeholder="🌍 Select International City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value, 'international')}
          bg="gray.700"
          borderColor="gray.600"
          _hover={{ borderColor: 'purple.400' }}
          _focus={{ borderColor: 'purple.500', boxShadow: '0 0 0 1px purple.500' }}
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
          <Text mt={4} color="gray.400">Loading city data...</Text>
        </Box>
      )}

      {prediction && !loading && (
        <VStack spacing={4} align="stretch" className="slide-up">
          {/* Temperature Cards */}
          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="blue.900/30" p={4} borderRadius="xl" border="1px" borderColor="blue.500/30">
              <Text color="blue.400" fontSize="xs" mb={1} fontWeight="600">CURRENT TEMP</Text>
              <Heading size="2xl">{prediction.current.temperature}°C</Heading>
            </Box>
            <Box bg="red.900/30" p={4} borderRadius="xl" border="1px" borderColor="red.500/30">
              <Text color="red.400" fontSize="xs" mb={1} fontWeight="600">2050 PREDICTION</Text>
              <Heading size="2xl">{prediction.prediction_2050.temperature}°C</Heading>
            </Box>
          </Grid>

          {/* AQI & Rainfall */}
          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="orange.900/30" p={4} borderRadius="xl">
              <Text color="orange.400" fontSize="xs" mb={1} fontWeight="600">CURRENT AQI</Text>
              <Heading size="xl" mb={2}>{prediction.current.aqi}</Heading>
              <Badge 
                colorScheme={getAQIColor(prediction.current.aqi)} 
                px={2} py={1} borderRadius="full" fontSize="xs"
              >
                {getAQILabel(prediction.current.aqi)}
              </Badge>
            </Box>
            <Box bg="cyan.900/30" p={4} borderRadius="xl">
              <Text color="cyan.400" fontSize="xs" mb={1} fontWeight="600">ANNUAL RAINFALL</Text>
              <Heading size="xl">{prediction.current.rainfall_mm} mm</Heading>
            </Box>
          </Grid>

          {/* Increase Indicator */}
          <Box bg="yellow.900/20" p={4} borderRadius="xl" border="1px" borderColor="yellow.500/30">
            <Text color="yellow.400" fontSize="xs" mb={1}>TEMPERATURE INCREASE BY 2050</Text>
            <Heading size="lg" color="yellow.400">+{prediction.prediction_2050.increase}°C</Heading>
          </Box>

          {/* Recommendations */}
          <Box bg="green.900/20" p={4} borderRadius="xl" border="2px" borderColor="green.500/30">
            <Heading size="sm" color="green.400" mb={3} display="flex" alignItems="center">
              💡 Recommendations:
            </Heading>
            <VStack align="stretch" spacing={2}>
              {prediction.recommendations.map((rec, idx) => (
                <Text key={idx} fontSize="sm" color="gray.200">
                  {rec}
                </Text>
              ))}
            </VStack>
          </Box>
        </VStack>
      )}

      {!prediction && !loading && (
        <Box textAlign="center" py={8} color="gray.500">
          <Icon as={FaGlobe} boxSize={12} mb={3} opacity={0.5} />
          <Text fontSize="sm">Select a city to view climate prediction</Text>
        </Box>
      )}
    </Box>
  );
};

export default CitySelector;
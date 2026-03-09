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
} from '@chakra-ui/react';

const indianStates = [
  { value: 'delhi', name: 'Delhi 🏛️' },
  { value: 'mumbai', name: 'Mumbai, Maharashtra 🌊' },
  { value: 'kolkata', name: 'Kolkata, West Bengal 🏙️' },
  { value: 'chennai', name: 'Chennai, Tamil Nadu 🏖️' },
  { value: 'bangalore', name: 'Bangalore, Karnataka 💻' },
  { value: 'hyderabad', name: 'Hyderabad, Telangana 🕌' },
  { value: 'pune', name: 'Pune, Maharashtra 🎓' },
  { value: 'ahmedabad', name: 'Ahmedabad, Gujarat 🏭' },
  { value: 'jaipur', name: 'Jaipur, Rajasthan 🏰' },
  { value: 'lucknow', name: 'Lucknow, Uttar Pradesh 🌳' },
  { value: 'kanpur', name: 'Kanpur, UP 🏭' },
  { value: 'nagpur', name: 'Nagpur, Maharashtra 🍊' },
  { value: 'indore', name: 'Indore, MP 🏆' },
  { value: 'bhopal', name: 'Bhopal, MP 🕌' },
  { value: 'patna', name: 'Patna, Bihar 📚' },
  { value: 'vadodara', name: 'Vadodara, Gujarat 🎭' },
  { value: 'ghaziabad', name: 'Ghaziabad, UP 🏭' },
  { value: 'ludhiana', name: 'Ludhiana, Punjab 🌾' },
  { value: 'agra', name: 'Agra, UP 🕌' },
  { value: 'nashik', name: 'Nashik, Maharashtra 🍇' },
  { value: 'faridabad', name: 'Faridabad, Haryana 🏭' },
  { value: 'meerut', name: 'Meerut, UP 🏭' },
  { value: 'rajkot', name: 'Rajkot, Gujarat 🦁' },
  { value: 'kalyan', name: 'Kalyan, Maharashtra 🏘️' },
  { value: 'thane', name: 'Thane, Maharashtra 🏙️' },
  { value: 'varanasi', name: 'Varanasi, UP 🕉️' },
  { value: 'srinagar', name: 'Srinagar, J&K 🏔️' },
  { value: 'chandigarh', name: 'Chandigarh 🌳' },
  { value: 'coimbatore', name: 'Coimbatore, TN 🏭' },
  { value: 'kochi', name: 'Kochi, Kerala 🌴' },
  { value: 'thiruvananthapuram', name: 'Trivandrum, Kerala 🏛️' },
  { value: 'guwahati', name: 'Guwahati, Assam 🍵' },
  { value: 'bhubaneswar', name: 'Bhubaneswar, Odisha 🛕' },
  { value: 'ranchi', name: 'Ranchi, Jharkhand 🏞️' },
  { value: 'raipur', name: 'Raipur, Chhattisgarh 🌾' },
  { value: 'dehradun', name: 'Dehradun, Uttarakhand 🏔️' },
  { value: 'shimla', name: 'Shimla, HP 🏔️' },
  { value: 'gangtok', name: 'Gangtok, Sikkim 🏔️' },
  { value: 'imphal', name: 'Imphal, Manipur 🌸' },
  { value: 'agartala', name: 'Agartala, Tripura 🌳' }
];

const internationalCities = [
  { value: 'newyork', name: 'New York, USA 🗽' },
  { value: 'london', name: 'London, UK 🎡' },
  { value: 'paris', name: 'Paris, France 🗼' },
  { value: 'tokyo', name: 'Tokyo, Japan 🗾' },
  { value: 'beijing', name: 'Beijing, China 🏯' },
  { value: 'dubai', name: 'Dubai, UAE 🏙️' },
  { value: 'singapore', name: 'Singapore 🦁' },
  { value: 'sydney', name: 'Sydney, Australia 🦘' },
  { value: 'toronto', name: 'Toronto, Canada 🍁' },
  { value: 'berlin', name: 'Berlin, Germany 🍺' },
  { value: 'moscow', name: 'Moscow, Russia 🏰' },
  { value: 'cairo', name: 'Cairo, Egypt 🔺' },
  { value: 'saopaulo', name: 'São Paulo, Brazil 🇧🇷' },
  { value: 'mexicocity', name: 'Mexico City, Mexico 🌮' },
  { value: 'bangkok', name: 'Bangkok, Thailand 🛕' },
  { value: 'kualalumpur', name: 'Kuala Lumpur, Malaysia 🏙️' },
  { value: 'jakarta', name: 'Jakarta, Indonesia 🏝️' },
  { value: 'manila', name: 'Manila, Philippines 🏝️' },
  { value: 'karachi', name: 'Karachi, Pakistan 🕌' },
  { value: 'dhaka', name: 'Dhaka, Bangladesh 🇧🇩' },
  { value: 'colombo', name: 'Colombo, Sri Lanka 🇱🇰' },
  { value: 'kathmandu', name: 'Kathmandu, Nepal 🏔️' },
  { value: 'kabul', name: 'Kabul, Afghanistan 🏔️' },
  { value: 'tehran', name: 'Tehran, Iran 🕌' }
];

const CitySelector = ({ API_URL }) => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState(0);

  const handleCityChange = async (cityValue) => {
    if (!cityValue || !API_URL) return;

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/api/city/${cityValue}/quick`);
      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error('Error:', error);
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

  return (
    <Box bg="gray.800" p={6} borderRadius="2xl" border="2px" borderColor="purple.500/30">
      <Heading size="md" mb={4} color="purple.400">
        🌍 City Climate Prediction
      </Heading>

      <Tabs index={activeTab} onChange={setActiveTab} variant="enclosed" colorScheme="purple" mb={4}>
        <TabList>
          <Tab>🇮🇳 Indian</Tab>
          <Tab>🌏 International</Tab>
        </TabList>
      </Tabs>

      {activeTab === 0 ? (
        <Select
          placeholder="📍 Select Indian City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value)}
          bg="gray.700"
          borderColor="gray.600"
          color="white"
          _hover={{ borderColor: 'purple.400' }}
          _focus={{ borderColor: 'purple.500' }}
        >
          {indianStates.map(city => (
            <option key={city.value} value={city.value} style={{ color: 'white' }}>
              {city.name}
            </option>
          ))}
        </Select>
      ) : (
        <Select
          placeholder="🌍 Select International City..."
          size="md"
          mb={4}
          onChange={(e) => handleCityChange(e.target.value)}
          bg="gray.700"
          borderColor="gray.600"
          color="white"
          _hover={{ borderColor: 'purple.400' }}
          _focus={{ borderColor: 'purple.500' }}
        >
          {internationalCities.map(city => (
            <option key={city.value} value={city.value} style={{ color: 'white' }}>
              {city.name}
            </option>
          ))}
        </Select>
      )}

      {loading && <Spinner size="lg" color="purple.500" />}

      {prediction && !loading && prediction.current && (
        <VStack spacing={4} align="stretch">
          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="blue.900/30" p={4} borderRadius="xl">
              <Text color="blue.400" fontSize="xs">CURRENT</Text>
              <Heading size="xl">{prediction.current.temperature}°C</Heading>
            </Box>
            <Box bg="red.900/30" p={4} borderRadius="xl">
              <Text color="red.400" fontSize="xs">2050</Text>
              <Heading size="xl">{prediction.prediction_2050.temperature}°C</Heading>
            </Box>
          </Grid>

          <Grid templateColumns="1fr 1fr" gap={3}>
            <Box bg="orange.900/30" p={4} borderRadius="xl">
              <Text color="orange.400" fontSize="xs">AQI</Text>
              <Heading size="lg">{prediction.current.aqi}</Heading>
              <Badge mt={1} colorScheme={getAQIColor(prediction.current.aqi)}>
                {prediction.current.aqi > 200 ? 'Unhealthy' : 'Moderate'}
              </Badge>
            </Box>
            <Box bg="cyan.900/30" p={4} borderRadius="xl">
              <Text color="cyan.400" fontSize="xs">RAINFALL</Text>
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
          <Text>Select a city to view prediction</Text>
        </Box>
      )}
    </Box>
  );
};

export default CitySelector;
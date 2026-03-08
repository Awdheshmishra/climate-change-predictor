import React from 'react';
import { Box, Heading, Text, Progress, Grid, Alert, AlertIcon, Spinner } from '@chakra-ui/react';

const PredictionPanel = ({ data, loading }) => {
  if (loading) {
    return (
      <Box bg="gray.800" p={6} borderRadius="2xl" textAlign="center">
        <Spinner size="xl" color="yellow.500" />
      </Box>
    );
  }

  const currentTemp = data?.current_temp || 15.14;
  const forecastTemp = data?.forecast_2050 || 16.5;
  const increase = forecastTemp - currentTemp;
  const co2Current = data?.co2_levels?.[data?.co2_levels.length - 1] || 420;
  const co2PreIndustrial = 280;

  const getRiskLevel = (increase) => {
    if (increase < 1.5) return { level: 'Moderate', color: 'yellow', message: 'Action needed' };
    if (increase < 2) return { level: 'High', color: 'orange', message: 'Urgent action required' };
    return { level: 'Critical', color: 'red', message: 'Immediate action critical' };
  };

  const risk = getRiskLevel(increase);

  return (
    <Box bg="gray.800" p={6} borderRadius="2xl" border="2px" borderColor="yellow.500/30" h="full">
      <Heading size="md" mb={6} color="yellow.400" display="flex" alignItems="center">
        ⚠️ Climate Risk Assessment
      </Heading>

      <Grid templateColumns={{ base: "1fr", md: "1fr 1fr" }} gap={6} mb={6}>
        {/* Temperature Rise */}
        <Box>
          <Text color="gray.400" mb={2} fontSize="sm" fontWeight="600">Temperature Increase by 2050</Text>
          <Box mb={2}>
            <Text fontSize="4xl" fontWeight="bold" color={risk.color + '.400'}>
              +{increase.toFixed(2)}°C
            </Text>
          </Box>
          <Progress 
            value={(increase / 3) * 100} 
            colorScheme={risk.color}
            size="md"
            borderRadius="full"
            mb={2}
          />
          <Text fontSize="xs" color="gray.500">Target: &lt;1.5°C (Paris Agreement)</Text>
        </Box>

        {/* CO2 Levels */}
        <Box>
          <Text color="gray.400" mb={2} fontSize="sm" fontWeight="600">CO₂ Concentration</Text>
          <Box mb={2}>
            <Text fontSize="4xl" fontWeight="bold" color="orange.400">
              {co2Current} ppm
            </Text>
          </Box>
          <Progress 
            value={((co2Current - co2PreIndustrial) / 200) * 100} 
            colorScheme="orange"
            size="md"
            borderRadius="full"
            mb={2}
          />
          <Text fontSize="xs" color="gray.500">Pre-industrial: {co2PreIndustrial} ppm</Text>
        </Box>
      </Grid>

      {/* Alert Box */}
      <Alert 
        status={risk.color === 'red' ? 'error' : risk.color === 'orange' ? 'warning' : 'info'}
        borderRadius="xl"
        py={4}
        px={4}
      >
        <AlertIcon boxSize={5} />
        <Box>
          <Text fontWeight="bold" fontSize="md">
            Risk Level: {risk.level.toUpperCase()}
          </Text>
          <Text fontSize="sm" mt={1}>
            {risk.message} - Global temperature rise is {increase >= 1.5 ? 'exceeding' : 'approaching'} safe limits. 
            Carbon neutrality must be achieved by 2050.
          </Text>
        </Box>
      </Alert>

      {/* AI Insight */}
      <Box 
        mt={4} 
        p={4} 
        bg="blue.900/20" 
        borderRadius="xl" 
        border="2px" 
        borderColor="blue.500/30"
      >
        <Heading size="sm" color="blue.400" mb={2}>💡 AI Insight:</Heading>
        <Text fontSize="sm" color="gray.300" lineHeight="tall">
          By the year 2050, global temperatures could stabilize if carbon neutrality is achieved by 2050. 
          Immediate action on renewable energy, reforestation, and emission reduction is critical. 
          Every 0.1°C matters! 🌱
        </Text>
      </Box>
    </Box>
  );
};

export default PredictionPanel;
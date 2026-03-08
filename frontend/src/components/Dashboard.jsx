import React from 'react';
import { Box, Heading, Text, SimpleGrid, Spinner } from '@chakra-ui/react';

const Dashboard = ({ data, loading }) => {
  if (loading) {
    return (
      <Box bg="gray.800" p={8} borderRadius="2xl" textAlign="center">
        <Spinner size="xl" color="blue.500" />
        <Text mt={4} fontSize="lg">Loading climate data...</Text>
      </Box>
    );
  }

  const cards = [
    { 
      title: "Global Temp (Today)", 
      value: `${data?.current_temp || 15.14}°C`, 
      subtitle: "Current Average",
      color: "cyan" 
    },
    { 
      title: "Forecast (2050)", 
      value: `${data?.forecast_2050 || 16.5}°C`, 
      subtitle: "Predicted Rise",
      color: "orange" 
    },
    { 
      title: "Confidence Index", 
      value: `${data?.confidence || 98.4}%`, 
      subtitle: "Satellite Verified",
      color: "green" 
    },
    { 
      title: "CO₂ Level", 
      value: `${data?.co2_levels?.[data?.co2_levels.length - 1] || 420} ppm`, 
      subtitle: "Pre-industrial: 280 ppm",
      color: "red" 
    }
  ];

  return (
    <SimpleGrid columns={{ base: 2, md: 4 }} gap={6}>
      {cards.map((card, index) => (
        <Box 
          key={index} 
          bg={`${card.color}.900/20`} 
          border="2px" 
          borderColor={`${card.color}.500/40`} 
          p={6} 
          borderRadius="2xl"
          _hover={{ transform: 'translateY(-4px)', boxShadow: `0 10px 30px ${card.color}.500/20` }}
          transition="all 0.3s"
        >
          <Heading size="xs" color={`${card.color}.400`} mb={2} textTransform="uppercase" letterSpacing="wide">
            {card.title}
          </Heading>
          <Heading size="2xl" color="white" mb={1}>{card.value}</Heading>
          <Text fontSize="xs" color="gray.400">{card.subtitle}</Text>
        </Box>
      ))}
    </SimpleGrid>
  );
};

export default Dashboard;
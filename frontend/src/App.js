import React, { useState, useEffect } from "react";
import { Box, Heading, Container, Text, SimpleGrid } from "@chakra-ui/react";
import TemperatureChart from "./components/TemperatureChart";
import HinglishChatbot from "./components/HinglishChatbot";
import CitySelector from "./components/CitySelector";
import PredictionPanel from "./components/PredictionPanel";

function App() {

  const [climateData, setClimateData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedCity, setSelectedCity] = useState(null);

  useEffect(() => {
    fetchClimateData();
  }, []);

  const fetchClimateData = async () => {
    try {

      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/climate-data`
      );

      const data = await response.json();

      setClimateData(data);
      setLoading(false);

    } catch (error) {
      console.error("Error fetching climate data", error);
      setLoading(false);
    }
  };

  return (
    <Box bg="#0f172a" minH="100vh" color="white">

      <Box py={8} textAlign="center">
        <Heading size="2xl">🌍 Climate Predictor</Heading>
        <Text mt={2}>
          AI Powered Climate Prediction Platform
        </Text>
      </Box>

      <Container maxW="container.xl">

        <SimpleGrid columns={{ base: 1, lg: 3 }} spacing={6}>

          <Box>
            <PredictionPanel data={climateData} loading={loading}/>
          </Box>

          <Box>
            <CitySelector
              selectedCity={selectedCity}
              onSelectCity={setSelectedCity}
            />
          </Box>

          <Box>
            <HinglishChatbot/>
          </Box>

        </SimpleGrid>

        <Box mt={10}>
          <TemperatureChart
            data={climateData}
            loading={loading}
          />
        </Box>

      </Container>

    </Box>
  );
}

export default App;
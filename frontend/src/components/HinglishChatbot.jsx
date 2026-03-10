import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  Input,
  Button,
  VStack,
  Text,
  Avatar,
  Heading,
  Spinner,
  Badge,
  Flex,
  Icon
} from '@chakra-ui/react';
import { FaPaperPlane, FaRobot } from 'react-icons/fa';

const HinglishChatbot = ({ API_URL }) => {
  const [messages, setMessages] = useState([
    { 
      sender: 'bot', 
      text: 'Namaste! 🙏 Main hoon Climate AI Assistant.\n\nMujhse pucho:\n• Kisi city/state ka climate prediction\n• Temperature trends\n• Carbon emissions\n• Solutions aur tips\n\nEnglish, Hindi ya Hinglish - jo comfortable ho!',
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = {
      sender: 'user',
      text: input,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });

      const data = await response.json();
      
      const botMsg = {
        sender: 'bot',
        text: data.response,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      const errorMsg = {
        sender: 'bot',
        text: '⚠️ Backend se connect nahi ho pa raha.\n\nPlease check karo:\n1. Backend chal raha hai\n2. Internet connection check karo',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMsg]);
    }

    setLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const quickQuestions = [
    "Lucknow ka temperature",
    "Delhi climate",
    "Mumbai prediction",
    "2050 tak kya hoga?",
    "Carbon neutrality",
    "Help"
  ];

  return (
    <Box 
      bg="gray.800" 
      borderRadius="2xl" 
      p={4} 
      h="calc(100vh - 200px)"
      minH="600px"
      display="flex" 
      flexDirection="column"
      border="2px"
      borderColor="green.500/30"
      boxShadow="0 0 40px rgba(34, 197, 94, 0.1)"
    >
      {/* Header */}
      <Flex align="center" borderBottom="2px" borderColor="gray.700" pb={3} mb={3}>
        <Avatar bg="green.500" size="md">
          <FaRobot size={20} />
        </Avatar>
        <Box ml={3} flex={1}>
          <Heading size="md" color="green.400">Eco-AI Assistant</Heading>
          <Flex gap={2} mt={1}>
            <Badge colorScheme="green" fontSize="8px">Hinglish</Badge>
            <Badge colorScheme="blue" fontSize="8px">Hindi</Badge>
            <Badge colorScheme="purple" fontSize="8px">English</Badge>
          </Flex>
        </Box>
        <Box w="3" h="3" bg="green.500" borderRadius="50%" animation="pulse 2s infinite"></Box>
      </Flex>

      {/* Messages */}
      <Box 
        flex={1} 
        overflowY="auto" 
        mb={4} 
        p={2}
        css={{
          '&::-webkit-scrollbar': { width: '6px' },
          '&::-webkit-scrollbar-track': { background: '#1e293b' },
          '&::-webkit-scrollbar-thumb': { background: '#3b82f6', borderRadius: '3px' }
        }}
      >
        <VStack spacing={3} align="stretch">
          {messages.map((msg, idx) => (
            <Box
              key={idx}
              bg={msg.sender === 'user' ? 'blue.600' : 'gray.700'}
              p={3}
              borderRadius="xl"
              align={msg.sender === 'user' ? 'right' : 'left'}
              maxW="90%"
              whiteSpace="pre-wrap"
              boxShadow="md"
            >
              <Text fontSize="sm">{msg.text}</Text>
              <Text 
                fontSize="xs" 
                color={msg.sender === 'user' ? 'blue.200' : 'gray.400'}
                mt={1}
                textAlign="right"
              >
                {new Date(msg.timestamp).toLocaleTimeString([], { 
                  hour: '2-digit', 
                  minute: '2-digit' 
                })}
              </Text>
            </Box>
          ))}
          {loading && (
            <Box bg="gray.700" p={3} borderRadius="xl" align="left" maxW="85%">
              <Spinner size="sm" color="blue.500" />
            </Box>
          )}
          <div ref={messagesEndRef} />
        </VStack>
      </Box>

      {/* Quick Questions */}
      <Box mb={3}>
        <Text fontSize="xs" color="gray.500" mb={2} fontWeight="600">⚡ Quick Ask:</Text>
        <Flex wrap="wrap" gap={2}>
          {quickQuestions.map((q, idx) => (
            <Button
              key={idx}
              size="xs"
              variant="outline"
              borderColor="gray.600"
              color="gray.400"
              _hover={{ bg: 'blue.600', color: 'white', borderColor: 'blue.500' }}
              onClick={() => setInput(q)}
            >
              {q}
            </Button>
          ))}
        </Flex>
      </Box>

      {/* Input */}
      <Flex gap={2}>
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question..."
          bg="gray.700"
          border="2px"
          borderColor="gray.600"
          _hover={{ borderColor: 'blue.500' }}
          _focus={{ borderColor: 'blue.500', boxShadow: '0 0 0 1px blue.500' }}
          disabled={loading}
        />
        <Button
          colorScheme="blue"
          onClick={sendMessage}
          disabled={loading || !input.trim()}
          px={6}
          borderRadius="xl"
        >
          <Icon as={FaPaperPlane} />
        </Button>
      </Flex>
    </Box>
  );
};

export default HinglishChatbot;
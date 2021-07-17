import React from "react";
import {
  Button,
  Flex,
  useColorMode,
  VStack,
  Select,
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  Box,
  HStack,
  Text,
  Center,
  Heading,
} from "@chakra-ui/react";
import { SiAtom } from "react-icons/si";
import { Progress } from "@chakra-ui/react";

const colorScheme = [
  {
    backgroundImage: "linear-gradient( 135deg, #ABDCFF 10%, #0396FF 100%)",
    colorScheme: "telegram",
  },
  {
    backgroundImage: "linear-gradient( 135deg, #CE9FFC 10%, #7367F0 100%)",
    colorScheme: "purple",
  },
  {
    backgroundImage: "linear-gradient( 135deg, #90F7EC 10%, #32CCBC 100%)",
    colorScheme: "green",
  },
  {
    backgroundImage: "linear-gradient( 135deg, #FAD7A1 10%, #E96D71 100%)",
    colorScheme: "orange",
  },
];

function Card({ topic, index }) {
  return (
    <Box
      bg="blue.500"
      py={9}
      px={12}
      w="em"
      borderRadius="lg"
      mb="1em"
      color="white"
      style={{
        backgroundImage: colorScheme[index].backgroundImage,
      }}
    >
      <HStack>
        <Heading as="h3" size="md">
          {topic.name}
        </Heading>
        {/* {topic.icon} */}
      </HStack>

      <HStack align="center">
        <Progress
          colorScheme={colorScheme[index].colorScheme}
          mt="0.5em"
          value={topic.progress}
          h="0.3em"
          borderRadius="1em"
          w="10em"
        />
        <Text align="center">{topic.progress}</Text>
      </HStack>
    </Box>
  );
}

export default Card;

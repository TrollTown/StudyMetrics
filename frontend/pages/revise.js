import Head from "next/head";
import Image from "next/image";
import {
  Button,
  Flex,
  Heading,
  useColorMode,
  VStack,
  Select,
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  Box,
  Grid,
  HStack,
  Center,
  Text,
  RadioGroup,
  Radio,
} from "@chakra-ui/react";
import Chart from "../components/Chart";
import Layout from "../components/Layout";
import Card from "../components/Card";
import { SiAtom } from "react-icons/si";
import { BiShapeTriangle, BiDna } from "react-icons/bi";
import { AiOutlineStock } from "react-icons/ai";
import React, { useState, useEffect } from "react";
import { Progress } from "@chakra-ui/react";
import { ArrowForwardIcon } from "@chakra-ui/icons";
import { useRouter } from "next/router";

export default function Revise() {
  const [questionNum, setQuestionNum] = useState(1);
  const router = useRouter();

  const { qID } = router.query;
  const [questionID, setQuestionID] = useState(1);
  const [answer, setAnswer] = useState("");

  useEffect(async () => {
    const options = {
      method: "GET",
    };

    const res = await fetch(
      `https://api.production.hackathon.outki.org/get_revision_questions?studentID=5`,
      options
    );
    const data = await res.json();
    console.log(data);
  }, []);

  return (
    <Layout>
      <VStack
        style={{ minWidth: "calc(100vw - 17em)" }}
        minH="100vh"
        spacing="2em"
      >
        <HStack
          justify="spaceAround"
          align="stretch"
          spacing="1em"
          w="100%"
          h="0.5em"
          mb="6em"
        >
          <Box bg="blue.500" borderRadius="1em" flex="1" />
          <Box bg="blue.500" borderRadius="1em" flex="1" />
          <Box bg="blue.500" borderRadius="1em" flex="1" />
          <Box bg="blue.500" borderRadius="1em" flex="1" />
          <Box bg="gray.500" borderRadius="1em" flex="1" />
        </HStack>
        <VStack spacing="0.5em">
          <Heading as="h3" color="#1E2D38">
            Question 1
          </Heading>
          <HStack>
            <Heading size="md">Derivatives · </Heading>
            <Heading size="md" color="gray.500">
              Chain Rule
            </Heading>
          </HStack>
        </VStack>
        <Text maxW="50em">
          Lorem ipsum dolor si t amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </Text>
        <RadioGroup onChange={setAnswer} value={answer}>
          <VStack>
            <Radio value="1">Answer 1</Radio>
            <Radio value="2">Answer 2</Radio>
            <Radio value="3">Answer 3</Radio>
            <Radio value="4">Answer 4</Radio>
          </VStack>
        </RadioGroup>
        <Button rightIcon={<ArrowForwardIcon />} colorScheme="blue">
          Next Question
        </Button>
      </VStack>
    </Layout>
  );
}

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
import StudentLayout from "../components/StudentLayout";
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
  const [question, setQuestion] = useState();
  const [answer, setAnswer] = useState("");

  const questions = [
    {
      questionID: "204",
      subjectID: "HSC Mathematics Extension 2",
      moduleID: "Integration",
      submoduleID: "9",
      questionText:
        "Consider the statement: ‘If n is even, then if n is a multiple of 3, then n is a multiple of 6’. Which of the following is the negation of this statement?",
      options: [
        "n is odd and n is not a multiple of 3 or 6",
        "n is even and n is a multiple of 3 but not a multiple of 6",
        "If n is even, then n is not a multiple of 3 and n is not a multiple of 6. multiple of 6.",
        "If n is odd, then if n is not a multiple of 3 then n is not a multiple of 6.",
      ],
      questionType: "mc",
      photo: null,
      difficulty: 2,
      starred: false,
      module: "Proofs",
      subModule: "Proofs by Contradiction",
    },
    {
      questionID: "200",
      subjectID: "HSC Mathematics Extension 2",
      moduleID: "Integration",
      submoduleID: "Integration by Parts",
      questionText:
        "Using integration by parts, compute the following integral:int_1^5x^{2}ln(x)",
      questionType: "numerical",
      answer: "53.28",
      photo: null,
      difficulty: 2,
      starred: false,
    },
    {
      questionID: "201",
      subjectID: "HSC Mathematics Extension 2",
      moduleID: "Integration",
      submoduleID: "9",
      questionText: "Find:int_{}^{}\frac{16x-43}{(x-3)^2(x+2)}dx",
      questionType: "whiteboard",
      photo: null,
      difficulty: 2,
      starred: false,
    },
    {
      questionID: "202",
      subjectID: "HSC Mathematics Extension 2",
      moduleID: "Integration",
      submoduleID: "7",
      questionText:
        "Find:int_{}^{}\frac{x}{sqrt{1-x}}dx:using the substitution:u=1+x^2",
      questionType: "whiteboard",
      photo: null,
      difficulty: 2,
      starred: false,
    },
    {
      questionID: "203",
      subjectID: "HSC Mathematics Extension 2",
      moduleID: "Integration",
      submoduleID: "7",
      questionText:
        "Solve:int_{\frac{}{}}^{}\frac{1}{sqrt{e^{2x}-1}} where xge  0",
      questionType: "whiteboard",
      photo: null,
      difficulty: 2,
      starred: false,
    },
  ];

  return (
    <StudentLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }} spacing="2em">
        <HStack
          justify="spaceAround"
          align="stretch"
          spacing="1em"
          w="100%"
          h="0.3em"
          mb="6em"
        >
          <Box bg="blue.500" borderRadius="1em" flex="1" />
          <Box bg="gray.500" borderRadius="1em" flex="1" />
          <Box bg="gray.500" borderRadius="1em" flex="1" />
          <Box bg="gray.500" borderRadius="1em" flex="1" />
          <Box bg="gray.500" borderRadius="1em" flex="1" />
        </HStack>
        <VStack spacing="0.5em">
          <Heading as="h3" color="#1E2D38">
            Question {questionNum}
          </Heading>
          <HStack>
            <Heading size="md">{questions[questionNum - 1].module} ·</Heading>
            <Heading size="md" color="gray.500">
              {questions[questionNum - 1].subModule}
            </Heading>
          </HStack>
        </VStack>
        <Text maxW="50em">{questions[questionNum - 1].questionText}</Text>
        <RadioGroup onChange={setAnswer} value={answer}>
          <VStack>
            <Radio value="1" alignSelf="start">
              {questions[questionNum - 1].options[0]}
            </Radio>
            <Radio alignSelf="start" value="2">
              {questions[questionNum - 1].options[1]}
            </Radio>
            <Radio alignSelf="start" value="3">
              {questions[questionNum - 1].options[2]}
            </Radio>
            <Radio alignSelf="start" value="4">
              {questions[questionNum - 1].options[3]}
            </Radio>
          </VStack>
        </RadioGroup>
        <Button rightIcon={<ArrowForwardIcon />} colorScheme="blue">
          Next Question
        </Button>
      </VStack>
    </StudentLayout>
  );
}

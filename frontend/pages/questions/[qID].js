import { React, useEffect, useState } from "react";
import {
  Button,
  Text,
  Heading,
  HStack,
  VStack,
  RadioGroup,
  Radio,
  Image,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
  Tooltip,
  Icon,
} from "@chakra-ui/react";
import {
  ArrowForwardIcon,
  CheckIcon,
  CloseIcon,
  CheckCircleIcon,
} from "@chakra-ui/icons";
import { useRouter } from "next/router";
import StudentLayout from "../../components/StudentLayout";

export default function Question() {
  const router = useRouter();
  const { qID } = router.query;
  const [routerReady, setRouterReady] = useState(false);
  const [questionData, setQuestionData] = useState({});
  const [subjectName, setSubjectName] = useState("");
  const [moduleName, setModuleName] = useState("");
  const [submoduleName, setSubmoduleName] = useState("");
  const [answerMC, setAnswerMC] = useState("");
  const [answerCorrect, setAnswerCorrect] = useState(false);
  const [answerRevealed, setAnswerRevealed] = useState(false);
  const [answerNum, setAnswerNum] = useState("");

  console.log(qID)

  if (router.isReady && routerReady === false) {
    setRouterReady(true);
  }

  useEffect(() => {
    if (routerReady) {
      fetchQuestionData();
    }
  }, [routerReady]);

  const fetchQuestionData = async () => {
    const options = {
      method: "GET",
    };

    let res = await fetch(
      `https://api.production.hackathon.outki.org/get_question_by_ID?questionID=${qID}`,
      options
    );
    const qData = await res.json();
    console.log(qData);
    setQuestionData(qData);
    res = await fetch(
      `https://api.production.hackathon.outki.org/get_subject_by_ID?subjectID=${qData.subjectID}`,
      options
    );
    const subData = await res.json();
    console.log(subData);
    setSubjectName(subData.subjectName);
    res = await fetch(
      `https://api.production.hackathon.outki.org/get_module_by_ID?moduleID=${qData.moduleID}`,
      options
    );
    const mData = await res.json();
    console.log(mData);
    setModuleName(mData.moduleName);
    res = await fetch(
      `https://api.production.hackathon.outki.org/get_submodule_by_ID?submoduleID=${qData.submoduleID}`,
      options
    );
    const sData = await res.json();
    console.log(sData);
    setSubmoduleName(sData.submoduleName);
  };

  const handleSubmit = async () => {
    let answer;

    if (questionData.questionType === "mc") {
      answer = answerMC;
    } else if (questionData.questionType === "numerical") {
      answer = answerNum;
    } else {
      answer = "base64";
    }

    const body = {
      questionID: questionData.questionID,
      studentID: window.sessionStorage.getItem("token"),
      answer: answer,
    };

    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    };

    const res = await fetch(
      "https://api.production.hackathon.outki.org/submit_answer",
      options
    );
    const data = await res.json();
    console.log(data);
    if (data.result) {
      setAnswerCorrect(true);
    } else {
      setAnswerCorrect(false);
    }
    setAnswerRevealed(true);
  };

  const handleNext = async () => {
    const options = {
      method: "GET",
    };

    const res = await fetch(
      `https://api.production.hackathon.outki.org/get_next_question?studentID=${window.sessionStorage.getItem(
        "token"
      )}&submoduleID=${questionData.submoduleID}`,
      options
    );
    const data = await res.json();
    console.log(data);
    // setRouterReady(false);
    // setAnswerRevealed(false);
    // setAnswerMC(false);
    // setAnswerNum(false);
    router.push(`/questions/next/${data.questionID}`)
  }

  if (!router.isReady) {
    return <></>;
  } else {
    return (
      <StudentLayout>
        <HStack minWidth="calc(100vw - 17em)" justifyContent="space-between">
          <Heading as="h3" color="#1E2D38" alignSelf="center">
            Questions
          </Heading>
          <Heading as="h3" color="#1E2D38">
            {subjectName}
          </Heading>
        </HStack>
        <VStack m="6em" spacing="2em">
          <VStack spacing="0.5em">
            <Heading size="lg">{moduleName}</Heading>
            <Heading size="md" color="gray.500">
              {submoduleName}
            </Heading>
          </VStack>
          <Text>{questionData.questionText}</Text>
          <Image maxWidth="400px" height="auto"></Image>
          {questionData.questionType === "mc" && (
            <Tooltip
              hasArrow
              label={answerCorrect ? "Correct" : "Incorrect"}
              bg={answerCorrect ? "green" : "red"}
              isOpen={answerRevealed}
              placement="top"
            >
              <RadioGroup onChange={setAnswerMC} value={answerMC}>
                <VStack>
                  <Radio value="A">{questionData.options[0]}</Radio>
                  <Radio value="B">{questionData.options[1]}</Radio>
                  <Radio value="C">{questionData.options[2]}</Radio>
                  <Radio value="D">{questionData.options[3]}</Radio>
                </VStack>
              </RadioGroup>
            </Tooltip>
          )}
          {questionData.questionType === "numerical" && (
            <Tooltip
              hasArrow
              label={answerCorrect ? "Correct" : "Incorrect"}
              bg={answerCorrect ? "green" : "red"}
              isOpen={answerRevealed}
              placement="top"
            >
              <NumberInput
                size="lg"
                maxW={64}
                onChange={setAnswerNum}
                value={answerNum}
                allowMouseWheel
              >
                <NumberInputField />
                <NumberInputStepper>
                  <NumberIncrementStepper />
                  <NumberDecrementStepper />
                </NumberInputStepper>
              </NumberInput>
            </Tooltip>
          )}
          {answerRevealed && (
            <Icon
              as={answerCorrect ? CheckIcon : CloseIcon}
              color={answerCorrect ? "green" : "red"}
              boxSize="2em"
            />
          )}
          <Button
            rightIcon={
              answerRevealed ? <ArrowForwardIcon /> : <CheckCircleIcon />
            }
            colorScheme="blue"
            onClick={answerRevealed ? handleNext : handleSubmit}
          >
            {answerRevealed ? "Next Question" : "Submit Answer"}
          </Button>
        </VStack>
      </StudentLayout>
    );
  }
}

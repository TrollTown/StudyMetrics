import { useRouter } from "next/router";
import { useEffect } from "react";
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
  Stack,
  Grid,
  HStack,
  Input,
  Textarea,
  Checkbox,
  RadioGroup,
  Radio,
} from "@chakra-ui/react";
import StudentLayout from "../components/StudentLayout";
import React from "react";
import { useToast } from "@chakra-ui/react";

export default function upload() {
  const router = useRouter();

  const [loading, setLoading] = React.useState(false);
  const [message, setMessage] = React.useState("Submit");
  const toast = useToast();
  const [value, setValue] = React.useState(0);

  const handleClick = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      toast({
        title: "Success",
        description: "Your question was uploaded!",
        status: "success",
        duration: 4000,
        isClosable: true,
        position: "top",
      });
      setMessage("Submitted");
    }, 2000);

    //     setMessage("Uploaded");
  };
  return (
    <StudentLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }}>
        <Breadcrumb alignSelf="start">
          <BreadcrumbItem>
            <BreadcrumbLink href="#">All</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbItem>
            <BreadcrumbLink href="#">HSC Maths Extension 2</BreadcrumbLink>
          </BreadcrumbItem>
        </Breadcrumb>
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="2em">
          Upload Question
        </Heading>

        <Stack spacing="1em" alignSelf="start">
          <HStack>
            <VStack>
              <Heading as="h3" size="md" color="#1E2D38" alignSelf="start">
                Module
              </Heading>
              <Select w="15em" alignSelf="start" placeholder="Select module">
                <option value="option1">Integration</option>
                <option value="option2">Derivative</option>
                <option value="option3">Conics</option>
                <option value="option4">Proofs</option>
                <option value="option5">Complex Numbers</option>
              </Select>
            </VStack>
            <VStack>
              <Heading as="h3" size="md" color="#1E2D38" alignSelf="start">
                Submodule
              </Heading>
              <Select w="15em" alignSelf="start" placeholder="Select submodule">
                <option value="option6">U-substitution</option>
                <option value="option7">Trigonemtric Substitution</option>
                <option value="option8">Reduction Formulae</option>
                <option value="option9">Partial Fractions</option>
              </Select>
            </VStack>
          </HStack>

          <Heading as="h3" size="md" color="#1E2D38" alignSelf="start" mb="1em">
            Question
          </Heading>
          <Textarea placeholder="Question" w="50em" />
          <Heading as="h3" size="md" color="#1E2D38" alignSelf="start" mb="1em">
            Possible Responses
          </Heading>

          <Input placeholder="Option A" />

          <Input placeholder="Option B" />

          <Input placeholder="Option C" />

          <Input placeholder="Option D" />

          <Heading as="h3" size="md" color="#1E2D38" alignSelf="start" mb="1em">
            Correct Response
          </Heading>
          <RadioGroup onChange={setValue} value={value}>
            <Stack direction="row">
              <Radio value="1">A</Radio>
              <Radio value="2">B</Radio>
              <Radio value="3">C</Radio>
              <Radio value="4">D</Radio>
            </Stack>
          </RadioGroup>

          <HStack>
            <Button alignSelf="start" colorScheme="teal" variant="outline">
              Upload Image
            </Button>
            <Button
              onClick={handleClick}
              isLoading={loading}
              alignSelf="start"
              colorScheme="teal"
              variant="solid"
            >
              Submit
            </Button>
          </HStack>
        </Stack>
      </VStack>
    </StudentLayout>
  );
}

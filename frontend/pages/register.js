import React, { useState } from "react";
import {
  Button,
  Heading,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Link,
  Radio,
  RadioGroup,
  VStack,
  Icon,
  Center,
  Tooltip,
} from "@chakra-ui/react";
import { FaUser, FaKey } from "react-icons/fa";
import { IoIosMail } from "react-icons/io";
import { GiConfirmed } from "react-icons/gi";
import router from "next/router";

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [userType, setUserType] = useState("student");
  const [invalidPass, setInvalidPass] = useState(false);
  const [invalidName, setInvalidName] = useState(false);
  const [invalidEmail, setInvalidEmail] = useState(false);
  const [existingEmail, setExistingEmail] = useState(false);
  const [pwTooltipOpen, setPwTooltipOpen] = useState(false);
  const [nameTooltipOpen, setNameTooltipOpen] = useState(false);
  const [emailTooltipOpen, setEmailTooltipOpen] = useState(false);

  const handleChange = (e) => {
    switch (e.target.name) {
      case "name":
        setInvalidName(false);
        setNameTooltipOpen(false);
        setName(e.target.value);
        break;
      case "email":
        setInvalidEmail(false);
        setEmailTooltipOpen(false);
        setExistingEmail(false);
        setEmail(e.target.value);
        break;
      case "pass":
        setInvalidPass(false);
        setPwTooltipOpen(false);
        setPassword(e.target.value);
        break;
      case "passCon":
        setInvalidPass(false);
        setPwTooltipOpen(false);
        setPasswordConfirm(e.target.value);
        break;
      default:
        console.log("Error changing input");
    }
  };

  const handleClick = () => {
    if (name === "") {
      setInvalidName(true);
      setNameTooltipOpen(true);
      return;
    }
    if (email === "") {
      setInvalidEmail(true);
      setEmailTooltipOpen(true);
      return;
    }
    if (password.length < 8) {
      setInvalidPass(true);
      setPwTooltipOpen(true);
      return;
    }
    if (password != passwordConfirm) {
      setInvalidPass(true);
      setPwTooltipOpen(true);
      return;
    }

    const body = {
      name: name,
      email: email,
      password: password,
      userType: userType,
    };

    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    };

    fetch("https://api.production.hackathon.outki.org/register", options)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.result === "failed") {
          setInvalidEmail(true);
          setExistingEmail(true);
        } else {
          window.sessionStorage.setItem("token", data.token);
          window.sessionStorage.setItem("userType", userType);
          if (userType === "student") {
            router.push("/progress");
          } else {
            router.push("/allClasses");
          }
        }
      });
  };

  return (
    <VStack w="100vw" h="100vh" justify="center" spacing="6">
      <Heading>Register</Heading>
      <Center>
        <Tooltip
          hasArrow
          label="Please enter a name"
          bg="red"
          isOpen={nameTooltipOpen}
          placement="top"
        >
          <InputGroup>
            <InputLeftElement
              children={<Icon as={FaUser} color="gray.400" />}
            />
            <Input
              name="name"
              placeholder="Name"
              w="400px"
              m="4"
              onChange={handleChange}
              isInvalid={invalidName}
              m="0"
            />
          </InputGroup>
        </Tooltip>
      </Center>
      <Center>
        <Tooltip
          hasArrow
          label={
            existingEmail
              ? "That email already exists"
              : "Please enter an email"
          }
          bg="red"
          isOpen={emailTooltipOpen || existingEmail}
          placement="top"
        >
          <InputGroup>
            <InputLeftElement
              children={<Icon as={IoIosMail} color="gray.400" />}
            />
            <Input
              name="email"
              placeholder="Email"
              w="400px"
              m="4"
              onChange={handleChange}
              isInvalid={invalidEmail}
              m="0"
            />
          </InputGroup>
        </Tooltip>
      </Center>
      <Center>
        <Tooltip
          hasArrow
          label={
            password.length < 8
              ? "Password must be at least 8 characters"
              : "Passwords don't match"
          }
          bg="red"
          isOpen={pwTooltipOpen}
          placement="top"
        >
          <InputGroup>
            <InputLeftElement children={<Icon as={FaKey} color="gray.400" />} />
            <Input
              name="pass"
              type="password"
              placeholder="Password"
              w="400px"
              m="4"
              onChange={handleChange}
              isInvalid={invalidPass}
              m="0"
            />
          </InputGroup>
        </Tooltip>
      </Center>
      <Center>
        <InputGroup>
          <InputLeftElement
            children={<Icon as={GiConfirmed} color="gray.400" />}
          />
          <Input
            name="passCon"
            type="password"
            placeholder="Confirm Password"
            w="400px"
            m="4"
            onChange={handleChange}
            isInvalid={invalidPass}
            m="0"
          />
        </InputGroup>
      </Center>
      <RadioGroup onChange={setUserType} value={userType}>
        <HStack>
          <Radio value="student">Student</Radio>
          <Radio value="teacher">Teacher</Radio>
        </HStack>
      </RadioGroup>
      <HStack>
        <Button colorScheme="blue">
          <Link href="/login">Login</Link>
        </Button>
        <Button colorScheme="teal" onClick={handleClick}>
          Register
        </Button>
      </HStack>
    </VStack>
  );
}

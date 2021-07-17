import React, { useState } from "react";
import { Button, Heading, HStack, Input, InputGroup, InputLeftElement, Link, VStack, Icon, Center, Tooltip } from "@chakra-ui/react";
import { FaKey } from "react-icons/fa";
import { IoIosMail } from "react-icons/io";
import router from "next/router";

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [invalidPass, setInvalidPass] = useState(false);
  const [invalidEmail, setInvalidEmail] = useState(false);
  const [pwTooltipOpen, setPwTooltipOpen] = useState(false);
  const [invalidCreds, setInvalidCreds] = useState(false);
  const [emailTooltipOpen, setEmailTooltipOpen] = useState(false);

  const handleChange = (e) => {
    switch (e.target.name) {
      case "email":
        setInvalidEmail(false);
        setEmailTooltipOpen(false);
        setInvalidCreds(false);
        setEmail(e.target.value);
        break;
      case "pass":
        setInvalidPass(false);
        setPwTooltipOpen(false);
        setInvalidCreds(false);
        setPassword(e.target.value);
        break;
      default:
        console.log('Error changing input')
    }
  }

  const handleClick = () => {
    if (email === '') {
      setInvalidEmail(true);
      setEmailTooltipOpen(true);
      return;
    }
    if (password === '') {
      setInvalidPass(true);
      setPwTooltipOpen(true);
      return;
    }

    const body = {
      email: email,
      password: password,
    };

    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    };

    fetch('https://api.production.hackathon.outki.org/login', options)
      .then(res => res.json())
        .then(data => {
          console.log(data)
          if (data.result === "failed") {
            setInvalidCreds(true);
          } else {
            window.sessionStorage.setItem('token', data.token);
            window.sessionStorage.setItem('userType', data.type);
            router.push('/progress')
            if (data.type === "student") {
              router.push('/progress')
            } else {
              router.push('/classes')
            }
          }
        })
  }

  return (
    <VStack w="100vw" h="100vh" justify="center" spacing="6">
      <Heading>Login</Heading>
      <Center>
        <Tooltip hasArrow label={invalidCreds ? "Invalid credentials" : "Please enter an email"} bg="red" isOpen={emailTooltipOpen || invalidCreds} placement="top">
          <InputGroup>
            <InputLeftElement children={<Icon as={IoIosMail} color="gray.400" />} />
            <Input name="email" placeholder="Email" w="400px" m="4" onChange={handleChange} isInvalid={invalidEmail || invalidCreds} m="0" />
          </InputGroup>
        </Tooltip>
      </Center>
      <Center>
        <Tooltip hasArrow label="Please enter a password" bg="red" isOpen={pwTooltipOpen} placement="top">
          <InputGroup>
            <InputLeftElement children={<Icon as={FaKey} color="gray.400" />} />
            <Input name="pass" type="password" placeholder="Password" w="400px" m="4" onChange={handleChange} isInvalid={invalidPass || invalidCreds} m="0"/>
          </InputGroup>
        </Tooltip>
      </Center>
      <HStack>
        <Button colorScheme="blue" onClick={handleClick}>Login</Button>
        <Button colorScheme="teal"><Link href="/register">Register</Link></Button>
      </HStack>
    </VStack>
  );
}

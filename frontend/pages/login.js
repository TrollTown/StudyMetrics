import { Box, Button, Heading, HStack, Input, VStack } from "@chakra-ui/react";

export default function Login() {
  return (
    <VStack w="100vw" h="100vh" justify="center" spacing="6">
      <Heading>Login</Heading>
      <Input placeholder="Username" w="400px" m="4" />
      <Input type="password" placeholder="Password" w="400px" m="4" />
      <HStack>
        <Button colorScheme="blue">Login</Button>
        <Button colorScheme="teal">Register</Button>
      </HStack>
    </VStack>
  );
}
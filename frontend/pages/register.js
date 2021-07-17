import { Button, Heading, HStack, Input, Link, VStack } from "@chakra-ui/react";

export default function Register() {
  return (
    <VStack w="100vw" h="100vh" justify="center" spacing="6">
      <Heading>Register</Heading>
      <Input placeholder="Name" w="400px" m="4" />
      <Input placeholder="Email" w="400px" m="4" />
      <Input type="password" placeholder="Password" w="400px" m="4" />
      <Input type="password" placeholder="Confirm Password" w="400px" m="4" />
      <HStack>
        <Button colorScheme="blue"><Link href="/login">Login</Link></Button>
        <Button colorScheme="teal">Register</Button>
      </HStack>
    </VStack>
  );
}

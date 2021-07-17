import Head from "next/head";
import Image from "next/image";
import { Button, Flex, useColorMode } from "@chakra-ui/react";
import Layout from "../components/Layout";

export default function Home() {
  return (
    <Layout>
      <Button colorScheme="blue">Chakra Button</Button>
    </Layout>
  );
}

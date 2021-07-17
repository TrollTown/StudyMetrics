import Head from "next/head";
import Image from "next/image";
import { Button, Flex, Heading, useColorMode, VStack } from "@chakra-ui/react";
import Chart from "../components/Chart";
import Layout from "../components/Layout";

export default function Home() {
  return (
    <Layout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }} spacing="2em">
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          HSC Mathematics Extension 2
        </Heading>
        <Chart />
      </VStack>
    </Layout>
  );
}

import Head from "next/head";
import Image from "next/image";
import { Button, Flex, useColorMode } from "@chakra-ui/react";
import Chart from "../components/Chart";
import Layout from "../components/Layout";

export default function Home() {
  return (
    <Layout>
      <Chart />
    </Layout>
  );
}

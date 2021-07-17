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
} from "@chakra-ui/react";
import Chart from "../components/Chart";
import Layout from "../components/Layout";
import Card from "../components/Card";

export default function Progress() {
  return (
    <Layout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }}>
        <Breadcrumb alignSelf="start">
          <BreadcrumbItem>
            <BreadcrumbLink href="#">All</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbItem>
            <BreadcrumbLink href="#">HSC Maths Extension 2</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbItem isCurrentPage>
            <BreadcrumbLink href="#">s</BreadcrumbLink>
          </BreadcrumbItem>
        </Breadcrumb>
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          Progress
        </Heading>
        <Chart />
      </VStack>
    </Layout>
  );
}

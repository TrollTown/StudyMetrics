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
import StudentLayout from "../components/StudentLayout";
import Card from "../components/Card";
import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";

export default function ProgressMath() {
  const router = useRouter();
  const handleClick = () => {
    router.push("/progressMath");
  };

  return (
    <StudentLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }}>
        <Breadcrumb alignSelf="start">
          <BreadcrumbItem>
            <BreadcrumbLink href="progress">All</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbItem>
            <BreadcrumbLink href="#">HSC Maths Extension 2</BreadcrumbLink>
          </BreadcrumbItem>
        </Breadcrumb>
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          Progress
        </Heading>
        <Chart message="Your Performance" type="math" />
      </VStack>
    </StudentLayout>
  );
}

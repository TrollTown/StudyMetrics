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
  Grid,
} from "@chakra-ui/react";
import Chart from "../components/Chart";
import TeacherLayout from "../components/TeacherLayout";
import Card from "../components/Card";
import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";

export default function allClasses() {
  const classes = [
    { name: "12AMathsExtII", progress: 80 },
    { name: "12CMathsExtII", progress: 70 },
    { name: "11BMath", progress: 40 },
    { name: "10AMath", progress: 50 },
    { name: "9GMath", progress: 50 },
    { name: "7RMath", progress: 50 },
  ];

  const router = useRouter();
  const handleClick = () => {
    router.push("/classes");
  };

  return (
    <TeacherLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }} spacing="2em">
        {/* <Breadcrumb alignSelf="start">
          <BreadcrumbItem>
            <BreadcrumbLink href="#">All</BreadcrumbLink>
          </BreadcrumbItem>
        </Breadcrumb> */}
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          Class Performance
        </Heading>
        <Chart message="Average Performance" />

        <Grid templateColumns="repeat(3, 1fr)" gap={3}>
          {classes.map((eduClass, index) => (
            <div onClick={handleClick} key={index}>
              <Card topic={eduClass} index={index} />
            </div>
          ))}
        </Grid>
      </VStack>
    </TeacherLayout>
  );
}

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
  Divider,
} from "@chakra-ui/react";
import Chart from "../components/Chart";
import StudentLayout from "../components/StudentLayout";
import Card from "../components/Card";
import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { SiAtom } from "react-icons/si";
import { BiShapeTriangle, BiDna } from "react-icons/bi";
import { AiOutlineStock } from "react-icons/ai";
import { GiFountainPen } from "react-icons/gi";

export default function Progress() {
  const classes = [
    { name: "HSC Physics", icon: <SiAtom />, progress: 80 },
    { name: "HSC Maths Ext2", icon: <BiShapeTriangle />, progress: 70 },
    { name: "HSC Biology", icon: <BiDna />, progress: 40 },
    { name: "HSC Economics", icon: <AiOutlineStock />, progress: 50 },
    { name: "HSC Maths Ext1", icon: <BiShapeTriangle />, progress: 50 },
    { name: "HSC English Advanced", icon: <GiFountainPen />, progress: 50 },
  ];

  const router = useRouter();
  const handleClick = () => {
    router.push("/progressMath");
  };

  return (
    <StudentLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }} spacing="2em">
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          Progress
        </Heading>
        <Chart message="Your Performance" type="all" />

        <Grid templateColumns="repeat(3, 1fr)" gap={3}>
          {classes.map((eduClass, index) => (
            <div onClick={handleClick} key={index}>
              <Card topic={eduClass} index={index} />
            </div>
          ))}
        </Grid>
      </VStack>
    </StudentLayout>
  );
}

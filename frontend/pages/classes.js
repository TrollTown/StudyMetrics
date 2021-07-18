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
import TeacherLayout from "../components/TeacherLayout";
import Card from "../components/Card";
import React, { useState, useEffect } from "react";

export default function classPerfomance() {
  return (
    <TeacherLayout>
      <VStack style={{ minWidth: "calc(100vw - 17em)" }}>
        <Breadcrumb alignSelf="start">
          <BreadcrumbItem>
            <BreadcrumbLink href="/allClasses">All</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbItem>
            <BreadcrumbLink href="#">HSC Maths Extension 2</BreadcrumbLink>
          </BreadcrumbItem>
        </Breadcrumb>
        <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
          Class Performance
        </Heading>
        <Chart message="Average Performance" />
      </VStack>
    </TeacherLayout>
  );
}

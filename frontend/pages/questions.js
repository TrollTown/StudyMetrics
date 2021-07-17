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
import Layout from "../components/Layout";
import Card from "../components/Card";
import { SiAtom } from "react-icons/si";
import { BiShapeTriangle, BiDna } from "react-icons/bi";
import { AiOutlineStock } from "react-icons/ai";
import React, { useState } from "react";

export default function Progress() {
  const topics = [
    { name: "Physics", icon: <SiAtom />, progress: 80 },
    { name: "Mathematics", icon: <BiShapeTriangle />, progress: 70 },
    { name: "Biology", icon: <BiDna />, progress: 40 },
    { name: "Economics", icon: <AiOutlineStock />, progress: 50 },
  ];

  const [level, setLevel] = useState("subject");
  //   const [topics, setTopics] = useState([]);

  // request for subjects

  const handleClick = () => {
    if (level === "subjects") {
      // request for modules and update topics
      // setLevel("modules")
    } else if (level === "modules") {
      // request for submodules and update topics
      // setLevel("submodules")
    } else if (level === "submodules") {
      // request for a question from that submodule
    }
  };

  return (
    <Layout>
      <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
        Questions
      </Heading>
      <Grid templateColumns="repeat(3, 1fr)" gap={3}>
        {topics.map((topic, index) => (
          <Card topic={topic} key={index} index={index} />
        ))}
      </Grid>
    </Layout>
  );
}

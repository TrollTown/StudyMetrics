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
import StudentLayout from "../components/StudentLayout";
import Card from "../components/Card";
import { SiAtom } from "react-icons/si";
import { BiShapeTriangle, BiDna } from "react-icons/bi";
import { AiOutlineStock } from "react-icons/ai";
import React, { useState } from "react";
import { useRouter } from "next/router";

export default function Progress() {
  const router = useRouter();
  const subjects = [
    { name: "Physics", icon: <SiAtom />, progress: 80 },
    { name: "Mathematics", icon: <BiShapeTriangle />, progress: 70 },
    { name: "Biology", icon: <BiDna />, progress: 40 },
    { name: "Economics", icon: <AiOutlineStock />, progress: 50 },
  ];

  const modules = [
    { name: "Integration", progress: 80 },
    { name: "Derivatives", progress: 30 },
    { name: "Conics", progress: 60 },
    { name: "Proofs", progress: 50 },
    { name: "Complex Numbers I", progress: 20 },
    { name: "Complex Numbers II", progress: 50 },
  ];

  const subModules = [
    { name: "Roots of Unity", progress: 50 },
    { name: "Square of Complex Number", progress: 60 },
    { name: "Polar and Exponential form", progress: 40 },
    { name: "Modulus and Argument", progress: 56 },
  ];

  const [topics, setTopics] = useState(subjects);
  const [level, setLevel] = useState("subjects");
  //   const [topics, setTopics] = useState([]);

  // request for subjects

  const handleClick = () => {
    console.log("leee");
    if (level === "subjects") {
      setTopics(modules);
      setLevel("modules");

      // request for modules and update topics
    } else if (level === "modules") {
      setTopics(subModules);
      setLevel("subModules");

      // request for submodules and update topics
    } else if (level === "subModules") {
      router.push("/questions/1");
      //       setTopics();
      // request for a question from that submodule
    }
  };

  return (
    <StudentLayout>
      <Heading as="h3" color="#1E2D38" alignSelf="start" mb="1em">
        Questions
      </Heading>
      <Grid templateColumns="repeat(3, 1fr)" gap={3}>
        {topics.map((topic, index) => (
          <div onClick={handleClick} key={index}>
            <Card topic={topic} index={index} />
          </div>
        ))}
      </Grid>
    </StudentLayout>
  );
}

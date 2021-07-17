import React from "react";
import {
  HStack,
  Stack,
  Link as ChakraLink,
  VStack,
  Button,
} from "@chakra-ui/react";
import Link from "next/link";
import { GiBrain, GiTeacher, GiSpellBook } from "react-icons/gi";
import { IoIosSpeedometer } from "react-icons/io";
import { RiQuestionnaireFill } from "react-icons/ri";
import { FaFileUpload } from "react-icons/fa";
import router from "next/router";

function Sidebar({ userType }) {
  let items = [];
  if (userType === "student") {
    items = [
      { name: "progress", icon: <IoIosSpeedometer size={18} /> },
      { name: "questions", icon: <RiQuestionnaireFill size={18} /> },
      { name: "revise", icon: <GiBrain size={18} /> },
    ];
  } else if (userType === "teacher") {
    items = [
      { name: "classes", icon: <GiTeacher size={18} /> },
      { name: "upload", icon: <FaFileUpload size={18} /> },
    ];
  }

  const handleLogout = () => {
    window.sessionStorage.removeItem("token");
    window.sessionStorage.removeItem("userType");
    router.push("/");
  };
  return (
    <VStack
      bg="#F5FAFE"
      w="15em"
      minH="100%"
      p={4}
      justifyContent="space-between"
    >
      <Stack color="#516284" spacing="1em" mt="0.5em">
        <HStack mb="1em" align="center" spacing="1em">
          <GiSpellBook />
          <Link href="/">App Name</Link>
        </HStack>
        {items.map((item) => (
          <ChakraLink
            _hover={{
              textDecoration: "none",
              color: "#283753",
            }}
            key={`/${item.name}`}
          >
            <HStack spacing="1em">
              {item.icon}
              <Link href={`/${item.name}`}>
                <a>{item.name.charAt(0).toUpperCase() + item.name.slice(1)}</a>
              </Link>
            </HStack>
          </ChakraLink>
        ))}
      </Stack>
      <Button colorScheme="purple" onClick={handleLogout}>
        Logout
      </Button>
    </VStack>
  );
}

export default Sidebar;

import React from "react";
import {
  Box,
  HStack,
  Stack,
  Link as ChakraLink,
  Center,
} from "@chakra-ui/react";
import Link from "next/link";
import { GiSpellBook } from "react-icons/gi";
import { GiBrain } from "react-icons/gi";
import { IoIosSpeedometer } from "react-icons/io";
import { RiQuestionnaireFill } from "react-icons/ri";

function Sidebar() {
  const items = [
    { name: "progress", icon: <IoIosSpeedometer size={18} /> },
    { name: "questions", icon: <RiQuestionnaireFill size={18} /> },
    { name: "revise", icon: <GiBrain size={18} /> },
  ];
  return (
    <Box bg="#F5FAFE" w="15em" minH="100%" p={4}>
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
    </Box>
  );
}

export default Sidebar;

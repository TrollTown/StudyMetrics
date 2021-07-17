import React from "react";
import { Box, HStack, Stack, Link as ChakraLink } from "@chakra-ui/react";
import Link from "next/link";
import { GiSpellBook } from "react-icons/gi";

function Sidebar() {
  const items = ["Progress", "Questions", "Revise"];
  return (
    <Box bg="#F5FAFE" w="15em" minH="100%" p={4}>
      <Stack color="#516284">
        <HStack mb="1em" align="center">
          <GiSpellBook />
          <Link href="/">App Name</Link>
        </HStack>

        {items.map((item) => (
          <ChakraLink
            _hover={{
              textDecoration: "none",
              color: "#283753",
            }}
          >
            <Link href={`/${item}`}>
              <a>{item}</a>
            </Link>
          </ChakraLink>
        ))}
      </Stack>
    </Box>
  );
}

export default Sidebar;

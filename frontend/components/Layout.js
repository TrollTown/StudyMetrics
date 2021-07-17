import { Flex } from "@chakra-ui/react";
import Sidebar from "./Sidebar";

export default function Layout({ children }) {
  return (
    <Flex minH="100vh">
      <Sidebar />
      <main style={{ padding: "2em" }}>{children}</main>
    </Flex>
  );
}

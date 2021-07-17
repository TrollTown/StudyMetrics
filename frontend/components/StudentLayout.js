import { Flex } from "@chakra-ui/react";
import Sidebar from "./Sidebar";

export default function StudentLayout({ children }) {
  return (
    <Flex minH="100vh">
      <Sidebar userType="student" />
      <main style={{ padding: "2em" }}>{children}</main>
    </Flex>
  );
}

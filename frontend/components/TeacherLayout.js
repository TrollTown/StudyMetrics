import { Flex } from "@chakra-ui/react";
import Sidebar from "./Sidebar";

export default function TeacherLayout({ children }) {
  return (
    <Flex minH="100vh">
      <Sidebar userType="teacher" />
      <main style={{ padding: "2em" }}>{children}</main>
    </Flex>
  );
}

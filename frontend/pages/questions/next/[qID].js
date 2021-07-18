import { useRouter } from "next/router";

export default function next() {
  const router = useRouter();
  const { qID } = router.query;
  if (router.isReady) {
    router.push(`/questions/${qID}`);
  }

  return <></>;
}

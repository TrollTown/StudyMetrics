import { useRouter } from 'next/router';
import { useEffect } from 'react';

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    if (window.sessionStorage.getItem('token') === null) {
      router.push('/login');
    } else {
      router.push('/progress')
    }
  });

  return (
    <div></div>
  );
}

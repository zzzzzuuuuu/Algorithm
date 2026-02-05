function solution(n, m) {
  let gcd = 0;

  for (let i = 1; i <= n; i++) {
    if (n % i === 0 && m % i === 0) gcd = i;
  }

  const lcm = (n * m) / gcd;

  return [gcd, lcm];
}
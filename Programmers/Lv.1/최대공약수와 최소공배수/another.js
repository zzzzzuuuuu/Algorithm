function solution(n, m) {
  const gcd = (a, b) => {
    while (b !== 0) {
      [a, b] = [b, a % b];
    }
    return a;
  }
  const GCD = gcd(n, m);
  const LCM = n * m / GCD;

  return [GCD, LCM];
}
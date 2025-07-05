function solution(a, b) {
  const A = a % 2;
  const B = b % 2;

  if (A && B) return a*a+b*b; // Math.pow(a, 2) + Math.pow(b, 2);
  else if (A | B) return 2*(a+b);
  else return Math.abs(a-b);
}
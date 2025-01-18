function solution(n) {
  let numbers = 0;
  if (n % 2) {
    for (let i=1; i<=n; i+=2) {
      numbers += i;
    }
  } else {
    for (let i=0; i<=n; i+=2) {
      numbers += i**2;
    }
  }
  return numbers;
}
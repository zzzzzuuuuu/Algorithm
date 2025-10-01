function solution(num1, num2) {
  console.log(Math.floor(num1 / num2)); // 항상 작은 정수 쪽 내림
  console.log(Math.trunc(num1 / num2)); // 소수점 자름, floor와 음수일 때 다름
  console.log(~~(num1 / num2)); // 비트 반전 연산자, 두 번 하면 원래 숫자로 돌아가되 소수점 사라짐
  console.log((num1 / num2) >> 0); // 32비트 부호있는 정수로 변환하면서 소수점 이하를 버림
}
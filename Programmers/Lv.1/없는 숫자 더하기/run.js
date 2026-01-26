function solution(numbers) {
  const number = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  let result = 0;

  for (const n of number) {
    if (!numbers.includes(n)) result += n;
  }

  return result;
}
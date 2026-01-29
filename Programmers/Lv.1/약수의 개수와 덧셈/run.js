function solution(left, right) {
  let n = left;
  let result = 0;

  while (n <= right) {
    let count = 0;
    for (let i = 1; i <= n; i++) {
      if (n % i === 0) count++;
    }
    result = count % 2 ? result -  n : result + n;
    n++;
  }

  return result;
}